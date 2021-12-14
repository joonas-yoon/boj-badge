import os
import logging
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from utils import pack2str, default_label, deco_text, query_to_key
from pybadges import badge as pybadge
from parsing import get_user
from exceptions import NoneError
import storage

APP_NAME = __name__

# Uncomment to logging stdout
# print = log.debug

def create_app():
  app = Flask(APP_NAME)

  DATABASE_URL = str(os.environ['DATABASE_URL']).replace('postgres://', 'postgresql://')
  app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
  app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = os.urandom(12).hex()

  gunicorn_logger = logging.getLogger('gunicorn.info')
  app.logger.handlers = gunicorn_logger.handlers
  app.logger.setLevel(gunicorn_logger.level)

  return app


app = create_app()
db = SQLAlchemy(app)

print(pack2str('app.config', app.config))
print(pack2str('db', db))

# Defaults to stdout
logging.basicConfig(level=logging.INFO)

# get the logger for the current Python module
log = logging.getLogger(APP_NAME)


# Models
class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.String(32), primary_key=True)
  rank = db.Column(db.Integer, nullable=True)
  solved = db.Column(db.Integer, nullable=True)
  psolved = db.Column(db.Integer, nullable=True)
  failed = db.Column(db.Integer, nullable=True)
  submitted = db.Column(db.Integer, nullable=True)
  max_streak = db.Column(db.Integer, nullable=True)
  last_sync = db.Column(db.DateTime, nullable=True,
      default=datetime.utcnow)
  is_valid = db.Column(db.Boolean, nullable=True)


  def __str__(self):
    d = {
      'id': self.id,
      'rank': self.rank,
      'solved': self.solved,
      'psolved': self.psolved,
      'failed': self.failed,
      'submitted': self.submitted,
      'max_streak': self.max_streak,
      'last_sync': self.last_sync,
      'is_valid': self.is_valid,
    }
    return str(d)

  def columns():
    return ['id', 'rank', 'solved', 'psolved',
      'failed', 'submitted', 'max_streak', 'is_valid']

  def get(self, key):
    if not key in User.columns():
      return None
    return self.__dict__[key]


def get_and_update_user(username):
  print(pack2str('get_and_update_user', username))
  if username is None:
    return None
  db_query_result = User.query.filter_by(id=username)
  user = db_query_result.first()
  now = datetime.now()
  # not updated in 1 day
  if user is not None:
    if not user.is_valid:
      if now - timedelta(days=7) < user.last_sync:
        return None
    elif now - timedelta(days=1) < user.last_sync:
      return user
    # if it is invalid, update for 7 days
  print(pack2str('user[refresh]', user, now))

  # get latest
  data = get_user(username)

  # update
  if user is None:
    user = User(**data)
    db.session.add(user)
  else:
    db_query_result.update(data)
  db.session.commit()

  return user if user.is_valid else None


@app.route('/')
def main():
  username = request.args.get('id')
  # override
  query = request.args.get('query') or 'solved'
  key = query_to_key(query)
  label = request.args.get('label') or default_label(key)
  color = request.args.get('color') or '#0f80c1'
  try:
    user = get_and_update_user(username)
    if user is None:
      raise NoneError
    print(pack2str('user', user))
    value = str(user.get(key))
    print(f'key={key} value={value} query={query}')
    badge = pybadge(left_text=label, right_text=deco_text(query, value), right_color=color)
  except NoneError as err:
    badge = pybadge(left_text=label, right_text='invalid', right_color='#d57f69')
  except Exception as err:
    badge = pybadge(left_text=label, right_text='error', right_color='#ef2a2a')
    print(pack2str('[ERROR]', err))
  response = Response(str(badge), mimetype='image/svg+xml')
  response.cache_control.no_store = True
  return response


if __name__ == '__main__':
  db.create_all()
  app.run()

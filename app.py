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


  def __str__(self):
    d = {
      'id': self.id,
      'rank': self.rank,
      'solved': self.solved,
      'psolved': self.psolved,
      'failed': self.failed,
      'submitted': self.submitted,
      'max_streak': self.max_streak,
      'last_sync': self.last_sync
    }
    return str(d)

  def columns():
    return ['id', 'rank', 'solved', 'psolved', 'failed', 'submitted', 'max_streak']

  def get(self, key):
    if not key in User.columns():
      return None
    return self.__dict__[key]


def is_invalid_username(username):
  DB_NAME = 'invalids'
  data = storage.get_all(DB_NAME)
  if 'last_sync' in data:
    now = datetime.now()
    last_sync = datetime.fromisoformat(data['last_sync'])
    # too old, it needs to update
    if now >= last_sync + timedelta(days=7):
      return True
  if not 'users' in data:
    return False
  return username in data['users']


def save_invalid_username(username):
  DB_NAME = 'invalids'
  data = storage.get_all(DB_NAME)
  data['last_sync'] = datetime.now().isoformat()
  if not 'users' in data:
    data['users'] = []
  data['users'].append(username)
  storage.save(DB_NAME, data)


def get_and_update_user(username):
  print(pack2str('get_and_update_user', username))
  if username is None or is_invalid_username(username):
    return None
  db_query_result = User.query.filter_by(id=username)
  user = db_query_result.first()
  now = datetime.now()
  # not updated in 1 day
  if user is not None:
    if now - timedelta(days=1) < user.last_sync:
      return user
  print(pack2str('user[refresh]', user, now))

  # save update time first
  if user is None:
    db.session.add(User(id=username))
  else:
    user.last_sync = now
  db.session.commit()

  # get latest
  data = get_user(username)
  if data is None:
    save_invalid_username(username)
    return None

  # update
  if user is None:
    user = User(**data)
    db.session.add(user)
  else:
    db_query_result.update(data)
  db.session.commit()
  return user


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

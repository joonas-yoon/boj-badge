import os
import logging
import requests
import anybadge
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from utils import pack2str

APP_NAME = __name__
DATABASE_URL = str(os.environ['DATABASE_URL']).replace('postgres://', 'postgresql://')
print('DATABASE_URL', DATABASE_URL)

app = Flask(APP_NAME)

gunicorn_logger = logging.getLogger('gunicorn.info')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(12).hex()
db = SQLAlchemy(app)

print(pack2str('app.config', app.config))
print(pack2str('DATABASE_URL', DATABASE_URL))
print(pack2str('db', db))

# Defaults to stdout
logging.basicConfig(level=logging.INFO)

# get the logger for the current Python module
log = logging.getLogger(APP_NAME)


class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.String(32), primary_key=True)
  rank = db.Column(db.Integer, unique=True)
  solved = db.Column(db.Integer)
  psolved = db.Column(db.Integer)
  failed = db.Column(db.Integer)
  submitted = db.Column(db.Integer)
  last_sync = db.Column(db.DateTime, nullable=False,
      default=datetime.utcnow)

  def __str__(self):
    d = {
      'id': self.id,
      'rank': self.rank,
      'solved': self.solved,
      'psolved': self.psolved,
      'failed': self.failed,
      'submitted': self.submitted,
      'last_sync': self.last_sync
    }
    return str(d)

  def columns():
    return ['id', 'rank', 'solved', 'psolved', 'failed', 'submitted']

  def get(self, key):
    if not key in User.columns():
      return None
    return self.__dict__[key]


HOST = 'https://www.acmicpc.net'


def get_as(element, func):
  if element is None: return None
  return func(element.text)


def get_and_update_user(username):
  log.debug(pack2str('get_and_update_user', username))
  if username is None: return None
  db_query_result = User.query.filter_by(id=username)
  log.debug(pack2str('db_query_result', db_query_result))
  u = db_query_result.first()
  now = datetime.now()
  log.debug(pack2str('user', u, now))
  # not updated in 10 mins
  if u is not None and now - timedelta(minutes=10) < u.last_sync:
    return u
  href = HOST + f'/user/{username}'
  log.debug(pack2str(href))
  res = requests.get(href)
  log.debug(pack2str(res))
  # Not found returns None
  if res.status_code != 200:
    return None
  # find and update
  html = bs(res.text, 'html.parser')
  statics = html.select_one('#statics')
  rank = get_as(statics.find('tr').find('td'), int)
  submitted = get_as(html.select_one(f'a[href="/status?user_id={username}"]'), int)
  solved = get_as(statics.select_one('#u-solved'), int)
  psolved = get_as(statics.select_one('#u-psolved'), int)
  failed = get_as(statics.select_one('#u-failed'), int)
  data = {
    'id': username,
    'rank': rank,
    'solved': solved,
    'psolved': psolved,
    'failed': failed,
    'submitted': submitted,
    'last_sync': now
  }
  if u is None:
    u = User(**data)
    db.session.add(u)
  else:
    db_query_result.update(data)
  db.session.commit()
  return u


@app.route('/')
def main():
  username = request.args.get('id')
  label = request.args.get('label') or 'BOJ solved'
  query = request.args.get('query') or 'solved'
  color = request.args.get('color') or '#0f80c1'
  log.debug(pack2str(username, label, query, color))
  u = get_and_update_user(username)
  log.debug(pack2str(u))
  try:
    value = str(u.get(query.lower()))
    log.debug(value)
    badge = anybadge.Badge(
      label=label, value=value, default_color=color, num_padding_chars=1
    )
  except:
    badge = anybadge.Badge(
      label=label, value='invalid', default_color='#d55f49', num_padding_chars=1
    )
  return Response(str(badge), mimetype='image/svg+xml')


if __name__ == '__main__':
  db.create_all()
  app.run()

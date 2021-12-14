import re
from datetime import datetime, timedelta

def pack2str(*args):
  return ' '.join(map(str, args))


def get_as(element, func):
  if element is None: return None
  return func(element.text)


def get_streak(raw_html):
  p = re.search(r'user_day_problems = \[(.*),?\];', raw_html, re.DOTALL)
  # empty
  if p is None: return 0
  try:
    arr = re.sub(r'\d+\],?', '', p.group(1)).replace('[', '').split(',')
  except:
    return 0

  def ymd(s):
    y, m, d = map(int, [s[:4], s[4:6], s[6:]])
    return datetime(y, m, d)

  max_streak, cur_streak = 0, 0
  prev, cur = None, None
  for i in arr:
    if len(i) != 8: continue
    cur = ymd(i)
    if prev is None or prev + timedelta(days=1) != cur:
      cur_streak = 1
    else:
      cur_streak += 1
    prev = cur
    max_streak = max(max_streak, cur_streak)
  return max_streak


def default_label(query):
  key = str(query).lower()
  labels = {
    'rank': 'BOJ rank',
    'solved': 'BOJ solved',
    'psolved': 'BOJ partial solved',
    'failed': 'BOJ failed',
    'submitted': 'BOJ submitted',
    'max_streak': 'BOJ max streak',
  }
  if key in labels.keys():
    return labels[key]
  return 'BOJ badge'


def query_to_key(q):
  return (str(q)+' ').split(' ')[0]


def query_detail(q):
  q = str(q).split(' ')
  if len(q) <= 1: return None
  return q[1]


def deco_text(query, value):
  import storage
  DB_NAME = 'counter'

  key = query_to_key(query)
  qtype = query_detail(query)
  v = str(value)

  if key == 'max_streak':
    return v + ' day' + ('s' if int(value) > 1 else '')
  elif key == 'rank':
    ranks = storage.get(DB_NAME, 'rankings')
    if qtype == 'a':
      return f'{v} / {str(ranks)}'
    elif qtype == 'b':
      return '{:.4f}%'.format(int(value) / ranks * 100)
    elif qtype == 'c':
      return 'on {} page'.format((int(value) - 1) // 100 + 1)
  elif key == 'solved' \
    or key == 'psolved' \
    or key == 'failed':
    problems = storage.get(DB_NAME, 'problems_available')
    if qtype == 'a':
      return f'{v} / {str(problems)}'
    elif qtype == 'b':
      problems = storage.get(DB_NAME, 'problems_available')
      return '{:.2f}%'.format(int(value) / problems * 100)
  return str(value)

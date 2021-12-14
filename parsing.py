import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from time import sleep
from utils import pack2str, get_as, get_streak

import storage as JsonStore

HOST = 'https://www.acmicpc.net'
DB_NAME = 'counter'

def get_user(username):
  href = HOST + f'/user/{username}'
  res = requests.get(href)
  print(pack2str(href, res))
  # Not found returns None
  if res.status_code != 200:
    return None
  # get
  html = bs(res.text, 'html.parser')
  statics = html.select_one('#statics')
  rank = get_as(statics.find('tr').find('td'), int)
  submitted = get_as(html.select_one(f'a[href="/status?user_id={username}"]'), int)
  solved = get_as(statics.select_one('#u-solved'), int)
  psolved = get_as(statics.select_one('#u-psolved'), int)
  failed = get_as(statics.select_one('#u-failed'), int)
  max_streak = get_streak(res.text)
  return {
    'id': username,
    'rank': rank,
    'solved': solved,
    'psolved': psolved,
    'failed': failed,
    'submitted': submitted,
    'max_streak': max_streak,
    'last_sync': datetime.now()
  }


def do_count():
  count = JsonStore.get_all(DB_NAME)
  now = datetime.now()

  if 'last_sync' in count:
    last_sync = datetime.fromisoformat(count['last_sync'])
    if now < last_sync + timedelta(days=1):
      print("Skip count sync")
      return
  count['last_sync'] = now.isoformat()

  print("Start to sync...")
  res = requests.get(HOST)
  # get problem statistics
  html = bs(res.text, 'html.parser')
  pc = html.find_all(class_='counters')
  pc = [int(e.find(class_='counter').text) for e in pc]
  count['problems_total'] = pc[0]
  count['problems_available'] = pc[1]
  count['problems_solved'] = pc[2]
  JsonStore.save(DB_NAME, count)

  # get ranking, users
  res = requests.get(f'{HOST}/ranklist')
  html = bs(res.text, 'html.parser')
  page_end = html.find(class_='pagination').find_all('li')[-1]
  page_end = int(page_end.find('a')['href'].replace('/ranklist/', ''))
  sleep(5)
  res = requests.get(f'{HOST}/ranklist/{page_end}')
  html = bs(res.text, 'html.parser')
  ranklist = html.find(id='ranklist').find_all('tr')
  total_users = page_end * 100 + len(ranklist) - 1
  count['users'] = total_users
  try:
    count['rankings'] = int(ranklist[-1].find('td').text)
  except:
    count['rankings'] = total_users
  JsonStore.save(DB_NAME, count)

  print(count)

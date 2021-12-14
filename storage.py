import os
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def get_path(db_name):
  db_name = str(db_name).replace(' ', '')
  if not db_name.endswith('.json'):
    db_name = f'{db_name}.json'
  return os.path.join(BASE_DIR, db_name)


def get(db_name, key):
  try:
    return get_all(db_name)[key]
  except:
    return None


def get_all(db_name):
  create_if_not_exists(db_name)
  with open(get_path(db_name), 'r', encoding='utf-8') as f:
    try:
      obj = json.load(f)
    except:
      return {}
  return obj


def save(db_name, data):
  create_if_not_exists(db_name)
  with open(get_path(db_name), 'w+', encoding='utf-8') as f:
    json.dump(data, f)


def create_if_not_exists(db_name):
  db_name = get_path(db_name)
  if not os.path.exists(db_name):
    with open(db_name, 'w+', encoding='utf-8') as f:
      json.dump({}, f)


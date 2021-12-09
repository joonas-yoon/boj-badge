import os
import json
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
JSON_FILE = os.path.join(basedir, 'counter.json')
print(JSON_FILE)

def get(key):
  try:
    return get_all()[key]
  except:
    return None


def get_all():
  with open(JSON_FILE, 'r', encoding='utf-8') as f:
    try:
      obj = json.load(f)
    except:
      return {}
  return obj


def save(data):
  with open(JSON_FILE, 'w+', encoding='utf-8') as f:
    json.dump(data, f)


if not os.path.exists(JSON_FILE):
  save({})


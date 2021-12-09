web: gunicorn app:app --log-level=debug
init: python migrate.py db init
migrate: python migrate.py db migrate
upgrade: python migrate.py db upgrade

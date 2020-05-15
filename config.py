import os

workers = int(os.environ.get("GUNICORN_PROCESS", '3'))
threads = int(os.environ.get("GUNICORN_THREADS", '1'))

forwarded_allow_apis = "*"
secure_schema_headers = {'X-Forwarded-Proto': 'https'}

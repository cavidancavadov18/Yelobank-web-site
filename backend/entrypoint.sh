#!/bin/sh
set -eu

python - <<'PY'
import os
import time

import psycopg

host = os.environ.get("POSTGRES_HOST", "db")
port = os.environ.get("POSTGRES_PORT", "5432")
name = os.environ.get("POSTGRES_DB", "yelo")
user = os.environ.get("POSTGRES_USER", "yelo")
password = os.environ.get("POSTGRES_PASSWORD", "yelo")

for _ in range(60):
    try:
        psycopg.connect(dbname=name, user=user, password=password, host=host, port=port).close()
        break
    except Exception:
        time.sleep(1)
else:
    raise SystemExit("database not ready")
PY

python manage.py migrate --noinput
python manage.py ensure_superuser
python manage.py seed_demo
exec python manage.py runserver 0.0.0.0:8000

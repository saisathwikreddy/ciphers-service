#!/bin/ash
echo "Apply migrations"
cd ./ciphers_project python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
exec"$@"
# Criar projeto Django

python -m venv venv
source venv/bin/activate
pip install django
pip install djangorestframework
django-admin startproject core .
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
pip freeze > requirements.txt

pip install django-cors-headers

# Fazer Migracoes

python manage.py makemigrations
python manage.py migrate

pip install -r requirements.txt

# Criar uma app nova

python manage.py startapp units
settings.py > add app name in the INSTALLED_APPS

# Git set up

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Wemesonm/manufacturing-ticket-backend.git
git push -u origin main

# Load seed data

python manage.py loaddata "nome do arquivo

# Para fazer o download de todos os dados

python manage.py loaddata catalog_seed.json

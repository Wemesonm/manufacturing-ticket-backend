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
git remote add origin https://github.com/Wemesonm/drinksmachinebackend.git
git push -u origin main

# Load seed data

python manage.py loaddata "nome do arquivo

# Para fazer o download de todos os dados

python manage.py dumpdata references items drinks recipes --indent 2 > project_backup.json
python manage.py dumpdata references --indent 2 --output recipes/fixtures/recipes.json
python manage.py dumpdata references.ItemType --indent 2 --output references/fixtures/itemtype.json
python manage.py dumpdata references.Unit --indent 2 --output references/fixtures/unit.json
python manage.py dumpdata references.IceType --indent 2 --output references/fixtures/icetype.json
python manage.py dumpdata references.GlassType --indent 2 --output references/fixtures/glasstype.json
python manage.py dumpdata items --indent 2 --output items/fixtures/items.json

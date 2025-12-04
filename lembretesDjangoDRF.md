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

# Seed para copiar dados e enviar dados para o db

```bash

python manage.py dumpdata \
  --exclude auth \
  --exclude contenttypes \
  --exclude admin \
  --exclude sessions \
  --exclude tickets \
  --indent 2 > seed.json

```

```bash

python manage.py loaddata seed.json
```

# 🐳 Docker – Comandos Essenciais

```bash
docker pull <imagem>                     # Baixa uma imagem
docker images                            # Lista imagens locais
docker rmi <imagem>                      # Remove uma imagem
docker build -t <nome>:<tag> .           # Constrói imagem do Dockerfile
docker tag <imagem> <novo_nome>          # Cria nova tag para imagem

docker run <imagem>                      # Cria e inicia container
docker run -it <imagem> bash             # Container + terminal interativo
docker run -d <imagem>                   # Inicia em background
docker ps                                # Containers ativos
docker ps -a                             # Todos containers
docker stop <container>                  # Para container
docker start <container>                 # Inicia container parado
docker restart <container>               # Reinicia container
docker rm <container>                    # Remove container
docker logs <container>                  # Mostra logs
docker exec -it <container> bash         # Entra no terminal do container

docker volume ls                         # Lista volumes
docker volume create <nome>              # Cria volume
docker volume rm <nome>                  # Remove volume
docker run -v <volume>:<caminho> <img>   # Monta volume no container

docker network ls                        # Lista redes
docker network create <nome>             # Cria rede
docker network rm <nome>                 # Remove rede
docker network inspect <nome>            # Inspeciona rede

docker inspect <container/imagem>        # Detalhes avançados
docker stats                             # Uso de CPU/RAM em tempo real
docker system df                         # Espaço usado pelo Docker

docker system prune                       # Limpa objetos não usados
docker image prune                        # Remove imagens não usadas
docker container prune                    # Remove containers parados
docker volume prune                       # Remove volumes não usados

docker compose up                         # Sobe serviços
docker compose up -d                      # Sobe em background
docker compose down                       # Derruba serviços
docker compose logs -f                    # Logs em tempo real
docker compose build                      # Recompila imagens
```

# comando docker para iniciar o postgres

```bash
docker run -p 5433:5432 --name ticket_db -v postgres_data:/var/lib/postgresql/data/ -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=ticket --network=ticket_network postgres
```

# Comando de build para o docker hub

docker build --platform linux/amd64 -t wemeson/ticket_api:1.0 .

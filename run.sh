docker stop mysql-db
docker rm mysql-db
docker build -t mysql-db -f ./images/mysql-db/Dockerfile .
docker run --name mysql-db -p 3308:3306 -d mysql-db

poetry install
poetry run python3 src/app.py

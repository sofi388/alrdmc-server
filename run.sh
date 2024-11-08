docker stop postgres
docker rm postgres
docker run --name postgres -e POSTGRES_PASSWORD=pass -d postgres
poetry install
poetry run python3 src/app.py

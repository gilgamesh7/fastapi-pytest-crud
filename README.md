# fastapi-pytest-crud

# Links
- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/#additional-validation)


# Run the app
## VDI
uvicorn main:app --reload  (If __main__ not present)
<br>
run main.py from vscode
## CLI Docker
docker-compose up -d --build

# Access App
## Local Docker
http://localhost:8002/ping

# Docker Compose if not using VScode
docker-compose up -d --build

# Check database on Docker
- docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev
- List of databases : \l
- Connect : c hello_fastapi_dev
- List if relations : \dt

# Run test on Docker
docker-compose exec web pytest .

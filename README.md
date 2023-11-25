[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3113/)

#### Usage

The application require Python version 3.11 or older. In order to install the application on your local machine go through the following steps:
1. clone the repo using comand
 ```
git clone https://github.com/ADv0rnik/fastapi-microservices.git
 ```
2. Install and activate virtual environment.
For UNIX-based systems:
```commandline
   python -m venv venv
   source venv/bin/activate
```
3. Setup .env according to the structure displayed in .env.example 
4. Run docker compose
```commandline
docker compose up --build -d
```

5. In `app` container execute:
```commandline
alembic revision --autogenerate -m 'init db'
alembic upgrade head
python run_db.py
```
6. From `/rpc` run `python server.py` in order to up the rpc service
7. From `/gateway` run `python main.py` in order to up the gateway service

#### Notes
- You may want to connect to RabbitMQ GUI. In this case go to `127.0.0.1:15672` 
- Set RABIT_HOST to `0.0.0.0` 

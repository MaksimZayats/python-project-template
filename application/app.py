from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()


@app.on_event('startup')
async def on_startup() -> None:
    load_dotenv()

    pg_user = getenv('POSTGRES_USER')
    pg_password = getenv('POSTGRES_PASSWORD')
    pg_database = getenv('POSTGRES_DB')
    pg_host = getenv('POSTGRES_HOST')

    db_url = f'postgres://{pg_user}:{pg_password}@{pg_host}:5432/{pg_database}'  # type: ignore  # NOQA
    # connect to database using this url


@app.get('/')
def read_root():
    return {'Hello': 'World'}

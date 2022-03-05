from os import getenv

import uvicorn
from dotenv import load_dotenv

from application.app import app


def run():
    load_dotenv()

    uvicorn.run(app=app, host=getenv("HOST", "0.0.0.0"), port=getenv("PORT", 80))  # type: ignore


if __name__ == "__main__":
    run()

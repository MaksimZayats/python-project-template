from os import getenv

import uvicorn
from dotenv import load_dotenv

from application.app import app


def run():
    load_dotenv()

    if getenv("FROM_DOCKER", "").lower() in ("1", "true"):
        host = "0.0.0.0"
        port = 80
    else:
        host = getenv("HOST", "0.0.0.0")
        port = getenv("PORT", 80)

    uvicorn.run(app=app, host=host, port=port)  # type: ignore


if __name__ == "__main__":
    run()

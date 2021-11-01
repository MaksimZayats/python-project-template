# Python Project Template

## Features
* [pre-commit](.pre-commit-config.yaml)
* [CI: GitHub Actions](.github/workflows/code_checks.yml)
* Code checks
  * `flake8`
  * `isort`
  * `brunette (black)`
  * `mypy`
* [Docker](docker-compose.yml)
  * Database (`PostgreSQL`)
  * Reverse proxy (`Traefik`)
  * SSL Certificate (`letsencrypt`)
* [Tests (`Pytest`)](tests)

## Usage

* Docker
  * Configure `environment variables` or `.env` file as [`.env.dist`](.env.dist)
  * `docker-compose up --build --force-recreate`
* Default run
  * Configure `environment variables` or `.env` file
    * ```dotenv
      POSTGRES_DB=dev
      POSTGRES_USER=dev
      POSTGRES_PASSWORD=dev
      POSTGRES_HOST=127.0.0.1
      ```
  * `python -m uvicorn application.app:app`

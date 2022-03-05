# Python Project Template

## Features
* [pre-commit](.pre-commit-config.yaml)
* [CI: GitHub Actions](.github/workflows/code_checks.yml)
* Code checks
  * `flake8`
  * `isort`
  * `black`
  * `mypy`
* [Docker](docker-compose.yml)
  * Database (`PostgreSQL`)
  * Reverse proxy (`Traefik`)
  * SSL Certificate (`letsencrypt`)
* [Tests (`Pytest`)](tests)

## Usage

* Docker
  * Configure `environment variables` or `.env` file as [`.env.docker-example`](.env.docker-example)
  * `docker-compose up --build --force-recreate`
* Default run
  * Configure `environment variables` or `.env` file as [`.env.no-docker-example`](.env.no-docker-example)
  * `python run_server.py`

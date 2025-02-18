FROM python:3.13-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y libpq-dev gcc python3-dev

WORKDIR /var/www

COPY ./poetry.toml .
COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN python -m pip --no-cache-dir install --upgrade pip
RUN pip install --no-cache-dir poetry
RUN poetry install

COPY ./src ./src
COPY ./alembic.ini ./

CMD ["poetry", "run", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "80"]
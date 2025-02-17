FROM python:3.13-slim

WORKDIR /var/www

COPY ./poetry.toml .
COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN python -m pip --no-cache-dir install --upgrade pip
RUN pip install --no-cache-dir poetry
RUN poetry install

COPY ./src ./src

CMD ["poetry", "run", "fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "80"]
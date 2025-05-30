FROM python:3.13.2-slim

ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE 1

WORKDIR /src

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir poetry \
    && poetry self add poetry-plugin-export \
    && poetry lock \
    && poetry export --without-hashes -f requirements.txt --output requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
FROM python:3.12

WORKDIR /app
ADD . /app

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN poetry install --only=main && rm -rf $POETRY_CACHE_DIR

EXPOSE 105

CMD ["poetry", "run", "python", "src/app.py"]

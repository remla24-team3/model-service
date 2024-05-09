FROM python:3.12

WORKDIR /app
ADD . /app

RUN pip install poetry
RUN poetry install

EXPOSE 105


CMD ["poetry", "run", "python", "src/app.py"]
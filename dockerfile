FROM python:3.12

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get install pkg-config libhdf5-dev -y
RUN apt-get install python3-h5py -y

RUN pip install poetry
RUN poetry install

EXPOSE 105

CMD ["poetry", "run", "python", "src/app.py"]

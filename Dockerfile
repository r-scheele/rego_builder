FROM python:3.10 as python-base

RUN mkdir rego_builder
WORKDIR /rego_builder
RUN mkdir /tmp/fastgeoapi/
COPY /pyproject.toml /rego_builder

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 

COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.server.api:app", "--bind", "0.0.0.0:8080"]
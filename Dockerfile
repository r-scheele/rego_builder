<<<<<<< HEAD
FROM python:3.10

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . /app

=======
FROM python:3.10 as python-base
RUN mkdir rego_builder
WORKDIR /rego_builder
COPY /pyproject.toml /rego_builder

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY . .
>>>>>>> origin/main
CMD ["python3", "main.py"]
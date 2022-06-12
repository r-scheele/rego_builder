FROM python:3.10 as python-base


RUN mkdir rego_builder
WORKDIR /rego_builder
COPY pyproject.toml /rego_builder

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .




CMD ["python3", "main.py"]
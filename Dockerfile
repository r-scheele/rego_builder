FROM python:3.10 as python-base


RUN mkdir rego_builder
WORKDIR /rego_builder
COPY /app rego_builder/app
COPY pyproject.toml /rego_builder
COPY /main.py /rego_builder/main.py 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN export PYTHONPATH=${PWD} 
CMD ["python3", "main.py"]
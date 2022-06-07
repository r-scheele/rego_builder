FROM python:3.10

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . /app

CMD ["python3", "main.py"]
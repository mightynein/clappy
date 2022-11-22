FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip --disable-pip-version-check install -r requirements.txt

CMD ["python", "-m", "clappy"]

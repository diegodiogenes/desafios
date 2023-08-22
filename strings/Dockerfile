FROM python:3.11-bullseye

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]

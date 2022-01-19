FROM python:3.8.12 as dev

WORKDIR /app
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

FROM dev as prod
COPY ./app /app

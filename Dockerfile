FROM python:latest

COPY requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/app

COPY src /usr/src/app/src
COPY configs /usr/src/app/configs
COPY Makefile app.py logging.yaml setup.cfg /usr/src/app/


CMD ["make", "run-in-docker"]
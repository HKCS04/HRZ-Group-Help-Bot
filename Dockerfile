FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app/
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

CMD python3 -m bot

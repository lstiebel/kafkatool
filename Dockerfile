FROM python:3.7.2-slim-stretch

ENV KAFKA_SSL_CA_CERT=/ssl/ca.crt
ENV KAFKA_SSL_CLIENT_CERT=/ssl/client.crt
ENV KAFKA_SSL_CLIENT_KEY=/ssl/client.key

COPY kafkatool /app/

WORKDIR /app

RUN python3 setup.py install

ENTRYPOINT [ "kafkatool.py" ]

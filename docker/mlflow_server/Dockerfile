#FROM ubuntu 
FROM python:3.7-slim-buster
ARG PROXY_SERVER
RUN pip --proxy $PROXY_SERVER install mlflow pymysql boto3 cryptography

#FROM ubuntu 
FROM python:3.8-slim-buster
ARG PROXY_SERVER
RUN pip --proxy $PROXY_SERVER install mlflow==2.0.1 pymysql boto3 cryptography

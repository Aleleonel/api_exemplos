# syntax=docker/dockerfile:1
FROM python:3
COPY . /Api_exemplos
WORKDIR /Api_exemplos
COPY . .
CMD ["/Api_exemplos/api_gitteste.py"]
ENTRYPOINT "python3"
from alpine:latest

RUN apk add --no-cache python3 \
    && apk add --no-cache py3-pip

WORKDIR /app

COPY . /app

RUN pwd

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["logs.py"]

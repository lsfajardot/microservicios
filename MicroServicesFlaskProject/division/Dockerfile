FROM alpine:3.11.5

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

EXPOSE 4740

WORKDIR /app

COPY requirements.txt /app

RUN pip3 --no-cache-dir install -r requirements.txt

COPY division.py /app

CMD ["python3", "division.py"]
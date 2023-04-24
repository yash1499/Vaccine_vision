FROM python:3.5.10-alpine3.12

WORKDIR /usr/src/app

RUN apk update && \
    apk add --no-cache --virtual build-deps gcc python3-dev musl-dev libxslt-dev && \
    apk add postgresql-dev
COPY req.txt ./
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r req.txt

COPY . .
EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
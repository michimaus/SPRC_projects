FROM python:3.8

ENV PYTHONUNBUFFERED=1

ARG DB_PASSWORD
ARG DB_USERNAME
ARG DB_NAME
ARG DB_HOSTNAME
ARG DB_PORT
ARG REST_API_PORT

RUN mkdir -p /sprc_rest_api
RUN mkdir -p /sprc_rest_api/temp

COPY . /sprc_rest_api
WORKDIR /sprc_rest_api
EXPOSE $REST_API_PORT

RUN pip install pipenv

COPY Pipfile* /sprc_rest_api/temp/
RUN cd /sprc_rest_api/temp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install --no-cache-dir -r /sprc_rest_api/temp/requirements.txt
RUN cd /sprc_rest_api
RUN rm -rf /sprc_rest_api/temp/*

RUN chmod a+x start_api.sh

CMD ./start_api.sh

#!/bin/bash

# docker swarm init --advertise-addr 192.168.99.99
docker swarm init

# /////////////////////////////////////////////
export INFLUXDB_HOSTNAME=sprc_influxdb
 
export DOCKER_INFLUX_INIT_MODE=setup
export DOCKER_INFLUX_INIT_USERNAME=user
export DOCKER_INFLUX_INIT_PASSWORD=my_password
 
export DOCKER_INFLUX_INIT_ORG=org
export DOCKER_INFLUX_INIT_BUCKET=buck
export DOCKER_INFLUX_INIT_ADMIN_TOKEN=8BnoOF5XsJ839U7sDQRU40iW7LUg1vxkCsvEG5F5wANbsfRwxnNuSb_F9Mm8-O_MLXJH-rGUwY6jc7YKtd3vVg
 
 
export MQTT_SERVICE_HOSTNAME=sprc_mqtt_service
 
 
export GRAFANA_HOSTNAME=sprc_grafana
 
 
export INFLUXDB_PORT=8086
export MQTT_SERVICE_PORT=1883
export GRAFANA_CONNECTION_PORT=3000
export GRAFANA_EXPOSED_PORT=3000

# ///////////////////////////////////////////////

docker service create --replicas 1 --name sprc3 -p 5000:5000 registry:2.7

curl http://localhost:5000/v2/
echo " "
echo I_am_wasted...

docker-compose -f stack.yml up -d

docker-compose -f stack.yml ps

docker-compose -f stack.yml down --volumes

docker-compose -f stack.yml push
# docker-compose -f stack_networks.yml push

# docker stack deploy -c stack_networks.yml -c stack.yml sprc3
docker stack deploy -c stack.yml sprc3


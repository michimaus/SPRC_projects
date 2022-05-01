import json
import math
import random
from datetime import datetime, timedelta
import iso8601
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK!")
        client.subscribe("#")
    else:
        print("Connection error {}".format(rc))


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected with status code = {}".format(rc))


def on_message(client, userdata, message):
    topic = message.topic
    decode_message = str(message.payload.decode("utf-8"))
    print("Topic: " + topic)
    print("Message received: " + decode_message)


LOCAL_HOST = "127.0.0.1"

mqtt_client = mqtt.Client(client_id="Client" + str(random.randint(0, 100000)))

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.on_disconnect = on_disconnect

mqtt_client.connect(LOCAL_HOST, port=1883)
mqtt_client.loop_start()

locations = ['pr_001', 'ec_101', 'ec_04', 'an_03', 'an_03', 'cantina']
param_list = ['BAT', 'humid', 'temp', 'warns', 'errs', 'aqi', 'light', 'speed', 'acc', 'up_time']

dump_words = ['BAT', 'humid', 'temp', 'warns', 'errs', 'aqi', 'light', 'speed', 'acc',
              'up_time', 'ceva', 'altceva', 'OK', 'NE_OK', 'BIG_BLANA', 'ce_trebuie']

for index in range(10):
    dest = random.choice(locations)
    params = random.sample(param_list, random.randint(2, 6))

    to_payload = {}

    for elm in params:
        if random.randint(0, 100) >= 75:
            to_payload[elm] = random.choice(dump_words)
        else:
            to_payload[elm] = random.randint(0, 1000) / 10
            if random.randint(0, 100) >= 60:
                to_payload[elm] = int(math.floor(to_payload[elm]))

    publish_topic = "poli/" + dest

    if random.randint(0, 100) >= 75:
        publish_topic += "/mocked"

    if random.randint(0, 100) >= 40:
        # date_register = datetime.now() - timedelta(days=random.randint(0, 3), hours=random.randint(0, 24),
        #                                            minutes=random.randint(0, 60), seconds=random.randint(0, 60))

        date_register = datetime.now() - timedelta(hours=random.randint(0, 30), minutes=random.randint(0, 60),
                                                   seconds=random.randint(0, 60))

        to_payload['timestamp'] = date_register.astimezone().replace(microsecond=0).isoformat()

    mqtt_client.publish(publish_topic, json.dumps(to_payload))

mqtt_client.loop_stop()
mqtt_client.disconnect()

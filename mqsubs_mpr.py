import paho.mqtt.client as mqtt
import re
import pprint
import os
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("cluster/SOME01_000/data/#")


MQTT_Messages = {}
def on_message(client, userdata, msg):

    # printing the messages form the subscribed topic
    print(msg.topic, msg.payload)


client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.tls_set("./caMqttRoot.crt")  #path of the .crt file

client.username_pw_set(username="username", password="password")
print("Connecting...")
client.connect("something.domain.com", 8883)
client.loop_forever()




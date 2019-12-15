#! /bin/env python

import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("[+] Connection success")
    client.subscribe('#', qos = 1)
    client.subscribe('$SYS/#')

def on_message(client, userdata, msg):
    print('[+] Topic: %s - Message: %s' % (msg.topic, msg.payload))

client = mqtt.Client(client_id = "MqttClient")
client.on_connect = on_connect
client.on_message = on_message

client.connect('whale.hacking-lab.com', 9001, 60)
while True:
    time.sleep(1)
    print('[+] loop')
    client.loop()

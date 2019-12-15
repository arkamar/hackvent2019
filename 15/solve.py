#! /bin/env python

import time
import paho.mqtt.client as mqtt

clientid = '0123456789012345'

def on_connect(client, userdata, flags, rc):
    print("[+] Connection success")
    client.subscribe('#', qos = 1)
    print("[+] subscribed #")
    client.subscribe('$SYS/#')
    print("[+] subscribed $SYS/#")

def on_message(client, userdata, msg):
    print('[+] Topic: %s - Message: %s' % (msg.topic, msg.payload))

def on_error(client, error):
    print('[-] Error:', error)

client = mqtt.Client(client_id=clientid, clean_session=True, transport = 'websockets')
client.on_connect = on_connect
client.on_message = on_message
client.on_error = on_error

client.connect('whale.hacking-lab.com', 9001, 60)
client.loop_forever()

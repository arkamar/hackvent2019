#! /bin/env python

import sys
import paho.mqtt.client as mqtt

clientid = '999999999999999999999999999'

if len(sys.argv) == 2:
    clientid = sys.argv[1]

def on_connect(client, userdata, flags, rc):
    print("[+] Connection success")
    client.subscribe('#')
    print("[+] subscribed #")
    #client.subscribe('HV19/gifts/' + clientid) # + '/flag-tbd')
    #client.subscribe('/HV19/gifts/flag-tbd')
    #print("[+] subscribed #flag")
    #client.subscribe('$SYS/#')
    #print("[+] subscribed $SYS/#")

m = None
def on_message(client, userdata, msg):
    global m

    n = int(msg.payload)
    d = 0
    if m != None:
        d = n - m
    m = n
    print('[+] Topic: %s - Message: %s, %d' % (msg.topic, msg.payload, d))

def on_error(client, error):
    print('[-] Error:', error)

client = mqtt.Client(client_id=clientid, clean_session=True, transport = 'websockets')
client.on_connect = on_connect
client.on_message = on_message
client.on_error = on_error

client.connect('whale.hacking-lab.com', 9001, 60)
client.loop_forever()

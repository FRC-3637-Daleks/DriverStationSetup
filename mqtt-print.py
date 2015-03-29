#pip install paho-mqtt
#pip install git+https://github.com/mbr/asciitree.git

import paho.mqtt.client as mqtt
import sys
from collections import defaultdict
from time import sleep

def on_connect(client, userdata, flags, rc):
	client.subscribe("#")

def on_message(client, userdata, msg):
	print msg.topic+" : "+msg.payload

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("roboRIO-3637.local", 1180)

client.loop_start()

while True:
	sleep(0.05)

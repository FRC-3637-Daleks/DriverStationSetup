#pip install paho-mqtt
#pip install git+https://github.com/mbr/asciitree.git

import asciitree
import paho.mqtt.client as mqtt
import sys
from collections import defaultdict
from time import sleep

def tree(): return defaultdict(tree)

data = tree()

def on_connect(client, userdata, flags, rc):
	client.subscribe("#")

def on_message(client, userdata, msg):
	loc = data
	for key in msg.topic.split('/')[:-1]:
		loc = loc[key]
	loc[msg.topic.split('/')[-1]] = { str(msg.payload): {} }

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.36.37.2", 1180)

client.loop_start()

renderer = asciitree.LeftAligned();

while True:
	if data != {}:
		sys.stderr.write("\033c")
		print renderer(data)
	sleep(0.05)

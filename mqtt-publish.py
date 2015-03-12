#pip install paho-mqtt
#pip install git+https://github.com/mbr/asciitree.git

import paho.mqtt.publish as publish
import sys
from time import sleep

if len(sys.argv) < 4:
	sys.exit()

publish.single(sys.argv[2], sys.argv[3], hostname=sys.argv[1], port=1180, retain=True)


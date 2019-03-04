#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("iot.eclipse.org")
client.publish("topic/test", "Hello world!")
client.disconnect()

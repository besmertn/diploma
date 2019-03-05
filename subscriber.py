import paho.mqtt.client as mqtt


# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/test")


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def subscribe():
    client = mqtt.Client()
    client.connect('iot.eclipse.org')

    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()

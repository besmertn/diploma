import os

import paho.mqtt.client as mqtt
from flask import send_from_directory, render_template, current_app
from flask_login import login_required

from diploma.main import bp


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@bp.route('/subscribe')
def subscribe():
    current_app.task_queue.enqueue(subscribe)
    return render_template('index.html', title='Home')


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


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

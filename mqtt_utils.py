import os
import time
import json
import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "broker.hivemq.com")
PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC_SENSOR = os.getenv("MQTT_TOPIC_SENSOR", "smartgarden/sensor")
TOPIC_CONTROL = os.getenv("MQTT_TOPIC_CONTROL", "smartgarden/control")

client = mqtt.Client()

last_sensor_value = {
    "soil": 0,
    "temperature": 0
}

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC_SENSOR)

def on_message(client, userdata, msg):
    global last_sensor_value
    try:
        data = json.loads(msg.payload.decode())
        last_sensor_value = data
    except:
        pass

def connect_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_start()

def get_sensor_data():
    return last_sensor_value

def send_command(cmd):
    client.publish(TOPIC_CONTROL, json.dumps({"pump": cmd}))
    time.sleep(0.1)

import os
import paho.mqtt.client as mqtt

MQTT_BROKER = os.getenv("MQTT_BROKER", "tu-broker.hivemq.cloud")
MQTT_PORT = int(os.getenv("MQTT_PORT", "8883"))
MQTT_USER = os.getenv("MQTT_USER", "tu_usuario")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "tu_password")

TOPIC_STATUS = "smarthome/status"
TOPIC_CONTROL = "smarthome/control"


last_message = {"status": "OFF"}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPIC_STATUS)
    else:
        print("Error de conexión MQTT:", rc)

def on_message(client, userdata, msg):
    last_message["status"] = msg.payload.decode()

def connect_mqtt():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
    client.tls_insecure_set(False)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    return client

mqtt_client = None

def init_mqtt():
    global mqtt_client
    if mqtt_client is None:
        mqtt_client = connect_mqtt()

def get_status():
    init_mqtt()
    return last_message["status"]

def send_command(command):
    init_mqtt()
    mqtt_client.publish(TOPIC_CONTROL, command)

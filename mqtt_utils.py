# mqtt_utils.py
import json
import threading
import time
import os

USE_MQTT = True  # cambia a False si vas a usar solo el simulador
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TOPIC_PREFIX = "smarthome/demo/tu_usuario"  # cámbialo por algo único

# Si USE_MQTT True se importará paho y se levantará cliente
if USE_MQTT:
    import paho.mqtt.client as mqtt
    client = mqtt.Client()

    def start_mqtt(on_message_callback=None):
        def _on_connect(client, userdata, flags, rc):
            print("MQTT conectado, rc=", rc)
            # subscribir topics de interés
            client.subscribe(TOPIC_PREFIX + "/#")

        def _on_message(client, userdata, msg):
            topic = msg.topic
            payload = msg.payload.decode()
            # callback para que la UI lo use
            if on_message_callback:
                on_message_callback(topic, payload)

        client.on_connect = _on_connect
        client.on_message = _on_message
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.loop_start()
        except Exception as e:
            print("Error conectando MQTT:", e)

    def mqtt_publish(topic_suffix, payload):
        full = TOPIC_PREFIX + "/" + topic_suffix
        try:
            client.publish(full, payload)
            print("Publicado:", full, payload)
        except Exception as e:
            print("Error publicando:", e)
else:
    # Simulación por archivo estado.json
    STATE_FILE = "estado.json"
    def start_mqtt(on_message_callback=None):
        print("MQTT desactivado: modo simulador activo.")
    def mqtt_publish(topic_suffix, payload):
        # guarda comando en un archivo para revisión manual
        out = {"topic": topic_suffix, "payload": payload}
        with open("last_command.json","w") as f:
            json.dump(out,f)
        print("Simulado publish:", out)

# Utilidad para leer estado local (simulador)
def read_estado_file(path="estado.json"):
    if not os.path.exists(path):
        return {}
    try:
        with open(path,"r") as f:
            return json.load(f)
    except Exception as e:
        print("Error leyendo estado.json:", e)
        return {}

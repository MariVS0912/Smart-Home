import paho.mqtt.client as mqtt
import json
import time

def get_mqtt_message(broker, port, topic, client_id):
"""Función para obtener mensaje MQTT (lectura sensores)"""
message_received = {"received": False, "payload": None}

```
def on_message(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode())
        message_received["payload"] = payload
    except:
        message_received["payload"] = message.payload.decode()
    message_received["received"] = True

try:
    client = mqtt.Client(client_id=client_id)
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.subscribe(topic)
    client.loop_start()
    
    timeout = time.time() + 5
    while not message_received["received"] and time.time() < timeout:
        time.sleep(0.1)
    
    client.loop_stop()
    client.disconnect()
    return message_received["payload"]

except Exception as e:
    return {"error": str(e)}
```

def send_mqtt_command(broker, port, topic, client_id, command):
"""Función para enviar comando MQTT (actuadores)"""
try:
client = mqtt.Client(client_id=client_id)
client.connect(broker, port, 60)
client.loop_start()
payload = json.dumps(command)
client.publish(topic, payload)
client.loop_stop()
client.disconnect()
return True
except Exception as e:
return {"error": str(e)}

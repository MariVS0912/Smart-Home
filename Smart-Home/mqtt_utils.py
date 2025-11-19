import paho.mqtt.client as mqtt
import ssl
import streamlit as st

# Callback cuando el cliente se conecta al broker

def on_connect(client, userdata, flags, rc):
if rc == 0:
print("Conectado al broker MQTT exitosamente.")
else:
print(f"Error al conectar, código: {rc}")

# Callback cuando llega un mensaje

def on_message(client, userdata, msg):
print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

# Función principal para conectar MQTT

def connect_mqtt(broker="TU_BROKER", port=8883, username=None, password=None):
# Guardar el cliente en session_state para evitar reconexión múltiple
if "mqtt_client" not in st.session_state:
client = mqtt.Client()

```
    # Configurar TLS solo si no está configurado
    if not hasattr(client, "_ssl_context"):
        client.tls_set(cert_reqs=ssl.CERT_NONE)

    # Configurar usuario y contraseña si aplica
    if username and password:
        client.username_pw_set(username, password)

    # Asignar callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar y arrancar loop
    client.connect(broker, port)
    client.loop_start()

    st.session_state.mqtt_client = client
else:
    client = st.session_state.mqtt_client

return client
```

# Función para publicar mensajes

def publish(topic, payload):
client = st.session_state.get("mqtt_client")
if client:
client.publish(topic, payload)
else:
print("El cliente MQTT no está conectado.")

# Función para suscribirse a un topic

def subscribe(topic):
client = st.session_state.get("mqtt_client")
if client:
client.subscribe(topic)
else:
print("El cliente MQTT no está conectado.")


# -----------------------------
# CALLBACKS MQTT
# -----------------------------
def on_connect(client, userdata, flags, rc):
    print("Conectado con código:", rc)
    if rc == 0:
        client.subscribe(TOPIC_SENSORES)
    else:
        print("Error en conexión MQTT:", rc)


def on_message(client, userdata, msg):
    global sensor_data
    topic = msg.topic
    payload = msg.payload.decode()

    if "temperatura" in topic:
        sensor_data["temp"] = payload

    elif "humedad" in topic:
        sensor_data["humedad"] = payload

    elif "luz" in topic:
        sensor_data["luz"] = payload


# -----------------------------
# INICIAR MQTT
# -----------------------------
def connect_mqtt():
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    client.tls_set(cert_reqs=ssl.CERT_NONE)
    client.tls_insecure_set(True)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()


# -----------------------------
# ENVIAR MENSAJE
# -----------------------------
def publish_message(message):
    client.publish(TOPIC_CONTROL, message)


# -----------------------------
# OBTENER DATOS
# -----------------------------
def get_sensor_data():
    return sensor_data




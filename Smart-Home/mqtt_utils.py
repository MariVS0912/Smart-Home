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
    decoded = f"{msg.topic}: {msg.payload.decode()}"
    print("Mensaje recibido:", decoded)
    if "mqtt_messages" not in st.session_state:
        st.session_state.mqtt_messages = []
    st.session_state.mqtt_messages.append(decoded)

# Conectar al broker MQTT
def connect_mqtt(broker="TU_BROKER", port=8883, username=None, password=None):
    if "mqtt_client" not in st.session_state:
        client = mqtt.Client()
        if not hasattr(client, "_ssl_context"):
            client.tls_set(cert_reqs=ssl.CERT_NONE)
        if username and password:
            client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker, port)
        client.loop_start()
        st.session_state.mqtt_client = client
    else:
        client = st.session_state.mqtt_client
    return client

# Publicar mensaje
def publish(topic, payload):
    client = st.session_state.get("mqtt_client")
    if client:
        client.publish(topic, payload)
    else:
        print("El cliente MQTT no está conectado.")

# Suscribirse a un topic
def subscribe(topic):
    client = st.session_state.get("mqtt_client")
    if client:
        client.subscribe(topic)
    else:
        print("El cliente MQTT no está conectado.")

# Wrappers para

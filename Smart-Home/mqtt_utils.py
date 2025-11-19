import paho.mqtt.client as mqtt
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

# Conectar al broker MQTT (broker de prueba)
def connect_mqtt():
    broker = "test.mosquitto.org"
    port = 1883

    if "mqtt_client" not in st.session_state:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker, port)
        client.loop_start()
        st.session_state.mqtt_client = client
    else:
        client = st.session_state.mqtt_client
    return client

# Publicar mensaje
def publish_message(topic, message):
    client = st.session_state.get("mqtt_client")
    if client:
        client.publish(topic, message)
    else:
        print("El cliente MQTT no está conectado.")

# Suscribirse a un topic y obtener datos
def get_sensor_data(topic):
    client = st.session_state.get("mqtt_client")
    if client:
        client.subscribe(topic)
    if "mqtt_messages" not in st.session_state:
        st.session_state.mqtt_messages = []
    return st.session_state.mqtt_messages


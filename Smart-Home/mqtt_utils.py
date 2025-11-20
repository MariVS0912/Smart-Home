import paho.mqtt.client as mqtt
import streamlit as st

# -----------------------------
#  CALLBACKS MQTT
# -----------------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT conectado correctamente.")
    else:
        print(f"Error al conectar MQTT. Código: {rc}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    # Guardar sensores
    if topic.startswith("casa/sensores/"):
        if "sensores" not in st.session_state:
            st.session_state["sensores"] = {}
        st.session_state["sensores"][topic.split("/")[-1]] = payload

    # Guardar dispositivos
    else:
        if "dispositivos" not in st.session_state:
            st.session_state["dispositivos"] = {}
        st.session_state["dispositivos"][topic] = payload


# -----------------------------
#  CONEXIÓN MQTT
# -----------------------------
def connect_mqtt(broker="test.mosquitto.org", port=1883):
    # Si ya está conectado, no repetir
    if "mqtt_client" in st.session_state:
        return st.session_state["mqtt_client"]

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(broker, port)
        client.loop_start()
    except Exception as e:
        st.error(f"No se pudo conectar al broker MQTT: {e}")

    st.session_state["mqtt_client"] = client
    return client


# -----------------------------
#  PUBLICAR
# -----------------------------
def publish_message(topic, payload):
    client = st.session_state.get("mqtt_client")
    if client:
        client.publish(topic, payload)

        # Reflejar estado inmediatamente en la UI
        if "dispositivos" not in st.session_state:
            st.session_state["dispositivos"] = {}
        st.session_state["dispositivos"][topic] = payload


# -----------------------------
#  SUSCRIBIR
# -----------------------------
def subscribe(topic):
    client = st.session_state.get("mqtt_client")
    if client:
        client.subscribe(topic)


# -----------------------------
#  OBTENER DATOS
# -----------------------------
def get_sensor_data(sensor):
    return st.session_state.get("sensores", {}).get(sensor, "N/A")

def get_device_status(topic):
    return st.session_state.get("dispositivos", {}).get(topic, "OFF")


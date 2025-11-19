import paho.mqtt.client as mqtt

data = {
    "temperature": 0,
    "light": 0,
    "soil": 0,                # Si luego quieres agregar humedad real
    "sala": "off",
    "cocina": "off",
    "habitacion": "off",
    "ventana": 0
}

# -------------------------
# CALLBACK DE MENSAJES
# -------------------------

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    # ----- Sensores -----
    if topic == "casa/sensores/temperatura":
        data["temperature"] = float(payload)

    if topic == "casa/sensores/luminosidad":
        data["light"] = float(payload)

    if topic == "casa/sensores/humedad":
        data["soil"] = float(payload)

    # ----- Luces -----
    if topic == "casa/luces/sala":
        data["sala"] = payload

    if topic == "casa/luces/cocina":
        data["cocina"] = payload

    if topic == "casa/luces/habitacion":
        data["habitacion"] = payload

    # ----- Ventana (servo) -----
    if topic == "casa/ventanas":
        data["ventana"] = int(payload)

# -------------------------
# FUNCIÓN PARA STREAMLIT
# -------------------------

def get_sensor_data():
    return data

# -------------------------
# CONFIG MQTT
# -------------------------

client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

# Suscribirse a TODO lo del proyecto
client.subscribe("casa/sensores/#")
client.subscribe("casa/luces/#")
client.subscribe("casa/ventanas")

client.loop_start()


import streamlit as st
from mqtt_utils import connect_mqtt, publish, subscribe

# Configuración de la página

st.set_page_config(page_title="Smart-Home", page_icon="🏠")
st.title("Smart-Home – Controla tu casa desde el celular")

# Conectar al broker MQTT (se guarda en session_state)

client = connect_mqtt(broker="TU_BROKER", port=8883, username="TU_USUARIO", password="TU_PASSWORD")

# Sección: Control de luces

st.header("Luces")
if st.button("Encender luz sala"):
publish("casa/luz/sala", "ON")
if st.button("Apagar luz sala"):
publish("casa/luz/sala", "OFF")

if st.button("Encender luz habitación"):
publish("casa/luz/habitacion", "ON")
if st.button("Apagar luz habitación"):
publish("casa/luz/habitacion", "OFF")

# Sección: Control de

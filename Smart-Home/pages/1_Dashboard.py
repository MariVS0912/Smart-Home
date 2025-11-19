import streamlit as st
from mqtt_utils import get_sensor_data, connect_mqtt

# Conectar al broker si no lo está
connect_mqtt(broker="TU_BROKER", port=8883, username="TU_USUARIO", password="TU_PASSWORD")

st.header("Dashboard - Sensores")

# Suscribirse a sensores
temperatura = get_sensor_data("casa/sensor/temperatura")
humedad = get_sensor_data("casa/sensor/humedad")

st.write("Últimos mensajes de sensores:")
for msg in temperatura[-5:] + humedad[-5:]:
    st.write(msg)

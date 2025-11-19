import streamlit as st
from mqtt_utils import connect_mqtt, get_sensor_data

st.header("Dashboard - Sensores")

# Conectar al broker si no lo está
connect_mqtt()

# Suscribirse a sensores de ejemplo
temperatura = get_sensor_data("casa/sensor/temperatura")
humedad = get_sensor_data("casa/sensor/humedad")

st.write("Últimos mensajes de sensores:")
for msg in temperatura[-5:] + humedad[-5:]:
    st.write(msg)

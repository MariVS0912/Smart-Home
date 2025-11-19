import streamlit as st
import pandas as pd
from mqtt_utils import connect_mqtt, get_sensor_data

st.header("Dashboard - Sensores y Estado de Dispositivos")
connect_mqtt()

# Sensores
temperatura_msgs = get_sensor_data("casa/sensores/temperatura")[-10:]
luminosidad_msgs = get_sensor_data("casa/sensores/luminosidad")[-10:]

temperatura = [int(m.split(":")[-1]) for m in temperatura_msgs]
luminosidad = [int(m.split(":")[-1]) for m in luminosidad_msgs]

# Mostrar tarjetas de estado actual
col1, col2 = st.columns(2)
col1.metric("Temperatura (°C)", temperatura[-1] if temperatura else "-")
col2.metric("Luminosidad (lux)", luminosidad[-1] if luminosidad else "-")

# Gráficos
st.subheader("Historial de sensores")
st.line_chart(pd.DataFrame({"Temperatura": temperatura, "Luminosidad": luminosidad}))

# Últimos mensajes
st.subheader("Últimos mensajes de sensores")
for msg in temperatura_msgs + luminosidad_msgs:
    st.write(msg)


import streamlit as st
from mqtt_utils import get_sensor_data

st.title("📊 Dashboard de Sensores")

data = get_sensor_data()

col1, col2 = st.columns(2)

with col1:
    st.metric("Luminosidad (lx)", data["luminosidad"])

with col2:
    st.metric("Temperatura (°C)", data["temperatura"])

st.write("---")
st.write("Los datos se actualizan automáticamente desde Wokwi mediante MQTT.")

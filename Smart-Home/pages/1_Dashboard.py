import streamlit as st
from mqtt_utils import get_sensor_data

st.title("📊 Dashboard de Sensores")

st.write("Lectura en tiempo real desde el ESP32 por MQTT.")

# Obtener los datos del broker
data = get_sensor_data()

# Si no hay datos
if not data:
    st.warning("Aún no llegan datos del ESP32…")
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌡️ Temperatura (°C)", data.get("temp", "—"))

    with col2:
        st.metric("💧 Humedad (%)", data.get("humedad", "—"))

    with col3:
        st.metric("💡 Luz (lx)", data.get("luz", "—"))

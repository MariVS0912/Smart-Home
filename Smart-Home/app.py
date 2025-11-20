# app.py
import streamlit as st
from mqtt_utils import connect_mqtt

st.set_page_config(page_title="Smart-Home", page_icon="🏠")

# Conexión MQTT
connect_mqtt()  # Aquí se conecta al broker

st.title("Smart-Home – Controla tu casa desde el celular")

# Navegación
page = st.sidebar.selectbox("Ir a:", ["Home Status", "Controles"])

if page == "Home Status":
    import pages.home_status
elif page == "Controles":
    import pages.controls


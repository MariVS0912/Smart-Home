import streamlit as st
from mqtt_utils import connect_mqtt

# Configuración de la página
st.set_page_config(page_title="Smart-Home", page_icon="🏠")
st.title("Smart-Home – Controla tu casa desde el celular")

# Conectar al broker
client = connect_mqtt(broker="TU_BROKER", port=8883, username="TU_USUARIO", password="TU_PASSWORD")

st.write("Usa el menú lateral para navegar entre Dashboard y Controles.")

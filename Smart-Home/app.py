import streamlit as st
from mqtt_utils import connect_mqtt

st.set_page_config(page_title="Smart-Home", page_icon="🏠")
st.title("Smart-Home – Controla tu casa desde el celular")

# Conectar al broker
connect_mqtt()

st.write("Usa el menú lateral para navegar entre Dashboard y Controles.")

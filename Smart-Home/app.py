import streamlit as st
from mqtt_utils import connect_mqtt

st.set_page_config(page_title="SmartHome", page_icon="🌱")

st.title("SmartHome – Sistema Inteligente de Riego")
st.write("Controla tu jardín con sensores, voz y automatización.")

if "mqtt_started" not in st.session_state:
    connect_mqtt()
    st.session_state["mqtt_started"] = True

st.write("Selecciona una página en el menú de la izquierda.")

import streamlit as st
from mqtt_utils import connect_mqtt

st.set_page_config(page_title="Smart-Home", page_icon="🏠")

# Conectar MQTT solo una vez
connect_mqtt()

st.title("Smart-Home – Controla tu casa desde el celular")

st.sidebar.title("Navegación")
page = st.sidebar.selectbox("Ir a:", ["Home Status", "Controles"])

if page == "Home Status":
    import pages.1-HomeStatus
elif page == "Controles":
    import pages.2-Controls

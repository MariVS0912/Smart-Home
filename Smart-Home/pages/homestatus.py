import streamlit as st
import sys
import os

# --- FIX IMPORTS ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mqtt_utils import get_sensor_data, connect_mqtt


def app():
    st.title("Estado de la Casa")
    
    # Conectar MQTT apenas abre la página
    connect_mqtt()

    st.write("Temperatura:", get_sensor_data("temperatura"))

    # ---------------- INFO ----------------
    with st.expander('ℹ Información', expanded=False):
        st.markdown("""
        Esta página muestra los datos actuales de los sensores de tu Smart-Home.
        Presiona *Obtener Datos* para recibir la información más reciente del broker MQTT.
        """)

    # ---------------- BOTÓN PARA OBTENER DATOS ----------------
    if st.button('🔄 Obtener Datos'):
        st.success("Datos actualizados desde MQTT (si hay sensores publicando).")

    # ---------------- MOSTRAR DATOS ----------------
    sensores = st.session_state.get("sensores", {})

    if sensores:
        cols = st.columns(len(sensores))
        for i, (key, value) in enumerate(sensores.items()):
            with cols[i]:
                st.metric(label=key, value=value)

        with st.expander('Ver JSON completo'):
            st.json(sensores)
    else:
        st.info("Todavía no se han recibido datos desde los sensores.")

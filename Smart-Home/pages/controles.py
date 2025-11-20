import streamlit as st
import sys
import os

# --- IMPORTACIÓN ROBUSTA ---
try:
    from mqtt_utils import send_mqtt_command, connect_mqtt
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from mqtt_utils import send_mqtt_command, connect_mqtt

def app():
    st.title("🎛️ Centro de Control")
    
    # Aseguramos conexión
    connect_mqtt()

    st.write("Controla los actuadores de tu ESP32 simulado.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💡 Iluminación (LED)")
        if st.button("Encender LED", type="primary"):
            send_mqtt_command({"Act1": "ON"})
            st.toast("Enviado: LED ON")
            
        if st.button("Apagar LED"):
            send_mqtt_command({"Act1": "OFF"})
            st.toast("Enviado: LED OFF")

    with col2:
        st.subheader("🚪 Escotilla")
        if st.button("Abrir Escotilla"):
            send_mqtt_command({"Act1": "Open"})
            st.toast("Enviado: Abrir")
            
        if st.button("Cerrar Escotilla"):
            send_mqtt_command({"Act1": "Close"})
            st.toast("Enviado: Cerrar")

    st.markdown("---")
    
    with st.container():
        st.subheader("🦾 Control Servo Motor")
        # Slider para el servo
        servo_pos = st.slider("Ángulo del Servo", 0, 180, 90)
        
        if st.button("Mover Servo"):
            send_mqtt_command({"Analog": servo_pos})
            st.success(f"Posición enviada: {servo_pos}°")

app()

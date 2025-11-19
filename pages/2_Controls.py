import streamlit as st
from mqtt_utils import send_command, get_sensor_data

st.title("🎛️ Control de la Casa")

data = get_sensor_data()

st.subheader("💡 Luces")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Sala ON"):
        send_command("casa/luces/sala", "on")
    if st.button("Sala OFF"):
        send_command("casa/luces/sala", "off")

with col2:
    if st.button("Cocina ON"):
        send_command("casa/luces/cocina", "on")
    if st.button("Cocina OFF"):
        send_command("casa/luces/cocina", "off")

with col3:
    if st.button("Habitación ON"):
        send_command("casa/luces/habitacion", "on")
    if st.button("Habitación OFF"):
        send_command("casa/luces/habitacion", "off")

st.write("---")

st.subheader("🪟 Ventana automática (Servo)")
angle = st.slider("Ángulo", 0, 180, data["ventana"])
send_command("casa/ventanas", str(angle))

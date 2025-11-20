import streamlit as st
from mqtt_utils import send_mqtt_command

def app(broker, port, topic_actuators, client_id):
st.title("🕹️ Control de Dispositivos")

```
with st.expander("💡 Luces y Actuadores"):
    if st.button("Encender Luz"):
        send_mqtt_command(broker, int(port), topic_actuators, client_id, {"Act1": "ON"})
    if st.button("Apagar Luz"):
        send_mqtt_command(broker, int(port), topic_actuators, client_id, {"Act1": "OFF"})
    if st.button("Abrir Escotilla"):
        send_mqtt_command(broker, int(port), topic_actuators, client_id, {"Act1": "Open"})
    if st.button("Cerrar Escotilla"):
        send_mqtt_command(broker, int(port), topic_actuators, client_id, {"Act1": "Close"})

with st.expander("🎛️ Control Servo Manual"):
    value_servo = st.slider("Posición Servo", 0, 180, 90)
    if st.button("Enviar posición"):
        send_mqtt_command(broker, int(port), topic_actuators, client_id, {"Analog": value_servo})
```

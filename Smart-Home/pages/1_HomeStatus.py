import streamlit as st
from mqtt_utils import get_device_status, get_sensor_data

st.header("Estado de tu casa inteligente")

# Sensores
st.subheader("Sensores")
temperatura_msgs = get_sensor_data("casa/sensores/temperatura")[-1:]
luminosidad_msgs = get_sensor_data("casa/sensores/luminosidad")[-1:]

temperatura = int(temperatura_msgs[0].split(":")[-1]) if temperatura_msgs else "-"
luminosidad = int(luminosidad_msgs[0].split(":")[-1]) if luminosidad_msgs else "-"

col1, col2 = st.columns(2)
col1.metric("Temperatura (°C)", temperatura)
col2.metric("Luminosidad (lux)", luminosidad)

# Dispositivos
st.subheader("Dispositivos")
luces = {
    "Sala": get_device_status("casa/luces/sala"),
    "Habitación": get_device_status("casa/luces/habitacion"),
}
enchufes = {
    "Televisor": get_device_status("casa/enchufe/televisor")
}
ventanas = {
    "Principal": get_device_status("casa/ventanas")
}

for nombre, estado in luces.items():
    st.write(f"{nombre}: {'💡 Encendida' if estado=='on' else '🔌 Apagada'}")
for nombre, estado in enchufes.items():
    st.write(f"{nombre}: {'🔌 Encendido' if estado=='on' else '❌ Apagado'}")
for nombre, valor in ventanas.items():
    st.write(f"{nombre}: {valor}° abierto" if valor else "❌ Cerrada")

# Interactividad visual
st.subheader("Escenas rápidas")
escena = st.selectbox("Selecciona una escena:", ["Normal", "Modo Noche", "Modo Fiesta"])
if escena == "Modo Noche":
    st.info("🌙 Escena Noche: luces apagadas, ventanas cerradas")
elif escena == "Modo Fiesta":
    st.success("🎉 Escena Fiesta: luces encendidas y ambiente alegre")
else:
    st.write("Casa en modo Normal")

# Slider de ventana (solo visual)
valor_ventana = 0
try:
    valor_ventana = int(ventanas.get("Principal") or 0)
except:
    pass

ventana_slider = st.slider("Ángulo ventana principal", 0, 180, value=valor_ventana)
st.write(f"Ventana principal: {ventana_slider}° (visual)")

st.button("Actualizar estado")

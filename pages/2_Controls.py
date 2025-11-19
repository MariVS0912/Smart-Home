import streamlit as st
from mqtt_utils import send_command

st.title("🎛️ Controles del Sistema")

st.subheader("Encender/Apagar la bomba")

col1, col2 = st.columns(2)

with col1:
    if st.button("Encender"):
        send_command("ON")
        st.success("Bomba encendida")

with col2:
    if st.button("Apagar"):
        send_command("OFF")
        st.error("Bomba apagada")

st.write("---")

st.subheader("Control por texto")
cmd = st.text_input("Escribe 'encender' o 'apagar'")

if st.button("Enviar texto"):
    if "encender" in cmd.lower():
        send_command("ON")
        st.success("Bomba encendida por texto")
    elif "apagar" in cmd.lower():
        send_command("OFF")
        st.error("Bomba apagada por texto")
    else:
        st.warning("Comando no válido")

st.write("---")

st.subheader("Control por voz")
st.write("Haz clic para grabar:")

audio = st.audio_input("Habla aquí")

if audio:
    text = st.experimental_audio_to_text(audio)
    if text:
        st.write("Detectado:", text)
        if "encender" in text.lower():
            send_command("ON")
            st.success("Bomba encendida por voz")
        elif "apagar" in text.lower():
            send_command("OFF")
            st.error("Bomba apagada por voz")

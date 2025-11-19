import streamlit as st
from mqtt_utils import publish_message

st.title("🎛️ Controles del Sistema")
st.write("Controla el sistema enviando comandos MQTT.")

# --- Botones de Encender / Apagar ---
st.subheader("Encender / Apagar Bomba")

col1, col2 = st.columns(2)

with col1:
    if st.button("Encender"):
        publish_message("ON")
        st.success("Bomba encendida")

with col2:
    if st.button("Apagar"):
        publish_message("OFF")
        st.error("Bomba apagada")

st.write("---")

# --- Control por texto ---
st.subheader("Control por texto")

cmd = st.text_input("Escribe 'encender' o 'apagar':")

if st.button("Enviar texto"):
    text = cmd.lower()

    if "encender" in text:
        publish_message("ON")
        st.success("Bomba encendida por texto")
    elif "apagar" in text:
        publish_message("OFF")
        st.error("Bomba apagada por texto")
    else:
        st.warning("Comando no válido")

st.write("---")

# --- Control por voz ---
st.subheader("Control por voz (si tu navegador lo soporta)")

audio = st.audio_input("Habla aquí:")

if audio:
    st.write("Procesando audio…")
    text = st.experimental_audio_to_text(audio)

    if text:
        st.write("Detectado:", text)

        text_l = text.lower()

        if "encender" in text_l:
            publish_message("ON")
            st.success("Bomba encendida por voz")
        elif "apagar" in text_l:
            publish_message("OFF")
            st.error("Bomba apagada por voz")
        else:
            st.warning("No se detectó un comando válido.")


import streamlit as st
from mqtt_utils import publish_message, get_device_status

st.header("Controles de la Casa")

modo = st.radio("Modo de control:", ["Botones", "Texto", "Voz"])

dispositivos = ["casa/luz/sala", "casa/luz/habitacion", "casa/enchufe/televisor", "casa/enchufe/lampara"]

def ejecutar_comando(comando):
    comando = comando.lower()
    # Buscamos palabras clave para encender/apagar
    for dev in dispositivos:
        nombre = dev.split("/")[-1]
        if nombre in comando:
            if "encender" in comando:
                publish_message(dev, "ON")
                st.success(f"{nombre} encendida")
            elif "apagar" in comando:
                publish_message(dev, "OFF")
                st.warning(f"{nombre} apagada")

if modo == "Botones":
    for dev in dispositivos:
        estado = get_device_status(dev)
        col1, col2 = st.columns([2,1])
        with col1:
            st.write(f"{dev.split('/')[-1].capitalize()}: {estado}")
        with col2:
            if st.button("ON", key=f"{dev}_on", help="Encender"):
                publish_message(dev, "ON")
            if st.button("OFF", key=f"{dev}_off", help="Apagar"):
                publish_message(dev, "OFF")

elif modo == "Texto":
    comando_texto = st.text_input("Escribe tu comando (ej: 'encender sala', 'apagar televisor'):")
    if st.button("Enviar comando"):
        ejecutar_comando(comando_texto)

elif modo == "Voz":
    st.write("🔊 Pulsa el botón y di tu comando (ej: 'encender sala', 'apagar televisor')")
    audio_bytes = st.file_uploader("Sube tu grabación de voz (wav)", type=["wav"])
    if audio_bytes is not None:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.AudioFile(audio_bytes) as source:
            audio_data = r.record(source)
            try:
                comando_voz = r.recognize_google(audio_data, language="es-ES")
                st.write(f"Comando detectado: {comando_voz}")
                ejecutar_comando(comando_voz)
            except sr.UnknownValueError:
                st.error("No se pudo entender la voz")
            except sr.RequestError as e:
                st.error(f"Error del servicio de reconocimiento: {e}")


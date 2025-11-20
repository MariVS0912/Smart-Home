import streamlit as st

st.set_page_config(page_title="Smart-Home", page_icon="🏠", layout="centered")

st.title("Smart Home Dashboard")

st.write("Bienvenido. Usa el menú de la izquierda para navegar.")

# Variables de estado
if 'sensor_data' not in st.session_state:
    st.session_state.sensor_data = None

# Sidebar
with st.sidebar:
    st.subheader('⚙️ Configuración de Conexión')
    broker = st.text_input('Broker MQTT', value='broker.mqttdashboard.com')
    port = st.number_input('Puerto', value=1883, min_value=1, max_value=65535)
    topic_sensors = st.text_input('Tópico Sensores', value='Sensor/THP2')
    topic_actuators = st.text_input('Tópico Actuadores', value='Invernadero_Daniel')
    client_id = st.text_input('ID del Cliente', value='streamlit_client')




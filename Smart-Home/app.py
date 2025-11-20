import streamlit as st
from pages.HomeStatus import app as home_app
from pages.Controls import app as control_app


# ==================== Configuración de la página ====================

st.set_page_config(page_title="Smart-Home", page_icon="🏠", layout="centered")

# Variables de estado para MQTT

if 'sensor_data' not in st.session_state:
  st.session_state.sensor_data = None

# ==================== Sidebar ====================

with st.sidebar:
  st.subheader('⚙️ Configuración de Conexión')
  broker = st.text_input('Broker MQTT', value='broker.mqttdashboard.com')
  port = st.number_input('Puerto', value=1883, min_value=1, max_value=65535)
  topic_sensors = st.text_input('Tópico Sensores', value='Sensor/THP2')
  topic_actuators = st.text_input('Tópico Actuadores', value='Invernadero_Daniel')
  client_id = st.text_input('ID del Cliente', value='streamlit_client')

# ==================== Navegación entre páginas ====================

page = st.sidebar.selectbox("Ir a:", ["HomeStatus", "Controls"])

if page == "HomeStatus":
  home_app(broker, port, topic_sensors, client_id)
elif page == "Controls":
  control_app(broker, port, topic_actuators, client_id)

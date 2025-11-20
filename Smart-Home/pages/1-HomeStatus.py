import streamlit as st
from mqtt_utils import get_mqtt_message

def app(broker, port, topic_sensors, client_id):
st.title("🏡 Estado de la Casa Inteligente")

```
with st.expander('ℹ️ Información', expanded=False):
    st.markdown("""
    Esta página muestra los datos actuales de los sensores de tu Smart-Home.
    Presiona **Obtener Datos** para recibir la información más reciente del broker MQTT.
    """)

if st.button('🔄 Obtener Datos'):
    with st.spinner('Conectando al broker y esperando datos...'):
        sensor_data = get_mqtt_message(broker, int(port), topic_sensors, client_id)
        st.session_state.sensor_data = sensor_data

if 'sensor_data' in st.session_state and st.session_state.sensor_data:
    data = st.session_state.sensor_data
    if isinstance(data, dict) and 'error' in data:
        st.error(f"❌ Error de conexión: {data['error']}")
    else:
        st.success('✅ Datos recibidos correctamente')
        if isinstance(data, dict):
            cols = st.columns(len(data))
            for i, (key, value) in enumerate(data.items()):
                with cols[i]:
                    st.metric(label=key, value=value)
            with st.expander('Ver JSON completo'):
                st.json(data)
        else:
            st.code(data)
```

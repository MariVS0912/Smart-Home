import streamlit as st
import sys
import os

# --- BLOQUE DE IMPORTACIÓN ROBUSTO ---
# Este bloque maneja la dependencia de mqtt_utils.py, que está en el directorio padre.
try:
    # Intento 1: Importación directa (funciona si la ruta ya está configurada)
    from mqtt_utils import get_sensor_data, connect_mqtt
except ImportError as e:
    # Intento 2: Solución de ruta manual para entornos como Streamlit Cloud/Wokwi
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    
    # Solo añadir la ruta si no existe
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)
    
    try:
        # Reintento de importación
        from mqtt_utils import get_sensor_data, connect_mqtt
    except ImportError as final_error:
        # Si la importación falla incluso con la manipulación de ruta, 
        # genera funciones mock para que la aplicación no se caiga.
        st.error(f"FATAL: No se pudo encontrar mqtt_utils.py. Asegúrate de que esté en la raíz del proyecto. Error original: {final_error}")
        
        # Funciones de Relleno para que el código Streamlit continúe
        def connect_mqtt(): 
            st.warning("Conexión MQTT simulada.")
        def get_sensor_data(topic): 
            # Si el módulo falla, devuelve un valor predeterminado
            return "ERROR: Módulo no encontrado"
            
# --- FIN DEL BLOQUE DE IMPORTACIÓN ---


def app():
    # Inicializar el estado de sesión si no existe
    if "sensores" not in st.session_state:
        st.session_state["sensores"] = {}

    st.title("Estado de la Casa")
    
    # Conectar MQTT apenas abre la página
    connect_mqtt()

    # Mostrar la temperatura inicial (o el último valor conocido)
    current_temp = st.session_state.get("sensores", {}).get("temperatura", "Cargando...")
    st.write(f"Temperatura: **{current_temp}**")

    # ---------------- INFO ----------------
    with st.expander('ℹ Información', expanded=False):
        st.markdown("""
        Esta página muestra los datos actuales de los sensores de tu Smart-Home.
        Presiona *Obtener Datos* para reintentar la conexión y lectura desde el broker MQTT.
        """)

    # ---------------- BOTÓN PARA OBTENER DATOS ----------------
    # Al presionar el botón, se fuerza una re-ejecución del script (un refresh)
    if st.button('🔄 Obtener Datos'):
        # En una aplicación real, esta re-ejecución debería desencadenar una nueva lectura 
        # en connect_mqtt o actualizar st.session_state a través de una función asíncrona.
        st.session_state["sensores"]["temperatura"] = get_sensor_data("temperatura")
        st.success("Datos actualizados desde MQTT (si hay sensores publicando).")

    # ---------------- MOSTRAR DATOS ----------------
    sensores = st.session_state.get("sensores", {})

    if sensores:
        # Muestra hasta 4 métricas en columnas para un buen diseño
        display_keys = list(sensores.keys())[:4]
        cols = st.columns(len(display_keys))

        for i, key in enumerate(display_keys):
            value = sensores[key]
            with cols[i]:
                # st.metric requiere un número o string para el valor
                st.metric(label=key.capitalize(), value=value)

        with st.expander('Ver JSON completo'):
            st.json(sensores)
    else:
        st.info("Todavía no se han recibido datos desde los sensores.")

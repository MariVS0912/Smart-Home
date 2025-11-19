def connect_mqtt(broker="TU_BROKER", port=8883, username=None, password=None):
    # Inicializar mqtt_client si no existe
    if "mqtt_client" not in st.session_state:
        st.session_state.mqtt_client = None

    if st.session_state.mqtt_client is None:
        client = mqtt.Client()
        client.tls_set(cert_reqs=ssl.CERT_NONE)

        if username and password:
            client.username_pw_set(username, password)

        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(broker, port)
        client.loop_start()

        st.session_state.mqtt_client = client

    return st.session_state.mqtt_client

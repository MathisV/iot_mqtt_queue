# mqtt_config.py
import paho.mqtt.client as mqtt
import uuid

# Configuration du broker MQTT
BROKER = 'ifbb7e86.ala.eu-central-1.emqxsl.com'
PORT = 8883
USERNAME = '<CHANGE_ME>'
PASSWORD = '<CHANGE_ME>'
TLS = True  # Utilisation de TLS/SSL

# Fonction de connexion pour les clients MQTT
def connect_mqtt(client_id):
    client = mqtt.Client(client_id)
    client.username_pw_set(USERNAME, PASSWORD)
    if TLS:
        client.tls_set()  # Utilisation de TLS/SSL
    client.connect(BROKER, PORT, 60)
    return client

import sys
import paho.mqtt.client as mqtt
import json
import uuid
from mqtt_config import connect_mqtt  # Import de la fonction de connexion
from mongo_config import connect_mongo  # Import de la fonction de connexion MongoDB

# Fonction pour envoyer une demande et s'abonner au topic de réponse correspondant
def request_client(topic):
    def on_connect(client, userdata, flags, rc):
        print(f"Connecté avec le code {rc}")
        # S'abonner aux topics après la connexion
        client.subscribe(topic)
        print(f"Abonné au topic {topic}")

    def on_message(client, userdata, msg):
        print(f"Message reçu sur {msg.topic}: {msg.payload.decode()}")
        # Traite la réponse
        message = json.loads(msg.payload.decode())
        # Set the message as validated
        messages_collection.update_one(
            {"request_id": message['uid']},
            {"$set": {"validated": True}}
        )

    # Connexion au broker MQTT
    client_id = 'consumers-' + str(uuid.uuid4())
    client = connect_mqtt(client_id)

    # Configure les callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()  # Maintient le client en fonctionnement


# Connexion à la base de données MongoDB
messages_collection = connect_mongo()

# Pour exécuter le client
if __name__ == '__main__':
    
    # list le paramètre de la commande de lancement
    if len(sys.argv) == 2:
        topic = str(sys.argv[1])
    else:
        print("Usage: python consumer.py topic")
        sys.exit(1)
    request_client(topic)

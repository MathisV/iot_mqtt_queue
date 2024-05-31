import threading
import time
import paho.mqtt.client as mqtt
import json
import uuid
import random
from bson.json_util import dumps
from mqtt_config import connect_mqtt  # Import de la fonction de connexion
from mongo_config import connect_mongo  # Import de la fonction de connexion MongoDB
import sys


def make_request(client, topic):
    # Publie une demande sur le topic commun
    temp = random.randint(-5, 30)
    request = {
        'uid': str(uuid.uuid4()),
        'temp': temp,
    }
    print(f"Envoie de la température {temp} publiée sur {topic}")

    # Publie la demande sur le topic si pas de message en attente
    if messages_collection.count_documents({"validated": False, "topic": topic}) == 0:
        client.publish(topic, json.dumps(request))
    queue_request = {
        'request_id': request['uid'],
        'topic': topic,
        'data': request,
        'timestamp': time.time(),
        'validated': False
    }
    messages_collection.insert_one(queue_request)

# Fonction du client de réponse
def loop_publisher(topic):
    def on_connect(client, userdata, flags, rc):
        print(f"Connecté avec le code {rc}")

    def check_queues():
        while True:
            # Vérifie les messages non validés dans la base de données
            messages = messages_collection.find({"validated": False, "topic": topic}).sort("timestamp", 1).limit(1)
            for message in messages:
                message.pop('_id', None)
                # Publie les messages sur le topic approprié
                client.publish(message['topic'], dumps(message["data"], indent = 2))
                print(f"[RESEND] Message {message['request_id']} publié de la queue sur {message['topic']}")
                # Clean validated messages
                messages_collection.delete_many({"validated": True, "topic": topic})

            time.sleep(5)

    # Connexion au broker MQTT
    client_id = 'publisher-' + str(uuid.uuid4())
    client = connect_mqtt(client_id)

    # Configure les callbacks
    client.on_connect = on_connect


    # Démarre un thread pour vérifier les messages en queue
    queue_thread = threading.Thread(target=check_queues)
    queue_thread.start()

    # loop pour publier des messages
    while True:
        make_request(client, topic)
        time.sleep(10)

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

    loop_publisher(topic)

# TP MQTT Queue

## Installation des dependances

Executer la commande

```bash
pip install -r requirements.txt
```

## Protocoles utilisés

- Pour la partie communication, nous avons utilisé le protocole **MQTT** avec le logiciel **MQTT Explorer** pour la visualisation des messages échangés.
- Pour la partie stockage, nous avons utilisé la base de données **MongoDB**.

## Fonctionnement de l'application

L'application utilise le protocole MQTT pour la communication entre un publisher et un consommateur.

1. Le fichier `mqtt_config.py` contient les informations de configuration pour la connexion au broker MQTT, telles que l'adresse IP, le port et les identifiants d'authentification.

2. Le fichier `mongo_config.py` contient les informations de configuration pour la connexion à la base de données MongoDB, telles que l'adresse IP, le port et les identifiants d'authentification.

3. Le fichier `publisher.py` est responsable de la publication des messages MQTT. Il se connecte au broker MQTT en utilisant les informations de configuration du fichier `mqtt_config.py` et publie les messages dans une file d'attente spécifique.

4. Le fichier `consumer.py` est responsable de la consommation des messages MQTT. Il se connecte au broker MQTT en utilisant les informations de configuration du fichier `mqtt_config.py` et consomme les messages de la file d'attente spécifique. Les messages consommés sont ensuite enregistrés dans la base de données MongoDB en utilisant les informations de configuration du fichier `mongo_config.py`.

L'application permet donc de publier des messages MQTT dans une file d'attente et de les consommer pour les enregistrer dans une base de données MongoDB. Cette architecture permet une communication asynchrone et une gestion efficace des messages.

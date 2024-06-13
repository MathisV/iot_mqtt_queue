# TP MQTT Queue

## Usages

### Prérequis

- Python 3.6 ou supérieur
- Un broker MQTT (par exemple, Mosquitto, EMQX)
- Une base MongoDB

### Initialisation

Changement des variables d'environnement dans les fichiers `mqtt_config.py` et `mongo_config.py` pour correspondre à votre configuration.

```python
# mqtt_config.py
BROKER = "localhost"
PORT = 1883
USERNAME = ""
PASSWORD = ""
```

```python
# mongo_config.py
MONGO_URI = "localhost"
DATABASE_NAME = ""
```

Création d'un environnement virtuel

```bash
python3 -m venv <nom_de_l_environnement>
source <nom_de_l_environnement>/bin/activate
```

Executer la commande

```bash
pip install -r requirements.txt
```

### Execution du publisher

```bash
python publisher.py
```

### Execution du consumer

```bash
python consumer.py
```

## Fonctionnement

### Protocoles utilisés

- Pour la partie communication, nous avons utilisé le protocole **MQTT** avec le logiciel **MQTT Explorer** pour la visualisation des messages échangés.
- Pour la partie stockage, nous avons utilisé la base de données **MongoDB**.

### Fonctionnement de l'application

L'application utilise le protocole MQTT pour la communication entre un publisher et un consommateur.

1. Le fichier `mqtt_config.py` contient les informations de configuration pour la connexion au broker MQTT, telles que l'adresse IP, le port et les identifiants d'authentification.

2. Le fichier `mongo_config.py` contient les informations de configuration pour la connexion à la base de données MongoDB, telles que l'adresse IP, le port et les identifiants d'authentification.

3. Le fichier `publisher.py` est responsable de la publication des messages MQTT. Il se connecte au broker MQTT en utilisant les informations de configuration du fichier `mqtt_config.py` et publie les messages dans une file d'attente spécifique.

4. Le fichier `consumer.py` est responsable de la consommation des messages MQTT. Il se connecte au broker MQTT en utilisant les informations de configuration du fichier `mqtt_config.py` et consomme les messages de la file d'attente spécifique. Les messages consommés sont ensuite enregistrés dans la base de données MongoDB en utilisant les informations de configuration du fichier `mongo_config.py`.

L'application permet donc de publier des messages MQTT dans une file d'attente et de les consommer pour les enregistrer dans une base de données MongoDB. Cette architecture permet une communication asynchrone et une gestion efficace des messages.

![Image](https://cdn.discordapp.com/attachments/900788486381129798/1246144307539476490/image.png?ex=666c7553&is=666b23d3&hm=3018073cb55a278f8942db5eaf2ae2a622468f1d32b0453486dafaf3c02e8a66&)

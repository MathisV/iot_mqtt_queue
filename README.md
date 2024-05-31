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
python publisher.py <topic>
```

Le publisher va publier des températures aléatoires dans le topic spécifié.

### Execution du consumer

```bash
python consumer.py <topic>
```

Le consumer va consommer les messages du topic spécifié.

## Fonctionnement

- Pour la partie communication, nous avons utilisé le protocole **MQTT** avec le broker **EMQX**.
- Pour la partie stockage, nous avons utilisé la base de données **MongoDB**.

Il se connecte au broker MQTT en utilisant les informations de configuration du fichier `mqtt_config.py` et à la base de données avec `mongo_config.py`.

L'application permet donc de publier des messages MQTT dans une file d'attente et de les consommer en respectant une fille d'attente. Cette architecture permet une communication asynchrone et une gestion efficace des messages.

1. Le fichier `publisher.py` est responsable de la publication des messages MQTT. Il publie les messages via le protocole MQTT et en parallèle stocke dans une file d'attente spécifique les messages pour renvoyer le premier message de la fille s'il n'a pas encore été consommé. Il nettoie les messages validés dans la base de données MongoDB.
2. Le fichier `consumer.py` est responsable de la consommation des messages MQTT. Il consomme les messages publiés dans le topic. Les messages consommés sont ensuite tagé comme validé dans la base de données MongoDB.

![Image](https://i.ibb.co/RNrf5By/schema.png)

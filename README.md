
![Logo](https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png)


# Gestionnaire de tournois d'échecs

Le script a pour but de gérer des tournois d'échecs

## Installation & Execution

Fonctionnel avec Python 3.10.4

Pour préparer l'environnement virtuel, vous pouvez utiliser ces commandes :
```bash
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
```

Pour lancer le script, il suffit de taper la commmande suivante
```bash
python main.py
```

## Génération d'un rapport Flake8

Pour générer un rapport Flake8 la commande suivante suffit:

```bash
flake8 --format=html --htmldir=flake8-rapport
```
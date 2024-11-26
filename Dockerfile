# Utiliser l'image officielle Python comme base
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande à exécuter au démarrage du conteneur
CMD ["python", "app.py"]

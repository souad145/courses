#!/usr/bin/env bash
# exit on first error
set -o errexit

# Mise à jour du pip (recommandé)
pip install --upgrade pip

# Installation des dépendances
pip install -r requirements.txt

# Collecte des fichiers statiques (CSS, JS, images)
python manage.py collectstatic --no-input --clear

# Application des migrations de la base de données
python manage.py migrate --no-input
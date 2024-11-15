# Rentcar - Analyse des Prix de Voitures et Rentabilité

**Rentcar** est une application Python utilisant Streamlit permettant d'extraire et d'analyser les prix d'achat et de location des voitures depuis différents sites web, notamment **lacentrale.com** et **getaround.com**. L'application permet également d'effectuer une analyse de rentabilité basée sur ces données.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rentcar-analysis.streamlit.app/)

### Comment exécuter l'application sur votre machine

1. Installez les dépendances

   ```bash
   $ pip install -r requirements.txt

    Lancez l'application

    $ streamlit run src/main.py

Table des matières

    Fonctionnalités
    Prérequis
    Installation
    Lancer l'application
    Structure du projet
    Utilisation
    Contribuer
    Licence
    Contact

Fonctionnalités

    Extraction des prix d'achat des véhicules sur le site lacentrale.com.
    Extraction des prix de location des véhicules sur le site getaround.com.
    Analyse de rentabilité en comparant les prix d'achat et de location pour évaluer la viabilité d'un investissement.
    Exportation des données sous forme de fichiers Excel (.xlsx) pour une analyse détaillée.
    Interface interactive avec Streamlit pour une navigation simple et rapide des fonctionnalités.

Prérequis

Avant de pouvoir utiliser l'application, vous devez vous assurer que votre environnement de développement est prêt avec les outils et bibliothèques suivants :

    Python 3.x
    pip (gestionnaire de packages Python)

Liste des principales dépendances :

    streamlit - pour l'interface utilisateur.
    selenium - pour l'extraction des données des sites web.
    pandas - pour la manipulation des données.
    openpyxl - pour la gestion des fichiers Excel.
    requests - pour les requêtes HTTP et les interactions avec les API.

Installation

    Clonez le dépôt sur votre machine locale :

git clone https://github.com/HSrbyte/Rent_car_analysis.git
cd Rent_car_analysis

Créez un environnement virtuel (optionnel, mais recommandé) :

Windows :

python -m venv venv
.\venv\Scripts\activate

macOS/Linux :

python3 -m venv venv
source venv/bin/activate

Installez les dépendances du projet :

    pip install -r requirements.txt

Lancer l'application

Une fois l'environnement configuré et les dépendances installées, vous pouvez lancer l'application Streamlit.

    Assurez-vous que vous êtes dans le répertoire du projet, puis exécutez la commande suivante :

    streamlit run src/main.py

    Ouvrez votre navigateur et allez à l'adresse indiquée dans la ligne de commande (généralement http://localhost:8501) pour accéder à l'application.

Structure du projet

Voici la structure du projet pour une meilleure organisation :

Rentcar/
├── src/                # Code source
│   └── main.py         # Script principal Streamlit
├── requirements.txt    # Liste des dépendances
├── README.md           # Documentation
├── data/               # Dossier des fichiers de données d'entrée
│   └── cars_ML.xlsx    # Base de données des voitures, prix d'achat et de location
├── .gitignore          # Fichiers à ignorer par Git
└── LICENSE             # Licence du projet

Utilisation

    Extraction des données :

    L'application extrait les données relatives aux voitures depuis lacentrale.com (prix d'achat) et getaround.com (prix de location). Ces données sont ensuite stockées dans des fichiers Excel (.xlsx).

    Analyse de rentabilité :

    Vous pouvez comparer les prix d'achat et de location pour évaluer la rentabilité de chaque véhicule. L'application présente des graphiques et des tableaux permettant de visualiser rapidement les informations pertinentes.

    Interface Streamlit :

    L'interface est simple à utiliser et permet de naviguer facilement entre les différentes fonctionnalités. Vous pouvez charger les fichiers Excel et voir les résultats des analyses en temps réel.

Contribuer

Vous souhaitez contribuer au projet ? Voici comment procéder :

    Forkez ce dépôt.
    Créez une nouvelle branche (git checkout -b feature/mon-nouvelle-fonctionnalité).
    Faites vos modifications et assurez-vous que les tests passent (si applicable).
    Commitez vos modifications (git commit -am 'Ajout d’une nouvelle fonctionnalité').
    Poussez sur la branche (git push origin feature/mon-nouvelle-fonctionnalité).
    Ouvrez une Pull Request pour discuter des modifications avec l’équipe.

Licence

Ce projet est sous licence MIT.
Contact

Pour toute question, vous pouvez me contacter à l’adresse suivante :
Email : hsrbyte@gmail.com
GitHub : https://github.com/HSrbyte

Je vous encourage à tester l'application, à explorer ses fonctionnalités, et à contribuer si vous souhaitez améliorer l'outil !
Note supplémentaire

    Assurez-vous que le scraping fonctionne correctement sur lacentrale.com et getaround.com. Ces sites peuvent changer leurs structures, ce qui pourrait nécessiter des ajustements dans le code pour continuer à extraire les données.
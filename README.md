# 📊 E-Commerce Dashboard

> Dashboard interactif de pilotage business construit avec Python et Streamlit.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Plotly](https://img.shields.io/badge/Plotly-6.x-green)

## 🎯 Problème résolu

Les dirigeants de PME e-commerce passent des heures chaque semaine à compiler manuellement leurs données depuis Excel, leur CRM ou leur logiciel de vente pour avoir une vision claire de leur activité. Ce dashboard centralise tout automatiquement et permet de prendre des décisions en quelques secondes.

## 🚀 Demo

👉 [Lien vers la demo en ligne](https://dashboard-ecommerce-aboedmprsxqeuc7x35npps.streamlit.app/)

<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/748c9768-d718-4a39-a18b-f0240276f830" />
<img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/f6fd8695-b628-4749-9d2c-59f9203e8136" />
<img width="1919" height="867" alt="image" src="https://github.com/user-attachments/assets/0cf4217b-f14a-4869-91a4-ec39f74f3a46" />



## 📈 Fonctionnalités

### Vue générale
- CA total, nombre de commandes, panier moyen, nombre de clients uniques
- Evolution mensuelle du chiffre d'affaires
- Evolution mensuelle du nombre de commandes
- Panier moyen par mois
- Revenu par jour de la semaine
- Heatmap des commandes par jour et heure

### Analyse Clients
- Taux de rétention : nouveaux vs clients récurrents
- Top 10 clients par chiffre d'affaires

### Produits & Pays
- Top 10 produits par revenu
- Carte du monde interactive par revenu
- Top 10 pays par chiffre d'affaires

### Tendances
- Scatter plot quantité vs prix unitaire

## 🛠️ Stack technique

| Outil | Usage |
|---|---|
| Python | Langage principal |
| Pandas | Nettoyage et transformation des données |
| Plotly | Graphiques interactifs |
| Streamlit | Interface web |

## 📁 Structure du projet
```
dashboard-ecommerce/
├── data/
│   └── data.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── metrics.py
│   └── charts.py
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation et lancement
```bash
# Cloner le repo
git clone https://github.com/ton-username/dashboard-ecommerce.git
cd dashboard-ecommerce

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

## 📊 Dataset

UK E-Commerce — transactions réelles 2010-2011 d'un retailer britannique.
Source : [Kaggle - E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

- 500 000+ transactions brutes
- 4 338 clients uniques après nettoyage
- 18 532 commandes
- CA total : £8.9M

## 👤 Auteur

**Ton Nom** — Étudiant ingénieur Data/IA
- LinkedIn : [ton profil](#)
- GitHub : [ton profil](#)

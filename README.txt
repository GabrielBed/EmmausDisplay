Emmaüs - Interface de Dons (Affichage en Temps Réel)

Objectif

Ce projet permet d'afficher en temps réel :
- La somme récoltée en euros
- Le poids de vêtements sauvés (1€ = 1.5 kg)
- Le nombre de nuits d’hébergement offertes
- Le nombre de repas offerts

Chaque tranche de 20€ correspond à 1 nuit + 1 repas.

---

Structure du projet

emmaus_interface/
├── static/
│   ├── fond.png         ← Image de fond
│   ├── logo.png         ← Logo Emmaüs
├── ecran.html           ← Interface d’affichage sur écran
├── admin.html           ← Interface de saisie (formulaire)
├── data.json            ← Données stockées localement
├── server.py            ← Serveur local Flask
└── README.txt           ← Ce fichier d’aide

---

Prérequis

- Python 3.7 ou supérieur
- Flask (à installer si besoin avec `pip install flask dans le terminal du dossier`)

---

Lancement

1. Ouvrir un terminal ou PowerShell dans le dossier du projet
2. Lancer le serveur :
   python server.py

Ouvrir les deux interfaces :

- Formulaire d’administration :
  http://127.0.0.1:5000/

- Interface d’affichage :
  http://127.0.0.1:5000/display

---

Fonctionnement

- `admin.html` permet de saisir une somme récoltée
- Cette somme met à jour `data.json`
- L'écran se met à jour automatiquement grâce à un signal envoyé via `BroadcastChannel`

---

Détails des calculs

- 💶 Somme : affichée directement
- 🧥 Poids : somme x 1.5 kg
- 🛏️ Nuits : 1 nuit par tranche de 20 €
- 🍽️ Repas : 1 repas par tranche de 20 €

---

Problèmes fréquents

Python non reconnu → ajouter au PATH ou réinstaller Python
L’écran ne se met pas à jour → vérifier que les deux onglets sont ouverts en même temps

---

Astuce

Mettre `ecran.html` en plein écran (F11) pour un affichage événementiel propre.

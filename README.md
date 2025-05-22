# socio-analyse-gpt

# 🧠 Analyse Qualitative d'Entretiens avec IA

Ce projet vise à utiliser l'intelligence artificielle (LLM) pour réaliser une **analyse qualitative d'entretiens sociologiques**, en identifiant automatiquement des **thématiques** et en extrayant les **verbatims** les plus significatifs.

Il a été réalisé par BOUDRIA Ines et Dounia PIHAN

## 📁 Structure du projet

├── data/ → Fichiers PDF des entretiens
├── outputs/ → Résultats produits (JSON, graphiques…)
├── main/ → Scripts Python d'analyse
├── requirements.txt → Dépendances Python
├── README.md → Ce fichier

📂 Données

Les données utilisées sont anonymisées, au format .pdf, et stockées dans le dossier data/.

## 📌 Objectifs

- Automatiser l’extraction de **thématiques** à partir d’entretiens.
- Extraire les **verbatims clés** associés à chaque thématique.
- Générer un **top 5** des thématiques les plus fréquentes.

## Réalisations 

1. Extraction des thématiques et verbatims

Le script python extrairethemes.py :

lit tous les PDF dans data/,
appelle le modèle Groq (LLM) pour analyser chaque chunk de texte,
génère un fichier entretiens_structures.json dans outputs/.

2. Génération du top 5

Le script top5themes.py :

lit le JSON structuré,
extrait les 5 thématiques les plus fréquentes,
associe les verbatims liés à chaque thème,
enregistre tout dans le .json,

3. Test de visualisation : 

Le script graphiquesthemes.py

crée un graphique camembert graphique_top5.png.
Un fichier PNG est généré avec la répartition des 5 thèmes les plus présents dans les entretiens.


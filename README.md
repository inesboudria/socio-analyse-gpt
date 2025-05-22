# socio-analyse-gpt

# 🧠 Analyse Qualitative d'Entretiens avec IA

Ce projet vise à utiliser l'intelligence artificielle (LLM) pour réaliser une **analyse qualitative d'entretiens sociologiques**, en identifiant automatiquement des **thématiques** et en extrayant les **verbatims** les plus significatifs.

## 📁 Structure du projet

├── data/ → Fichiers PDF des entretiens
├── outputs/ → Résultats produits (JSON, graphiques…)
├── main/ → Scripts Python d'analyse
├── requirements.txt → Dépendances Python
├── README.md → Ce fichier


## 📌 Objectifs

- Automatiser l’extraction de **thématiques** à partir d’entretiens.
- Extraire les **verbatims clés** associés à chaque thématique.
- Générer un **top 5** des thématiques les plus fréquentes.

1. Extraction des thématiques et verbatims

Le script python :

lit tous les PDF dans data/,
appelle le modèle Groq (LLM) pour analyser chaque chunk de texte,
génère un fichier entretiens_structures.json dans outputs/.
2. Génération du top 5
Le script top5_maker.py :

lit le JSON structuré,
extrait les 5 thématiques les plus fréquentes,
associe les verbatims liés à chaque thème,
enregistre tout dans top5.json,
crée un graphique camembert graphique_top5.png.
📈 Exemple de sortie (visualisation)

Un fichier PNG est généré avec la répartition des 5 thèmes les plus présents dans les entretiens.


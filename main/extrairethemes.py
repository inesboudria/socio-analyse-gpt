!pip install groq tiktoken matplotlib pandas PyPDF2 pdfplumber

import os
import pdfplumber 
import json
import PyPDF2
import tiktoken
import time
import groq

GROQ_API_KEY = "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"
LLAMA_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

PDF_FOLDER = "./entretiens_pdf"
OUTPUT_JSON = "entretiens_structures.json"
MAX_TOKENS = 5000

client = groq.Groq(api_key=GROQ_API_KEY)

enc = tiktoken.encoding_for_model("gpt-4")

def count_tokens(text):
    return len(enc.encode(text))

def split_text_by_tokens(text, max_tokens):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if count_tokens(" ".join(current_chunk)) > max_tokens - 200: 
            chunks.append(" ".join(current_chunk))
            current_chunk = []
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def extraire_texte_pdf(chemin_pdf):
    texte = ""
    try:
        with pdfplumber.open(chemin_pdf) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    texte += page_text + "\n"
    except Exception as e:
        print(f"Erreur avec {chemin_pdf} : {e}")
    return texte

def extraire_themes_verbatims(texte):
    prompt = f"""
Voici un extrait d'entretien sociologique.
Il peut contenir des thématiques et des verbatims.

Ta tâche est de :
1. Identifier les *thématiques*.
2. Identifier les *verbatims*.

Format réponse :

Thématiques:
- thème 1
- thème 2

Verbatims:
- "verbatim 1"
- "verbatim 2"

Contenu :

{texte}
"""
    response = client.chat.completions.create(
        model=LLAMA_MODEL,
        messages=[
            {"role": "system", "content": "Tu es un expert en analyse qualitative."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

resultats = []

for filename in os.listdir(PDF_FOLDER):
    if not filename.endswith(".pdf"):
        continue

    path = os.path.join(PDF_FOLDER, filename)
    contenu = extraire_texte_pdf(path)
    print(f"[INFO] Analyse de {filename}")

    chunks = split_text_by_tokens(contenu, MAX_TOKENS)

    thematiques_total = []
    verbatims_total = []

    for chunk in chunks:
        try:
            sortie = extraire_themes_verbatims(chunk)
        except Exception as e:
            print(f"Erreur IA sur {filename} : {e}")
            continue

        lignes = sortie.splitlines()
        current = None
        for ligne in lignes:
            ligne = ligne.strip()
            if ligne.lower().startswith("thématiques:"):
                current = "thematiques"
                continue
            elif ligne.lower().startswith("verbatims:"):
                current = "verbatims"
                continue
            if current == "thematiques" and ligne.startswith("-"):
                thematiques_total.append(ligne[1:].strip())
            elif current == "verbatims" and ligne.startswith("-"):
                verbatims_total.append(ligne[1:].strip().strip('"'))

    resultats.append({
        "entretien": filename,
        "thématiques": list(set(thematiques_total)),
        "verbatims": list(set(verbatims_total))
    })

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=4)

print(f"✅ JSON généré : {OUTPUT_JSON}")

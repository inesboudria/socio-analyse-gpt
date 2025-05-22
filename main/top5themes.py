import json
from collections import Counter

with open("entretiens_structures.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_themes = []

for entretien in data:
    all_themes.extend(entretien.get("thématiques", []))

theme_counts = Counter(all_themes)

top_5 = theme_counts.most_common(5)

result_top_5 = []

for theme, count in top_5:
    verbatims_associes = []

    for entretien in data:
        if theme in entretien.get("thématiques", []):
            verbatims_associes.extend(entretien.get("verbatims", []))

    result_top_5.append({
        "thématique": theme,
        "occurrences": count,
        "verbatims": list(set(verbatims_associes))
    })

with open("json5top.json", "w", encoding="utf-8") as f:
    json.dump(result_top_5, f, ensure_ascii=False, indent=4)

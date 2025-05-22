import json
import matplotlib.pyplot as plt

with open("json5top.json", "r", encoding="utf-8") as f:
    data = json.load(f)

themes = [item["thématique"] for item in data]
occurrences = [item["occurrences"] for item in data]

plt.figure(figsize=(10, 6))
bars = plt.barh(themes, occurrences, color="lightcoral")
plt.xlabel("Nombre d'occurrences")
plt.title("Top 5 des thématiques des entretiens")
plt.gca().invert_yaxis()
plt.tight_layout()

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.2, bar.get_y() + bar.get_height() / 2,
             f"{int(width)}", va='center')

plt.savefig("top5_themes.png", dpi=300)
plt.show()

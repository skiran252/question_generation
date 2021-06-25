import json

with open("train-v2.0.json") as f:
    squad = json.loads(f.read())

total = 0
for article in squad["data"]:
    total+=len(article["paragraphs"])
# print(squad["data"].keys())
print(total)
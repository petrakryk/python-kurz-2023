import json

with open('/Users/petrakrykorkova/Documents/body.json') as vstup:
    data = vstup.read()

prospech = json.loads(data)

for item in prospech:
    if prospech[item] >= 60:
        prospech[item] = "Pass"
    else:
        prospech[item] = "Fail"

with open("prospech.json", mode="w", encoding="utf-8") as vystup:
    json.dump(prospech, vystup, ensure_ascii=False)



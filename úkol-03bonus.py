import json

with open('/Users/petrakrykorkova/Documents/body.json') as vstup:
    data = vstup.read()

prospech = json.loads(data)

with open('/Users/petrakrykorkova/Documents/bonusy2.json') as vstup_bonusy:
    bonusy_data = vstup_bonusy.read()

bonusy = json.loads(bonusy_data)

hodnoceni = {
    "1": (90, 100),
    "2": (70, 89),
    "3": (50, 69),
    "4": (30, 49),
    "5": (0, 29)
    }

znamky = {}

for item in prospech:
    if item in bonusy:
        prospech[item] = prospech[item] + bonusy[item]
    
    for znamka in hodnoceni:
        low = hodnoceni[znamka][0]
        top = hodnoceni[znamka][1]

        if (prospech[item] >= low) and (prospech[item] < top):
            znamky.update({item: znamka})

        elif (prospech[item] > hodnoceni["1"][0]):
            znamky.update({item: "1"})

with open("znamky.json", mode="w", encoding="utf-8") as vystup:
    json.dump(znamky, vystup, ensure_ascii=False)

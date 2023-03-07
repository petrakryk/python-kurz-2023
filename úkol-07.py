class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return print("Potvrzuji zapůjčení vozidla.")
        else:
            return print("Vozidlo není k dispozici.")
    
    def get_info(self):
        return print(f"registrační značka: {self.registracni_znacka}, typ vozidla: {self.typ_vozidla}")
    
    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni
        self.dostupne = True
        if pocet_dni < 7:
            self.cena = 400 * pocet_dni
        else:
            self.cena = 300 * pocet_dni
        return (f"Počet dní: {self.pocet_dni}, cena za půjčení vozidla {self.typ_vozidla}: {self.cena} Kč.")

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
škoda = Auto("1P3 4747", "Škoda Octavia", 41253)

input_car = input("Jaké vozidlo si chcete vypůjčit?: " ).lower()

if input_car == "peugeot":
    peugeot.get_info()
    peugeot.pujc_auto()
else:
    škoda.get_info()
    škoda.pujc_auto()
    
input_car2 = input("Jaké další vozidlo si chcete vypůjčit?: " ).lower()
if input_car2 == "peugeot":
    peugeot.get_info()
    peugeot.pujc_auto()
else:
    škoda.get_info()
    škoda.pujc_auto()
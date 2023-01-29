sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_zakaznik = input ("Zadejte kód součástky: ")

if kod_zakaznik in sklad.keys():
    mnozstvi_zakaznik = int(input("Zadejte množství: "))
    
    if mnozstvi_zakaznik > sklad[kod_zakaznik]:
        print(f'Lze prodat pouze {sklad[kod_zakaznik]} kusů produktu.')

    else:
        print("Požadované množství produktu je k dispozici.")
        sklad[kod_zakaznik] = sklad[kod_zakaznik] - mnozstvi_zakaznik

        #print(sklad)#kontrola zůstatku na skladě
else:
    print(f'Požadovaný produkt není skladem.')

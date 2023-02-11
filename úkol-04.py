import math

tel_cis = input("Zadejte telefonní číslo: ")

def overeni (tel_cis):
    if len(tel_cis) == 9:
        return(True)
    elif (len(tel_cis) == 13) and ((tel_cis[:4]) == "+420"):
        return(True)
    else:
        return(False)

def cena (zprava):
    cena_zpravy = math.ceil((len(zprava)/180)) * 3
    return(cena_zpravy)

if overeni(tel_cis) == False:
    print("Nesprávný formát čísla. Spusťte program znovu.")
    exit()
else:
    zprava = input("Zadejte zprávu k odeslání: ")
    print(f'Cena za odeslání zadané zprávy je: {cena(zprava)} Kč.')



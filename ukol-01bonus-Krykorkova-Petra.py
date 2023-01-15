jmeno = input("Zadejte své křesní jméno: ")
prijmeni = input("Zadejte své příjmení: ")
jmeno_a_prijmeni = jmeno +" "+ prijmeni
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print((jmeno[0].upper())+(jmeno[1:].lower())+" "+(prijmeni[0].upper())+(prijmeni[1:].lower()))
print((jmeno[0].upper()) + "." + (prijmeni[0].upper()) + ".")
if len(jmeno) > 5:
    print((jmeno[0].upper())+". "+(prijmeni[0].upper())+(prijmeni[1:].lower()))
else:
    print((jmeno[0].upper())+(jmeno[1:].lower())+" "+(prijmeni[0].upper())+(prijmeni[1:].lower()))

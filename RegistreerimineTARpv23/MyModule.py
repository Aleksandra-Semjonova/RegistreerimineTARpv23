kasutaja={}

def registreerimine():
    nimi=input("Sisestage Kasutaja nimi: ")
    parool=input("Sisetage parool: ")
    if nimi in kasutaja:
        print("Kasutaja nimi on hõivatud. Kirjutage  Teine nimi.")
    else: 
        kasutaja[nimi]=parool
        print("Registreerimine lõpetatud.")

def autoriseerimine():
    nimi=input("Sisestage Kasutaja nimi: ")
    parool=input("Sisetage parool: ")
    if nimi in kasutaja and kasutaja[nimi]==parool:
        print("")



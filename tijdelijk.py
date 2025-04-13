from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5,
    }
    aanbieding = prijzen["aardbei"] * 0.8

    # Voor het vinden van de juiste index twijfel ik tussen de methode index(0) of index("€")+5  Met deze laatste kap je altijd op tijd af na het euro-teken, ook als het geen 0 is.
    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
    reclame_tekst2 = reclame_tekst[:reclame_tekst.index("0")]
    reclame_tekst2b = reclame_tekst[:reclame_tekst.index("€")+5]

    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split(" ")

    for el in reclame_tekst4:
        if len(el) > 4:
            print(el)   
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()    





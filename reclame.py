from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting) :
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs*(1-korting)} euro."

def inkomsten_toaal(inkomsten,btw) :
    totaal_inkomsten = 0
    for i in inkomsten :    
        totaal_inkomsten += i
    return f"Het toaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {totaal_inkomsten*btw} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst) :
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    laagste_en_hoogste = [laagste, hoogste]
    return laagste_en_hoogste

def gemiddelde(mijn_lijst) :
    som = 0
    for i in mijn_lijst :
        som += i
    gemiddelde_imkomsten = som / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_imkomsten} euro."

def meervoudig(invoer_lijst) : 
    uitvoer_meervoudig = laag_en_hoog(invoer_lijst)
    return uitvoer_meervoudig

def combinatie(invoer_lijst_2) :
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    combinatie = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return combinatie




def presenteer (dict, totaal):
    uitvoer = []
    for product,prijs in dict.items():
        uitvoer.append(f"{product} : {prijs} euro")
    uitvoer.append("=" * 20)
    uitvoer.append(f"Totaal : {totaal} euro")
    for el in uitvoer:
        print(el)

"""
mijndict = {
"vis" : 10,
"vlees" : 25,
"overig": 15
}
totaal_totaal = 50
"""

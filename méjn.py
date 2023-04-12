import math

#függvények
def szögfok(sz, m1, m2):
    return math.degrees( math.acos((m1**2 + m2**2 - sz**2)/(2*m1*m2)) )

#1
finp = open("Háromszögek.txt", mode="rt", encoding="utf-8")
tartalom = finp.read()
finp.close()
adatsorok = tartalom.split('\n')

#2
eredmenySorok = []
for item in adatsorok:
    item != '';
    reszletek = item.split(';')

    a = float(reszletek[0].replace(',' , '.'))
    b = float(reszletek[1].replace(',' , '.'))
    c = float(reszletek[2].replace(',' , '.'))
    alfa = szögfok(a, b, c)
    betta = szögfok(b, a, c)
    gamma = szögfok(c, a, b)

    eredmeny = f"{alfa:.2f};{betta:.2f};{gamma:.2f}\n"
    eredmenySorok.append(eredmeny)

#3
fout = open("szogek.txt", mode="wt", encoding="utf-8")
fout.writelines(eredmenySorok)
fout.close


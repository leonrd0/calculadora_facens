"""
Calculando media de final (Facens);
O calculo possui a seguinte formula
(AC1*0,15)+(AC2*0,3)+(AG*0,1)+(AF*0,45)
"""

ac1 = input("Digite o valor da AC1: ")
ac2 = input("Digite o valor da AC2: ")
ag = input("Digite o valor da AG: ")
af = input("Digite o valor da AF: ")

media = (float(ac1) * 0.15)+(float(ac2) * 0.3)+(float(ag) * 0.1)+(float(af) * 0.45)
print(media)
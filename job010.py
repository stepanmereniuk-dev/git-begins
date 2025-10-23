
def calcul_interet(capital, tax, years):
    interet = capital * tax * years
    return interet

interet1 = calcul_interet(5000, 0.02, 1)
interet2 = calcul_interet(5000-(5000*0.1), 0.01, 1)

print(f"Le montant des intérêts pour le premier cas est de {interet1} euros.")
print(f"Le montant des intérêts pour le deuxième cas est de {interet2} euros.")
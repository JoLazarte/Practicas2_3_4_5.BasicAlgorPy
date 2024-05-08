"""
Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero
e imprima a cuántos billetes equivale:
billetes de $1000, $500, $100, $50, $10, $5 y $1.
Desarrollar dicho programa de tal forma que se minimice la cantidad de
billetes entregados por el cajero.

"""
moneyAmt = int (input ("Ingrese una cantidad de dinero: "))

#Se otorga en billetes de: 
bill1000 = moneyAmt // 1000 #(cuántos $ de mil hay)
sobranA = moneyAmt % 1000 #(el resto)
print(f"{moneyAmt} corresponde a {bill1000} billete/s de $ 1000 pesos.")

bill500 = sobranA // 500 #(cuántos $ de 500 hay)
sobranB = sobranA % 500 #(el resto)
print(f"{moneyAmt} corresponde a {bill500} billete/s de $ 500 pesos.")

bill100 = sobranB // 100 #(cuántos $ de 100 hay)
sobranC = sobranB % 100 #(el resto)
print(f"{moneyAmt} corresponde a {bill100} billete/s de $ 100 pesos.")

bill50 = sobranC // 50 #(cuántos $ de 50 hay)
sobranD = sobranC % 50 #(el resto)
print(f"{moneyAmt} corresponde a {bill50} billete/s de $ 50 pesos.")

bill10 = sobranD // 10 #(cuántos $ de 10 hay)
sobranE = sobranD % 10 #(el resto)
print(f"{moneyAmt} corresponde a {bill10} billete/s de $ 10 pesos.")

bill5 = sobranE // 5 #(cuántos $ de 5 hay)
sobranF = sobranE % 5 #(el resto)
print(f"{moneyAmt} corresponde a {bill5} billete/s de $ 5 pesos.")

bill1 = sobranF // 1 #(cuántos $ de 1 hay)
sobranG = sobranF % 1 #(el res
print(f"{moneyAmt} corresponde a {bill1} billete/s de $ 1 peso.")
print(f"Faltan {sobranG} pesos.")
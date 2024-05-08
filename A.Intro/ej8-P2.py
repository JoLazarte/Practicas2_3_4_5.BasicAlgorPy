"""
Leer una medida en metros e imprimir esta medida expresada en centímetros,
pulgadas, pies y yardas. Los factores de conversión son: 1 yarda = 3 pies,
1 pie = 12 pulgadas, 1 pulgada = 2,54 cm, 100 cm = 1 metro. 
"""
m = int (input ("Ingrese una medida en metros: "))
cm = m*100
pul = cm//2.54
pie = pul//12
yar = pie//3

print(cm, pul, pie, yar)
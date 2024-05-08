"""
 Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos.
 Por ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.

minuto = 60 s· 1hora = 60 minutos· 1 día = 24 hs

NOTA: Para hallar en Python el resto de la división x // c se hace  x % c.    
Ejemplo:  6=20 // 3 y 2=20 % 3

"""
Seg = int (input ("Ingrese una cantidad de segundos: "))

Min = Seg//60
SegR = Seg%60 #lo que no se puede transformar en minutos, los segundos reales

Hr =Min//60 #los seg transformados en min ahora se transforman en horas
MinR = Min%60 #los minutos que no se pueden transformar en horas, los minutos reales

Dia = Hr//24 #las horas se transforman en días
HrR = Hr%24 #las horas que no se pueden transformar en días

print(Dia, HrR, MinR, SegR)
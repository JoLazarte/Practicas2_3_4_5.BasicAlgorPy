
# Sintaxis de los argumentos del print que estan entre comillas
# %d para decimal. Si queremos que ocupe 5 espacios ponemos %5d
# %f para float. Por ejemplo %5.2f significa que el float ocupara 5 espacios en total de los cuales 2 son decimales
# %s para string. Por ejemplo %5s significa que el string ocupara 5 espacios en total, indentados a izquierda.
# %c caracter
#\t para corre una tabulacion para la siguiente columna a la derecha

#Ejemplo
numero = 3.141532
print("%12.2f " %numero,"%5.4f\t" %numero, "%4.2f" %numero, "%4.2f" %numero )


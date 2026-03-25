from random import randint

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Juanio", "julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"]
lista =[]

for i in range (12):
    dato = randint (20, 80)
    lista.append (dato)

print(lista)

mayor = max(lista)
mes = lista.index(mayor)

print (f"se vendieron más autos en {meses[mes]}")
print (f"Se vendeiron {mayor} autos")



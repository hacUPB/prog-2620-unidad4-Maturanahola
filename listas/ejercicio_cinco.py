from random import randint

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"]
lista =[]

for i in range (12):
    dato = randint (0, 1000)
    lista.append (dato)

print(lista)

mayor = max(lista)
veces = lista.count(mayor)
mes = lista.index(mayor)

if veces > 1:
    lista_meses =[]
    for i in range(len(lista)):
        if lista [i] == mayor:
            lista_meses.append(i)
    print("ventas mayores en:")
    for mes in lista_meses: 
        print(f"{meses[mes]}")

else:
    mes = lista.index(mayor)

print(f"El {mayor} se repite {veces} veces")
print (f"En {meses[mes]} se vendieron más autos")
print (f"Se vendeiron {mayor} autos")
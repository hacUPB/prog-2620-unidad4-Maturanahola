import random
lista = []
for i in range (100,200):
    lista.append(random.randint(100, 200))
x = lista [0]
for y in lista:
    if x< y:
        x = y
menor = lista[0]
for z in lista:
    if menor > z:
        menor = z
m = max(lista)
menor = min (lista)
print (f"{lista}. el maximo es {m} y el menor es {menor}")
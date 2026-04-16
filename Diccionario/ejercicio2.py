vuelo = {
    "aerolinea" : "avianca",
    "vuelo" : "AV123",
    "origen" : "BOG",
    "destino": "MDE"
}

ciudad_llegada = vuelo["destino"]

#modifcar valor existente
vuelo["destino"]= "CLO"
print (vuelo["destino"])

#Agregar un nuevo par clave-valor
vuelo["estado"] = "en_el_aire"
print(vuelo)

#Uso del método `.get()` (Acceso seguro)
p= vuelo.get("piloto", "no hay piloto, el avión se cae")
print(p)

del vuelo["vuelo"]
print(ciudad_llegada)




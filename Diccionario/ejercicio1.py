aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

# Creación con dict()
motor = dict(fabricante="GE", modelo="GE9X", empuje=470, bypass_ratio=10)

asignaturas = {
    1 : "Matematicas",
    2 : "Ciencias"
}

# Acceso a valores
print(vuelo["tripulacion"][1])

#Modificar valor
vuelo["distancia"]=4000
print(vuelo["distancia"])

#Crear un nuevo para llave: valor

asignaturas[9] = "programacion"
print(asignaturas[9])

#Eliminar par clave :valor
del aeronave ["velocidad_max"]

#comprobar existencia de clave
if "vuelo" in aeronave:
    print(f"El alcance es {aeronave["alcance"]}Km")
else: 
    print("la clave no existe")

velociad = aeronave.get ("velocidad_max", "No disponible")
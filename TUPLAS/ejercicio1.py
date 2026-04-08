# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

print(f"coordenadas: {coordenada[0]}")
coordenada[1] = -120
print(f"coordenadas: {coordenada[1]}")  # Esto generará un error porque las tuplas son inmutables

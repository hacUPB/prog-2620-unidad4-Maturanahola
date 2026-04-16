limite_horas_componente = 300

aeronaves = []

num_aeronaves = int(input("Ingrese el número de aeronaves a registrar "))
i = 0
while i < num_aeronaves:
    print("REGISTRO DE AERONAVE")
    matricula = input("Ingrese la matrícula: ")
    modelo = input("Ingrese el modelo: ")
    horas_de_vuelo = float(input("Ingrese las horas de vuelo: "))

    aeronave = {
        "matricula": matricula,
        "modelo": modelo,
        "horas_de_vuelo": horas_de_vuelo,
        "componentes": []
    }
    comp = int(input("Ingrese el número de componentes: "))
    j = 0
    while j < comp:
        print("REGISTRO DE COMPONENTE")
        nombre = input("Ingrese el nombre del componente: ")
        horas_de_uso = float(input("Ingrese las horas de uso: "))

        componente = {
            "nombre": nombre,
            "horas_de_uso": horas_de_uso
        }
        aeronave["componentes"].append(componente)
        j += 1

        aeronaves.append(aeronave)
    i += 1

# reporte de mantenimiento
print("REPORTE DE MANTENIMIENTO")
i = 0
while i < len(aeronaves):
    aeronaave = aeronaves[i]
    j = 0   
    while j < len(aeronaave["componentes"]):
        componente = aeronaave["componentes"][j]
        if componente["horas_de_uso"] > limite_horas_componente:
            print("Mantenimiento requerido")
            print("Aeronave: ", aeronaave["matricula"], "-", aeronaave["modelo"])
            print("Componente: ", componente["nombre"])
            print("Horas de uso: ", componente["horas_de_uso"])
            print("Límite: ", limite_horas_componente)
        j += 1
    i += 1
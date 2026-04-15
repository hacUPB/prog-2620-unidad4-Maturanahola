# 📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️

**Instrucciones para los estudiantes:**
1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre `AUTOEVALUACION.md`.
2. Lean cuidadosamente cada criterio de la rúbrica.
3. En el apartado **Nota Esperada**, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio.
4. En el apartado **Justificación**, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos.
5. En el apartado **Evidencia**, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con \`\`\`) que respalden su justificación.
6. Al final, calculen su nota definitiva esperada según los porcentajes.

---

## 👥 1. Información del Equipo

* **Miembro 1:** [Juan Esteban Maturana] - [000570356/ID]
* **Miembro 2:** [None] - [None/None]

---

## 📊 2. Evaluación por Criterios

### Criterio 1: Diagrama y Lógica (Valor: 20%)
*Evalúa si el diagrama es claro, lógico y representa fielmente la estructura de datos utilizada (listas/diccionarios) y el flujo del programa.*

* **Nota Esperada (0.0 - 5.0):** [5.0]
* **Justificación:** 
  > *[Considero que me debo sacar una 5.0 porque hago entrega de todos los entregables del reto, el diagrama de flujo ilustra bastante bien lo que se queria lograr con el codigo y ademas el codigo cumple satisfactoriamente y con exactitud lo que se pedia en las rubricas]*
* **Evidencia:**
  *Inserta aquí la imagen de tu diagrama (ej. `![Diagrama de Flujo](./img/diagrama.png)`) y explica brevemente cómo se conecta con el código.*
  ![DIAGRAMA DE FLUJo](/imagenes/reto%20unidad%204.2%20(1).png)

### Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
*Evalúa si se utilizaron diccionarios y listas de manera correcta y anidada para almacenar los datos ingresados por el usuario, sin redundancias.*

* **Nota Esperada (0.0 - 5.0):** [5.0]
* **Justificación:**
  > *[Explica aquí cómo estructuraste la memoria. Por ejemplo: "Usamos un diccionario principal donde la llave es la matrícula de la aeronave, y el valor es una lista de diccionarios que representan cada componente..."]*

* **Evidencia:**
  *Pega aquí el fragmento de código exacto donde inicializas y llenas estas estructuras. Usa el formato de código de Markdown:*
  ```python
  # Reemplaza esto con tu fragmento de código real
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

# ... código de inserción de datos ...

### Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
*Evalúa el respeto total a las reglas: uso de ciclos clásicos (for/while), cero uso de list comprehensions, y ninguna librería/función avanzada no vista en clase.*

* **Nota Esperada (0.0 - 5.0):** [4.7]
* **Justificación:**
    > *[Solo se hizo uso de lo permitido y visto en clase pero solo se hace uso de ciclos anidados "while" no "for"]*
* **Evidencia:** *Pega un fragmento de código que demuestre cómo iteraste sobre los datos de forma clásica (sin atajos avanzados).*
````python
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
````

### Criterio 4: Funcionalidad del Código (Valor: 15%)
*Evalúa si el programa pide datos correctamente, no se "crashea" y genera el reporte final de mantenimiento esperado.*

* **Nota Esperada (0.0 - 5.0):** [5.0]
* **Justificación:**
    > *[EL programa muestra exitosamente las 3 aeronaves exigidas e incluso más, de tal forma que se realizan todas las que el usuario desee, tambien realiza el reporte final de mantenimiento (si el componente necesita mantenimiento)]*

* **Evidencia:** *Inserta aquí 1 o 2 pantallazos (![Ejecución](./img/consola1.png)) mostrando la terminal donde se vea:*
*El ingreso manual de datos.*
*El reporte final impreso en pantalla con las piezas que requieren mantenimiento.*

![REPORTE DE MANTENIMIENTO](/imagenes/Evidencias.png)

### Criterio 5: Preparación para Sustentación (Valor: 15%)
*Aunque esta nota la dará el profesor en la entrevista oral, autoevalúen su nivel de preparación y comprensión del código que entregaron.*

* **Nivel de Confianza (Bajo / Medio / Alto):** [MEdio]
* **Justificación:**
    > *[Entiendo el codigo por completo, y estoy en la capacidad de explicarlo sin ningún inconveniente]*
* **Evidencia de preparación:** Lo hice solo, lo que significa que se realizo con mi propia logica, capacidades y entendimiento


### 📈 3. Cálculo de Nota Definitiva Esperada
Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.

|Criterio	|Nota |Asignada	|Peso	|Subtotal |(Nota * Peso) |
|---|---|---|---|---|---|
|1. Diagrama y Lógica	|[5.0]	|20% |(0.2)	|[1]|
|2. Uso de Estructuras	|[5.0]	|30% |(0.3)	|[1,5]|
|3. Cumplimiento Restricciones|	[4,7]	|20% |(0.2)	|[0,94]|
|4. Funcionalidad	|[5.0]	|15% |(0.15)	|[0,75]|
|5. Sustentación (Estimado)|	[4,5]|	15%| (0.15)|	[0,675]|

NOTA FINAL ESPERADA		100%	[4.8]

✨ ""La educación es para el carácter, no solo para la mente"." ✨
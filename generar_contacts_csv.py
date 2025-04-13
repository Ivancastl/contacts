import pandas as pd
import random

# Crear nombres personalizados
def crear_nombres(cantidad, prefijo):
    return [f"{prefijo}{i}" for i in range(1, cantidad + 1)]

# Crear teléfonos con o sin números fijos
def crear_telefonos(cantidad, ladas, numeros_fijos=None):
    telefonos = []
    for _ in range(cantidad):
        lada = random.choice(ladas)
        if numeros_fijos:
            telefono = f"{lada}{numeros_fijos}{random.randint(1000, 9999)}"
        else:
            telefono = f"{lada}{random.randint(1000000, 9999999)}"
        telefonos.append(telefono)
    return telefonos

# Entradas del usuario
prefijo = input("¿Cómo quieres llamar a los contactos? (ej: Persona, Usuario, Contacto): ").strip()
cantidad = int(input("¿Cuántos números deseas generar?: "))

# Ingreso de ladas personalizadas
ladas_input = input("Ingresa las ladas que quieres usar, separadas por comas (ej: 55,33,777): ")
ladas = [lada.strip() for lada in ladas_input.split(",") if lada.strip().isdigit()]

if not ladas:
    print("No se ingresaron ladas válidas. Finalizando el programa.")
    exit()

# Opción de usar números fijos
usar_fijos = input("¿Quieres usar 3 números fijos después de la lada? (sí/no): ").strip().lower()
numeros_fijos = ""

if usar_fijos in ["sí", "si"]:
    while True:
        numeros_fijos = input("Ingresa los 3 números fijos (por ejemplo, 123): ").strip()
        if len(numeros_fijos) == 3 and numeros_fijos.isdigit():
            break
        else:
            print("Por favor, ingresa exactamente 3 números.")

# Generar datos
nombres = crear_nombres(cantidad, prefijo)
telefonos = crear_telefonos(cantidad, ladas, numeros_fijos)

# Crear DataFrame y guardar CSV
df = pd.DataFrame({"nombre": nombres, "telefono": telefonos})

nombre_archivo = input("Nombre del archivo CSV (ejemplo: contactos_mexico.csv): ").strip()
if not nombre_archivo.endswith(".csv"):
    nombre_archivo += ".csv"

df.to_csv(nombre_archivo, index=False, encoding="utf-8")
print(f"\n✅ Se ha creado el archivo CSV: {nombre_archivo}")

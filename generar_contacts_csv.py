import pandas as pd
import random

# Función para crear los nombres personalizados
def crear_nombres(cantidad, prefijo):
    return [f"{prefijo}{i}" for i in range(1, cantidad + 1)]

# Función para crear los números de teléfono
def crear_telefonos(cantidad, lada, numeros_fijos=None):
    telefonos = []
    for _ in range(cantidad):
        if numeros_fijos:
            # Si el usuario elige tener números fijos, lo combina con aleatorios
            telefono = f"{lada}{numeros_fijos}{random.randint(1000, 9999)}"
        else:
            # Si el usuario no elige números fijos, todo es aleatorio
            telefono = f"{lada}{random.randint(1000000, 9999999)}"
        telefonos.append(telefono)
    return telefonos

# Solicitar al usuario la entrada para personalizar
prefijo = input("¿Cómo quieres llamar a los contactos? (ejemplo: Persona, Usuario, Contacto): ")
cantidad = int(input("¿Cuántos números deseas generar? (Ejemplo: 10): "))
lada = input("¿Cuál es la lada de la región? (Ejemplo: 777 para Ciudad de México): ")

# Preguntar si quiere poner 3 números fijos
usar_numeros_fijos = input("¿Quieres poner 3 números fijos y el resto aleatorios? (sí/no): ").strip().lower()

numeros_fijos = ""
if usar_numeros_fijos in ["sí", "si"]:  # Aceptar tanto "sí" como "si"
    # Asegurarse de que se ingrese correctamente los tres números fijos
    while True:
        numeros_fijos = input("Ingresa los 3 números fijos (por ejemplo, 123): ").strip()
        if len(numeros_fijos) == 3 and numeros_fijos.isdigit():
            break
        else:
            print("Por favor, ingresa exactamente 3 números.")
        
# Crear los nombres y teléfonos
nombres = crear_nombres(cantidad, prefijo)
telefonos = crear_telefonos(cantidad, lada, numeros_fijos)

# Crear un diccionario con los datos
datos = {
    "nombre": nombres,
    "telefono": telefonos
}

# Crear un DataFrame de pandas
df = pd.DataFrame(datos)

# Nombre del archivo .csv
nombre_archivo = "datos_personalizados.csv"

# Guardar el DataFrame en un archivo .csv
df.to_csv(nombre_archivo, index=False, encoding='utf-8')

print(f"Se ha creado el archivo CSV: {nombre_archivo}")

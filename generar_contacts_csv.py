import pandas as pd
import random

def crear_nombres(cantidad, prefijo):
    return [f"{prefijo}{i}" for i in range(1, cantidad + 1)]

def crear_telefonos(cantidad, numeros_fijos, longitud_total):
    telefonos = []
    digitos_restantes = longitud_total - len(numeros_fijos)

    for _ in range(cantidad):
        aleatorios = ''.join(str(random.randint(0, 9)) for _ in range(digitos_restantes))
        telefonos.append(f"{numeros_fijos}{aleatorios}")
    return telefonos

print("📇 Generador de contactos con teléfonos personalizados\n")

# Paso 1: Prefijo para nombres
prefijo = input("📝 ¿Cómo quieres llamar a los contactos? (ej: Persona, Usuario): ").strip()

# Paso 2: Cantidad de números a generar
while True:
    cantidad_input = input("🔢 ¿Cuántos números deseas generar?: ").strip()
    if cantidad_input.isdigit() and int(cantidad_input) > 0:
        cantidad = int(cantidad_input)
        break
    print("⚠️ Ingresa un número válido mayor que cero.")

# Paso 3: Longitud del número telefónico
while True:
    longitud_input = input("📱 ¿Cuántos dígitos debe tener cada número telefónico (ej: 10)?: ").strip()
    if longitud_input.isdigit() and 5 <= int(longitud_input) <= 15:
        longitud_total = int(longitud_input)
        break
    print("⚠️ Ingresa un número entre 5 y 15.")

# Paso 4: Cuántos dígitos fijos dejar
while True:
    fijos_input = input(f"🔒 ¿Cuántos dígitos de los {longitud_total} deseas dejar fijos al inicio?: ").strip()
    if fijos_input.isdigit() and 0 <= int(fijos_input) < longitud_total:
        longitud_fijos = int(fijos_input)
        break
    print(f"⚠️ Debe ser un número entre 0 y {longitud_total - 1}.")

# Paso 5: Ingreso de los dígitos fijos
numeros_fijos = ""
if longitud_fijos > 0:
    while True:
        numeros_fijos = input(f"🔢 Ingresa los {longitud_fijos} dígitos fijos: ").strip()
        if numeros_fijos.isdigit() and len(numeros_fijos) == longitud_fijos:
            break
        print(f"⚠️ Por favor, ingresa exactamente {longitud_fijos} dígitos numéricos.")

# Generar nombres y teléfonos
nombres = crear_nombres(cantidad, prefijo)
telefonos = crear_telefonos(cantidad, numeros_fijos, longitud_total)

# Crear y guardar CSV
df = pd.DataFrame({"nombre": nombres, "telefono": telefonos})
archivo = input("💾 Nombre del archivo CSV (ej: contactos.csv): ").strip()
if not archivo.endswith(".csv"):
    archivo += ".csv"

df.to_csv(archivo, index=False, encoding="utf-8")
print(f"\n✅ ¡Archivo guardado exitosamente como '{archivo}' con {cantidad} contactos!")

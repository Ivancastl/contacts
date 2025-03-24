# Generador de Contactos WhatsApp

Este script genera un archivo CSV con números de teléfono aleatorios para ser utilizados como contactos de WhatsApp. Puedes personalizar la cantidad de contactos, la lada de la región y los números fijos.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Ivancastl/telegramOSINT.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd telegramOSINT
    ```

3. Instala las dependencias utilizando el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script `generar_contacts_csv.py`:

    ```bash
    python generar_contacts_csv.py
    ```

2. Responde a las preguntas que aparecerán en la terminal:
   - ¿Cómo quieres llamar a los contactos? (Ejemplo: Persona, Usuario, Contacto)
   - ¿Cuántos números deseas generar? (Ejemplo: 10)
   - ¿Cuál es la lada de la región? (Ejemplo: 777 para Ciudad de México)
   - ¿Quieres poner 3 números fijos y el resto aleatorios? (sí/no)

3. El archivo CSV con los contactos generados se guardará en el mismo directorio con el nombre `datos_personalizados.csv`.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

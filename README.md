# Generador de Contactos WhatsApp

Este script genera un archivo CSV con números de teléfono aleatorios para ser utilizados como contactos de WhatsApp. Puedes personalizar la cantidad de contactos, la lada de la región y los números fijos.

## ¿Cómo ejecutar el proyecto?

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local usando el siguiente comando:

\`\`\`bash
git clone https://github.com/Ivancastl/contacts.git
\`\`\`

### 2. Instalar dependencias

Una vez que hayas clonado el repositorio, navega a la carpeta del proyecto:

\`\`\`bash
cd generador_contactos
\`\`\`

Luego, instala las dependencias necesarias ejecutando:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Ejecutar el script

Para ejecutar el script que genera los contactos, usa el siguiente comando:

\`\`\`bash
python generar_contacts_csv.py
\`\`\`

El script te pedirá que ingreses:

- **Cómo quieres llamar a los contactos** (Ejemplo: Persona, Usuario, Contacto).
- **Cuántos números deseas generar** (Ejemplo: 10).
- **Cuál es la lada de la región** (Ejemplo: 777 para Ciudad de México).
- **Si quieres poner 3 números fijos y el resto aleatorios** (Responde "sí" o "no").

El archivo CSV con los contactos generados se guardará en el directorio del proyecto con el nombre **\`datos_personalizados.csv\`**.


## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

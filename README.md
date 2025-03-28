# Ejercicio Técnico: Cliente y Servidor TCP en Python

Este repositorio contiene un ejercicio técnico que implementa un servidor TCP y un cliente TCP en Python, que pueden comunicarse entre sí en localhost usando el puerto 5000.

---

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalado Python correctamente en tu sistema. Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).

### Instalación de Python
- Descarga e instala la última versión de Python.
- **Importante**: Durante la instalación, asegúrate de **marcar la casilla** de **"Add Python to PATH"** para poder ejecutar Python desde la línea de comandos (`cmd`).

---

## Instrucciones para ejecutar el servidor y cliente

1. **Clonar el repositorio** en tu máquina local:
   
   ```bash
   git clone https://github.com/DannyCrew/Servidor-TCP

2. **Ejecutar el servidor**

Abre una terminal o cmd en la carpeta del proyecto y ejecuta el siguiente comando:   

    python Servidor_TCP.py

El servidor mostrará el siguiente mensaje:


Servidor TCP escuchando en el puerto 5000...

3. **Ejecutar el cliente** (en una nueva terminal o ventana de cmd):

En otra terminal, ve a la carpeta del proyecto y ejecuta:

    python Cliente_TCP.py

El cliente solicitará al usuario ingresar un mensaje para enviar al servidor.

## Pruebas manuales
### Prueba de comunicación estándar

1. Escribe cualquier mensaje normal, por ejemplo: hola servidor.

2. El servidor responderá: 

    HOLA CLIENTE

## Prueba de desconexión

1. Envía el mensaje **DESCONEXION** desde el cliente.

2. Verifica que el servidor cierre la conexión con el cliente, mientras permanece disponible para nuevas conexiones.

### Notas importantes
Ejecuta siempre el servidor antes de iniciar el cliente para evitar errores de conexión.

Si no puedes ejecutar Python desde la terminal, asegúrate de haber marcado la opción "Add Python to PATH" durante la instalación de Python.

Si encuentras algún problema con la instalación de Python o con la ejecución de los scripts, consulta la documentación oficial de Python.

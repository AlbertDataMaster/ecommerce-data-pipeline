# 🛒 Manual eCommerce Data Pipeline (Etapa 1)

Bienvenido al manual de implementación de la primera fase de nuestro ecosistema de datos. En esta etapa, configuraremos el **Sistema de Origen (OLTP)**: una base de datos relacional cargada con más de 150,000 registros que simulan la operación real de una tienda en línea.

---

## 💻 Entorno del Proyecto
Este manual ha sido desarrollado y probado bajo las siguientes especificaciones:
* **Sistema Operativo:** macOS (Compatible con Linux y Windows mediante Docker).
* **Arquitectura:** 64-bit.
* **Objetivo:** Crear una base de datos PostgreSQL funcional y poblada.

---

## 🛠️ Herramientas Necesarias (Pre-requisitos)
Antes de comenzar, debes instalar estas tres herramientas en tu computadora. Haz clic en los enlaces para ir a las páginas oficiales de descarga:

1.  **Docker Desktop:** [Descargar aquí](https://www.docker.com/products/docker-desktop/). (Es el motor que permite crear contenedores).
2.  **Python 3.13:** [Descargar aquí](https://www.python.org/downloads/). (Es el lenguaje que usaremos para mover los datos).
3.  **Git:** [Descargar aquí](https://git-scm.com/downloads). (Para clonar este repositorio).

---

## 🚀 Guía de Implementación Paso a Paso

Sigue estos pasos en orden estricto. No saltes ninguno para asegurar el éxito.

### Paso 1: Clonar el Repositorio
Necesitamos traer los archivos de la nube a tu computadora local.
1. Abre tu terminal (Terminal en Mac/Linux o PowerShell en Windows).
2. Ejecuta el siguiente comando:
```bash
git clone [https://github.com/AlbertDataMaster/ecommerce-data-pipeline.git](https://github.com/AlbertDataMaster/ecommerce-data-pipeline.git)
cd ecommerce-data-pipeline
```
### Paso 2: Encender la Infraestructura (Docker) 🐳
¿Por qué? Vamos a crear un servidor de base de datos sin instalar programas complicados en tu sistema.
Asegúrate de que Docker Desktop esté abierto y corriendo.

En tu terminal, ejecuta:
```bash
docker-compose up -d
```
Descripción: Este comando lee el archivo docker-compose.yml y levanta dos servicios: PostgreSQL (donde viven los datos) y pgAdmin (la consola visual para ver los datos).

---
### Paso 3: Configurar el Entorno de Python 🐍
¿Por qué? Para que las herramientas de este proyecto no choquen con otras versiones que tengas en tu PC.

Crea un "cuarto limpio" (Entorno Virtual):
```bash
python3 -m venv venv
```
Activa el entorno (tu terminal mostrará un prefijo (venv)):
```bash
source venv/bin/activate
```
---

### Paso 4: Instalar las "Habilidades" (Dependencias) 🛠️
¿Por qué? Python necesita saber cómo leer archivos CSV y cómo conectarse a la base de datos de Docker.

Ejecuta:
```bash
pip install -r requirements.txt
```
---

### Paso 5: El Gran Final - Carga de Datos (Seeding) 📥
¿Por qué? Vamos a llenar la base de datos vacía con miles de filas de clientes, productos y ventas.

Ejecuta el script inteligente:
```bash
python seed_data.py
```
Descripción: El script tomará los archivos de la carpeta /data, arreglará los formatos de fecha y cargará todo en PostgreSQL.

---
### ✅ Validación: ¿Cómo saber si lo logré?

Para confirmar que el mueble está bien armado, entra a la consola visual:
Abre tu navegador y ve a: http://localhost:8080
Usuario: admin@admin.com | Contraseña: admin
Navega en el árbol de la izquierda: Servers > ecommerce_server > Databases > ecommerce_db > Schemas > public > Tables.

Debes visualizar estos números de registros:
👤 Users: 39,169
📦 Orders: 82,387
🏷️ Products: 29,120
⚡ Events: 47,929

### ⚠️ Solución de Problemas (FAQ)

"No se puede conectar al puerto 5432": Tienes otro PostgreSQL instalado y encendido en tu PC. Apágalo antes de correr Docker.
"Comando python3 no encontrado": Asegúrate de haber marcado la casilla "Add Python to PATH" durante la instalación de Python.

---

### Etapa 2 (Orquestación e Ingesta)

1. Preparación del Entorno
Antes de empezar, asegúrate de que los contenedores estén encendidos:

Abre la Terminal en la carpeta del proyecto.

Ejecuta el comando:

```bash
docker-compose up -d
```
Espera 30 segundos a que todos los servicios (Postgres, Airflow y pgAdmin) se estabilicen.

---

2. Validación en Airflow (Automatización)

Para verificar que el proceso de carga de datos está automatizado:
Abre tu navegador y ve a: http://localhost:8081.
Usuario: admin / Contraseña: admin.
En el listado, busca el DAG llamado 01_ingesta_oltp_ecommerce.
Asegúrate de que el interruptor azul a la izquierda del nombre esté en ON.
Haz clic en el botón de Play (Trigger DAG) a la derecha.
Verificación: Si aparece un círculo verde en la columna "Last Run", la ingesta fue exitosa.

---

3. Validación en pgAdmin (Base de Datos)
Para confirmar que los datos realmente llegaron a la base de datos:

Abre en tu navegador: http://localhost:8080.
Inicio de sesión en pgAdmin:
Email: admin@admin.com
Password: admin

Conectar al Servidor:

Si no ves el servidor a la izquierda, haz clic derecho en Servers > Register > Server.
En la pestaña Connection, usa:

Host: postgres_oltp
Username: Portafolio2026@
Password: Portafolio2026@

Consulta de Datos:

Navega por: Databases > Source > Schemas > public > Tables.
Haz clic derecho en la tabla products y selecciona View/Edit Data > All Rows.


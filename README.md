🛒 eCommerce Data Pipeline - Etapa 1: El Origen de los Datos (OLTP)
Este proyecto simula el "corazón" de una tienda en línea real. En esta primera fase, hemos construido una base de datos profesional con más de 150,000 registros que incluyen ventas, usuarios y productos.

🌟 ¿Qué estamos logrando?
Estamos transformando archivos de datos crudos (CSV) en una base de datos organizada y potente. Esto permite que una empresa pase de tener "papeles digitales" sueltos a tener una estructura sólida para tomar decisiones.

🚀 Guía de Instalación Paso a Paso
Sigue estas instrucciones para replicar este ecosistema en tu propia máquina:

1. Preparar la "Casa" de los Datos (Docker) 🐳
Comando:

Bash
docker-compose up -d
¿Por qué?: Las bases de datos pueden ser difíciles de configurar de forma idéntica en distintas computadoras.

Descripción: Docker crea una "caja virtual" (contenedor) donde la base de datos corre perfectamente sin importar si usas Mac, Windows o Linux. Es como llevar una oficina pre-amueblada a cualquier lugar; solo tienes que encender la luz.

2. Crear un Espacio de Trabajo Limpio (Entorno Virtual) 🐍
Comando:

Bash
python3 -m venv venv
source venv/bin/activate
¿Por qué?: Evitamos que las herramientas de este proyecto se mezclen o causen conflictos con otros programas en tu equipo.

Descripción: Esto crea un "entorno virtual". Imagina que es una mesa de trabajo nueva donde solo colocas las herramientas específicas que necesitas para este proyecto, manteniéndolo todo ordenado y seguro.

3. Instalar las Herramientas Necesarias 🛠️
Comando:

Bash
pip install -r requirements.txt
¿Por qué?: Python necesita aprender "habilidades" específicas para hablar con bases de datos y procesar grandes cantidades de información.

Descripción: Este comando lee una lista de instrucciones y descarga automáticamente todas las librerías necesarias (como Pandas y SQLAlchemy) para que el código funcione a la primera.

4. Llenar la Base de Datos (Seeding) 📥
Comando:

Bash
python seed_data.py
¿Por qué?: Una base de datos vacía no sirve para analizar nada. Necesitamos poblarla con información real.

Descripción: Este script actúa como un robot inteligente: lee los archivos de datos, los limpia, corrige formatos de fechas y los inserta de forma masiva en PostgreSQL. En pocos segundos, tendrás miles de filas listas para usar.

✅ Validación Visual (Prueba de Éxito)
Para confirmar que todo funciona correctamente, hemos utilizado pgAdmin para auditar los resultados:

Como se observa en la auditoría final:

Usuarios: 39,169 registrados.

Órdenes: 82,387 procesadas.

Productos: 29,120 en inventario.

Eventos: 47,929 acciones registradas.

🛠️ Solución de Problemas Frecuentes
Conflicto de Puertos: Si ya tienes otro servicio de base de datos corriendo, asegúrate de liberar el puerto 5432.

Conexión: El script utiliza credenciales seguras configuradas automáticamente en el contenedor Docker.
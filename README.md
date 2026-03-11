# 🚀 End-to-End eCommerce Data Pipeline: From OLTP to Cloud Data Warehouse OLAP to BI 

### 📖 Introducción
Este proyecto desarrolla una infraestructura de datos completa para un ecosistema de E-commerce, utilizando un dataset público de alta fidelidad que simula operaciones reales (usuarios, productos, pedidos y eventos de tráfico web).

La solución aborda el reto técnico de integrar un sistema transaccional local (OLTP) con un entorno analítico en la nube (OLAP). Se implementó un flujo automatizado de extracción, carga y transformación (ELT) diseñado para garantizar la integridad de los datos, la observabilidad del proceso y la escalabilidad de la arquitectura.

### 🛠️ Stack Tecnológico

* Origen: PostgreSQL (Dockerizado) como base de datos transaccional.
* Orquestación: Apache Airflow para la automatización y gestión de dependencias.
* Procesamiento: Python (Pandas & SQLAlchemy) para la lógica de extracción.
* Destino: Google BigQuery como Cloud Data Warehouse empresarial.
* Analítica e IA: BigQuery ML (Modelado Predictivo) y Looker Studio para BI.
* Infraestructura: Docker & Docker Compose para la consistencia del entorno.


## 🗺️ Roadmap de Implementación

Para facilitar la auditoría técnica y la replicabilidad, el proyecto se ha documentado en tres hitos fundamentales:

### [🔹 Fase 1: Configuración del Entorno Transaccional (OLTP)](docs/STAGE_01.md)
* Despliegue de PostgreSQL mediante contenedores (Docker).
* Estrategia de Data Seeding: carga de +150,000 registros normalizados.
* Validación de esquemas y relaciones en pgAdmin.

### [🔹 Fase 2: Orquestación y Control de Flujos](docs/STAGE_02.md)
* Configuración del ecosistema Airflow (Webserver, Scheduler, Worker).
* Diseño de DAGs (Directed Acyclic Graphs) para la sincronización de tareas.
* Manejo de conexiones y volúmenes persistentes.

### [🔹 Fase 3: Ingesta en la Nube y Seguridad (GCP)](docs/STAGE_03.md)
* Migración de datos a BigQuery Landing Zone.
* Implementación de políticas de seguridad mediante Service Accounts y manejo de secretos.
* Validación de calidad y disponibilidad de datos en Google Cloud Console.

### [🔹 Fase 4: Core Data Layer y Modelado Dimensional](docs/STAGE_04.md)
* **Construcción del Core Data Layer (CDL):** Transformación de datos crudos a un modelo analítico.
* **Modelo Estrella (Star Schema):** Diseño de dimensiones maestras y tablas de hechos centralizadas.
* **Performance Tuning en BigQuery:** Implementación de Particionamiento (Time-unit) y Clustering (Multi-column) para optimización de costos y velocidad.
* **Encapsulamiento de Lógica:** Creación de Stored Procedures para garantizar la idempotencia del pipeline.

### [🔹 Fase 5: Reporting Data Layer (RDL) e Inteligencia Artificial ](docs/STAGE_04.md)

* **Materialización Final:** Creación de la tabla de hechos de reporteo optimizada con lógica de negocio desde GCS.
* **Implementación de IA (BigQuery ML):** Desarrollo de un modelo predictivo ARIMA_PLUS para forecast de ventas a 30 días.
* **Capa de Semántica: Diseño de una Vista Maestra de Analítica que unifica datos históricos y predicciones en una sola fuente de verdad.
* **Visualización:** Integración con Looker Studio para la entrega de dashboards ejecutivos con análisis de tendencia.


## 🛠️ Tecnologías
`Docker` | `PostgreSQL` | `Apache Airflow` | `Python` | `Google BigQuery`| `BigQuery ML`| `Looker Studio`


### 📈 Impacto del Proyecto

Este pipeline transforma datos crudos dispersos en una fuente de verdad centralizada en la nube, permitiendo:

* Reducción de Latencia: Automatización de la carga de datos sin intervención manual.
* Seguridad: Aislamiento de credenciales y cumplimiento de mejores prácticas de DevOps.
* Analítica Avanzada: Preparación de los datos para modelos de Machine Learning y dashboards ejecutivos.
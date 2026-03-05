# 🛒 Manual de Ensamblaje: eCommerce Data Pipeline (Etapa 1)

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
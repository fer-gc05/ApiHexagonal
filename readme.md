# API Hexagonal con FastAPI

Este proyecto implementa una API RESTful utilizando la arquitectura hexagonal con FastAPI, MySQL y SQLAlchemy.

## Características
- **Arquitectura hexagonal**: separación de capas de dominio, aplicación e infraestructura.
- **Base de datos**: MySQL con SQLAlchemy como ORM y Alembic para migraciones.
- **Autenticación**: Manejo de usuarios con autenticación basada en JWT.
- **Pruebas**: Pruebas unitarias con `pytest`.
- **Gestión de secretos**: Configuración segura mediante variables de entorno.

## Requisitos
- Python 3.10+
- MySQL

## Instalación

1. Clonar el repositorio:
   ```sh
   git clone https://github.com/fer-gc05/ApiHexagonal.git
   cd ApiHexagonal
   ```
2. Crear y activar un entorno virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Configurar el archivo de entorno:
   ```sh
   cp .env.example .env
   ```
   Editar `.env` con las credenciales de MySQL.

5. Ejecutar migraciones:
   ```sh
   alembic upgrade head
   ```
6. Iniciar el servidor:
   ```sh
   uvicorn main:app --reload
   ```

## Uso
- Acceder a la documentación interactiva en `http://127.0.0.1:8000/docs`.
- Gestionar usuarios, posts y comentarios mediante las rutas de la API.


## Licencia
Este proyecto está bajo la licencia MIT.


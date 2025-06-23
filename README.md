# MiGestorPro-backend

Este es el backend de **MiGestorPro**, un sistema de gestión creado con Django y Django REST Framework. Está diseñado para facilitar el manejo de clientes y servicios desde una API RESTful.

## 🚀 Tecnologías usadas

- [Django 5.2.3](https://www.djangoproject.com/)
- [Django REST Framework 3.16.0](https://www.django-rest-framework.org/)
- [PyMySQL 1.1.1](https://pymysql.readthedocs.io/en/latest/) – Conexión con MySQL
- [python-decouple 3.8](https://pypi.org/project/python-decouple/) – Manejo de variables de entorno

## 📦 Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/jhonzuloetadev/MiGestorPro-backend.git
   cd MiGestorPro-backend


2. Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows


3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt


4. Crea un archivo .env en la raíz del proyecto (usa el .env.example como referencia)

5. Ejecuta las migraciones:

    ```bash
    python manage.py migrate

6. Inicia el servidor:

    ```bash
    python manage.py runserver


🧪 Endpoints disponibles
    
    ```bash
    GET /api/clients/ – Listar clientes

    POST /api/clients/ – Crear cliente

    PUT /api/clients/<id>/ – Actualizar cliente

    DELETE /api/clients/<id>/ – Eliminar cliente
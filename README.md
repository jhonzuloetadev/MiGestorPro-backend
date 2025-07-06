# MiGestorPro-backend

Este proyecto corresponde al backend de **MiGestorPro**, un sistema de gesti\ón construido con Django y Django REST Framework. Proporciona una API RESTful para administrar clientes y servicios.

## ✨ Tecnologías usadas

- [Django 5.2.3](https://www.djangoproject.com/)
- [Django REST Framework 3.16.0](https://www.django-rest-framework.org/)
- [PyMySQL 1.1.1](https://pymysql.readthedocs.io/en/latest/) – Conexi\ón con MySQL
- [python-decouple 3.8](https://pypi.org/project/python-decouple/) – Manejo de variables de entorno

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/jhonzuloetadev/MiGestorPro-backend.git
cd MiGestorPro-backend
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno. Copia `mi_gestor/.env.example` a `.env` y ajusta los valores según tu configuración de base de datos.

5. Aplica las migraciones de la base de datos:

```bash
python manage.py migrate
```

6. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

La API quedará disponible en `http://localhost:8000/`.

## 💻 Uso

### Endpoints de clientes

- `GET /api/clients` – Listar clientes.
- `POST /api/clients/create` – Crear un cliente.
- `PUT /api/clients/<id>/update` – Actualizar un cliente.
- `DELETE /api/clients/<id>/delete` – Eliminar un cliente.


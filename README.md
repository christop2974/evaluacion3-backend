# PNK Inmobiliaria - Evaluación Sumativa 2

Aplicación web desarrollada con Django para gestionar propiedades, solicitudes de visita y consejos inmobiliarios mediante base de datos relacional, Django ORM y Django Admin.

## Ejecución local

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
pip install -r requirements.txt
```

Para probar rápidamente en SQLite, no crees `.env` o usa `DB_ENGINE=sqlite`.

```bash
python manage.py migrate
python manage.py cargar_propiedades
python manage.py createsuperuser
python manage.py runserver
```

- Sitio: http://127.0.0.1:8000/
- Administración: http://127.0.0.1:8000/admin/
- Panel de propiedades: http://127.0.0.1:8000/panel/

## MySQL en EC2

Copia `.env.example` como `.env` y completa las credenciales. En `.env` usa `DB_ENGINE=mysql`.

```bash
python manage.py migrate
python manage.py cargar_propiedades
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

La configuración sensible queda fuera del código mediante variables de entorno.

## GitHub y EC2

```bash
git clone URL_DEL_REPOSITORIO
cd "proyeco back end inmobiliaria/proyecto back end/prueba"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Para producción se debe usar un servidor WSGI/ASGI apropiado y configurar el dominio/IP en `ALLOWED_HOSTS`.

## Evidencias sugeridas

- Django Admin con creación, edición, eliminación y búsqueda.
- Migraciones ejecutadas.
- Tablas y registros en phpMyAdmin.
- EC2 con Linux, Python, entorno virtual y proyecto ejecutándose.
- Repositorio GitHub y `git log`.
- Capturas de la interfaz con los botones Agregar, Modificar, Eliminar y Buscar.
# ev2_end
# ev2_end


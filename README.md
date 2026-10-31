# PNK Inmobiliaria — Evaluación Sumativa 3

Aplicación Django para publicación de propiedades, asesoría inmobiliaria y solicitudes de visita. Se conserva el diseño visual de PNK y se agrega gestión desde Django Templates, autenticación por grupos, recuperación de contraseña y permisos diferenciados. Las operaciones del sistema no dependen de Django Admin.

## Funcionalidades agregadas

- Inicio y cierre de sesión con autenticación de Django.
- Perfiles `Administrador`, `Supervisor` y `Administrativo`, configurados por grupos.
- Dashboard adaptado al perfil autenticado.
- Gestión de usuarios desde la interfaz (Administrador).
- Recuperación de contraseña con token seguro de Django y enlace enviado por correo.
- Mantenedor CRUD de Propiedades.
- Mantenedor CRUD de Consejos inmobiliarios.
- Transacción de Solicitud de Visita relacionada mediante `ForeignKey` con Propiedad.
- Búsqueda de propiedades, consejos, usuarios y solicitudes.
- Django ORM, migraciones y variables de entorno para SQLite local o MySQL.

## Instalación local (Windows)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Para usar SQLite local, en `.env` configura `DB_ENGINE=sqlite`, `DEBUG=True` y `ALLOWED_HOSTS=127.0.0.1,localhost`. Luego ejecuta:

```bash
python manage.py migrate
python manage.py cargar_propiedades
python manage.py configurar_perfiles
python manage.py createsuperuser
python manage.py runserver
```

El superusuario puede entrar a la interfaz y tiene acceso global. Para crear usuarios con perfiles desde la página, entra a `/cuentas/usuarios/` con un usuario del grupo Administrador. También puedes crear usuarios desde el formulario de la interfaz.

- Sitio: http://127.0.0.1:8000/
- Inicio de sesión: http://127.0.0.1:8000/cuentas/login/
- Dashboard: http://127.0.0.1:8000/cuentas/dashboard/
- Recuperación de contraseña: http://127.0.0.1:8000/cuentas/password-reset/
- Mantenedor de propiedades: http://127.0.0.1:8000/panel/
- Mantenedor de consejos: http://127.0.0.1:8000/asesoria/gestion/consejos/
- Solicitudes de visita: http://127.0.0.1:8000/gestion/visitas/

## Perfiles y restricciones

- **Administrador:** gestión de usuarios, acceso completo a mantenedores y transacciones, eliminación de registros.
- **Supervisor:** puede crear y modificar propiedades/consejos y consultar solicitudes; no puede eliminar registros ni administrar usuarios.
- **Administrativo:** consulta mantenedores y solicitudes; no puede ejecutar operaciones críticas.

Ejecuta `python manage.py configurar_perfiles` después de migrar para crear los grupos y asignar permisos. A continuación, asigna cada usuario al grupo correspondiente desde el formulario de creación de usuarios.

## Recuperación de contraseña por correo

En local, si no configuras SMTP, Django usa el backend de consola y muestra el correo en la terminal para probar el token y enlace. Para demostrar recepción real de correo, configura en `.env` los valores `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` y `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`. En Gmail utiliza una contraseña de aplicación, no la contraseña normal de la cuenta. No subas `.env` a GitHub. En AWS verifica el acceso de salida al servidor SMTP y usa credenciales propias.

## MySQL en AWS EC2

Configura `.env` con `DB_ENGINE=mysql`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST=127.0.0.1` y `DB_PORT=3306`. Instala dependencias y ejecuta:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_propiedades
python manage.py configurar_perfiles
python manage.py collectstatic --noinput
```

En producción, define `DEBUG=False`, una `SECRET_KEY` aleatoria, `ALLOWED_HOSTS` con la IP/dominio real y despliega con un servidor WSGI/ASGI como Gunicorn detrás de Apache/Nginx.

## GitHub

El archivo `.gitignore` excluye `.env`, entornos virtuales, bases de datos SQLite y archivos temporales. Mantén un historial de commits incremental y no subas contraseñas SMTP ni credenciales de base de datos.

## Evidencias sugeridas para la evaluación

1. Login y logout.
2. Recuperación de contraseña, correo recibido, enlace, cambio de contraseña e inicio de sesión con la nueva clave.
3. Dashboard con cada uno de los tres perfiles y prueba de una ruta restringida.
4. CRUD de Propiedades y CRUD de Consejos (crear, listar, buscar, modificar y eliminar según el rol).
5. Solicitud de visita desde el detalle de una propiedad y registro visible en el mantenedor de solicitudes.
6. Tablas, claves y relaciones de la base de datos.
7. Aplicación funcionando desde EC2 y repositorio GitHub con commits.
8. Prompts de IA utilizados y evidencia de su aplicación práctica.

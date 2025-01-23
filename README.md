#  Quadra - Python Flask Web App
# Plataforma de Puestos de Comida

**Quadra** es una aplicación web donde los usuarios pueden localizar, calificar y comentar puestos de comida. Los usuarios pueden agregar nuevos puestos con una ubicación georeferenciada, compartir reseñas, y calificar los puestos de comida existentes. El proyecto está construido utilizando Flask, SQLAlchemy y SQLite para gestionar la base de datos.

## Funcionalidades

- **Autenticación**: Los usuarios pueden registrarse e iniciar sesión.
- **Agregar Puestos de Comida**: Los usuarios pueden añadir nuevos puestos de comida con su ubicación, descripción y foto.
- **Calificaciones y Reseñas**: Los usuarios pueden calificar y agregar comentarios a los puestos de comida.
- **Visualización de Puestos**: Los usuarios pueden ver una lista de puestos de comida y acceder a los detalles de cada puesto.

  
## Estructura del Proyecto
```
Quadra/
│
├── website/                  # Directorio principal de la aplicación
│   ├── __init__.py           # Inicializa la aplicación y registra los Blueprints
│   ├── auth.py               # Rutas y lógica de autenticación
│   ├── models.py             # Modelos de la base de datos (User, FoodStall, Review)
│   ├── views.py              # Vistas y lógica principal de la aplicación
│   ├── food_stalls.py        # Rutas para gestión de puestos de comida
│   └── templates/            # Archivos HTML
│       ├── login.html        # Plantilla para iniciar sesión
│       ├── sign_up.html      # Plantilla para el registro
│       ├── add_food_stall.html # Plantilla para agregar un nuevo puesto
│       ├── food_stall_detail.html # Plantilla para ver los detalles del puesto
│
├── migrations/               # Migraciones de la base de datos
├── requirements.txt          # Dependencias del proyecto
├── main.py                   # Punto de entrada de la aplicación
└── README.md                 # Este archivo
```
## Tecnologías Utilizadas

* **Backend:** Flask, Flask-SQLAlchemy, fask-Login, Wekzeug
* **Base de Datos:** SQLite
* **Frontend:** HTML/Jinja2, CSS, Javascrpt

## Modelos de Base de Datos

>User: Almacena los usuarios registrados.
>FoodStall: Almacena los puestos de comida subidos por los usuarios.
>Review: Almacena las reseñas y calificaciones de los puestos.


## Instalación y Configuración

Clonar el repositorio:

```
git clone https://github.com/rodrigo2311037/pythonflaskwebappQuadra.git
cd Quadra
```
Crear entorno virtual (opcional pero recomendado):
```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
Instalar las dependencias:
```
pip install -r requirements.txt
```
Inicializar la base de datos:
```
flask db init
flask db migrate
flask db upgrade
```
Correr la aplicación:
```
python main.py
```
La aplicación estará disponible en http://127.0.0.1:5000/.



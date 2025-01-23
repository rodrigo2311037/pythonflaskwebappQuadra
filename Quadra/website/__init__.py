# Esta estructura de archivo hace que la carpeta website se convierta en un paquete de python, y asi poder hacer importaciones y demás.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "database.db"

# Inicializar Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'holayosoyrorry' # Encripta las cookies y data de sesion, aunque en fase de desarrollo no es usada
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    migrate = Migrate(app, db)

    # Registro de Blueprints para las vistas y la autenticación
    from .views import views
    from .auth import auth
    from .food_stalls import food_stalls  # importa el blueprint de puestos de comida


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(food_stalls, url_prefix='/')  # Registra el blueprint


    # Modelos y creación de la base de datos
    from .models import User, Note, FoodStall, Review
    
    with app.app_context():
        db.create_all()

    # Gestión de inicio de sesión
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Esta función crea la base de datos si no existe.
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

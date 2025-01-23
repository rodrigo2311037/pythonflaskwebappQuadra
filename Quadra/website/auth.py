from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ## significa que desde  __init__.py importa db
from flask_login import login_user, login_required, logout_user, current_user

# Creación del blueprint
auth = Blueprint('auth', __name__)

# Ruta de Login
@auth.route('/login', methods=['GET', 'POST']) # Metodo POST, verifica email y contraseña. Credenciales correctas=inicia sesion y redirige a la pagina principal
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Inicio de Sesión Exitoso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Contraseña Incorrecta, intenta de nuevo.', category='error')
        else:
            flash('Email no existe.', category='error')

    return render_template("login.html", user=current_user)

# Ruta de Log out
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Ruta de Registro = Sign Up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email ya existe.', category='error')
        elif len(email) < 4:
            flash('Email tiene que ser mayor a 3 letras.', category='error')
        elif len(first_name) < 2:
            flash('Nombre tiene que ser mayor que 1 letra.', category='error')
        elif password1 != password2:
            flash('Contraseñas no\' coinciden.', category='error')
        elif len(password1) < 7:
            flash('Contraseña debe tener al menos 7 letras.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Cuenta Creada!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

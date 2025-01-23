from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import FoodStall, Review
from . import db
from flask_login import current_user, login_required

# Definir el blueprint
food_stalls = Blueprint('food_stalls', __name__)

# Ruta para ver todos los puestos de comida
@food_stalls.route('/food-stalls')
def view_food_stalls():
    food_stalls_list = FoodStall.query.all()  # Obtener todos los puestos de comida

    return render_template('food_stalls_list.html', food_stalls=food_stalls_list, user=current_user)  # Se pasa la lista de puestos de comida

# Ruta para ver detalles de un puesto de comida
@food_stalls.route('/food-stall/<int:id>')
def view_food_stall(id):
    stall = FoodStall.query.get_or_404(id)  # Aquí sí se pasa el id correctamente
    return render_template('food_stall_detail.html', food_stall=stall, user=current_user)

# Ruta para calificar y comentar un puesto
@food_stalls.route('/rate-food-stall/<int:id>', methods=['POST'])
@login_required
def rate_food_stall(id):
    stall = FoodStall.query.get(int(id))
    if stall is None:
        flash('Puesto de comida no encontrado.', category='error')
        return redirect(url_for('food_stalls.view_food_stalls'))

    rating = request.form.get('rating')
    comment = request.form.get('comment')

    new_review = Review(
        rating=rating,
        comment=comment,
        user_id=current_user.id,
        foodstall_id=stall.id
    )
    db.session.add(new_review)
    db.session.commit()

    flash('Reseña añadida exitosamente!', category='success')
    return redirect(url_for('food_stalls.view_food_stall', id=stall.id))

# Ruta para subir un nuevo puesto de comida
@food_stalls.route('/add-food-stall', methods=['GET', 'POST'])
@login_required
def add_food_stall():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        image_url = request.form.get('image_url')

        if len(name) < 1 or len(description) < 1:
            flash('Por favor complete todos los campos.', category='error')
        else:
            new_stall = FoodStall(
                name=name,
                description=description,
                latitude=latitude,
                longitude=longitude,
                image_url=image_url,
                user_id=current_user.id
            )
            db.session.add(new_stall)
            db.session.commit()
            flash('Puesto de comida añadido con éxito!', category='success')
            return redirect(url_for('food_stalls.view_food_stalls'))

    return render_template('add_food_stall.html', user=current_user)

# Este archivo contiene las rutas, excepto lo relacionado con la autenticacin de usuario, eso esta en auth (authentication)
from flask import Blueprint, render_template, request, flash, jsonify, request, url_for, flash, redirect
from flask_login import login_required, current_user
from .models import Note, FoodStall, Review
from . import db
import json

# Define que este archivo es un Blueprint de la aplicacion para manejar las rutas.
views = Blueprint('views', __name__)

# Ruta de inicio ( home )
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note') # Obtiene la nota del HTML 

        if len(note) < 1:
            flash('Nota demasiado corta!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #prove el esquema para la nota 
            db.session.add(new_note) #añadir la nota a la DB
            db.session.commit()
            flash('Nota añadida!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

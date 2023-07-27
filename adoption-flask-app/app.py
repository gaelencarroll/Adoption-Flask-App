from flask import Flask, render_template, redirect, jsonify, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chickens'

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route('/')
def pets_list():
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def pets_add():
    add_form = AddPetForm()

    if add_form.validate_on_submit():
        data = {k: v for k, v in add_form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('pets_list'))

    else:
        return render_template('add_form.html', add_form=add_form)


@app.route('<int:pet_id>', methods=['GET', 'POST'])
def pets_edit(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    edit_form = EditPetForm(obj=pet)

    if edit_form.validate_on_submit():
        pet.notes = edit_form.notes.data
        pet.available = edit_form.available.data
        pet.photo_url = edit_form.photo_url.data
        db.session.commit()
        return redirect(url_for('pets_list'))

    else:
        return render_template('edit_form.html', edit_form=edit_form, pet=pet)

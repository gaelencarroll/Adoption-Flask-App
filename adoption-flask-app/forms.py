from flask_wtf import FlaskForm
from wtfforms import SelectField, IntegerField, StringField, TextareaField, BooleanField
from wtfforms.validators import InputRequired, Length, NumberRange, Optional, URL


class AddPetForm(FlaskForm):
    name = StringField(
        'Pet Name',
        validators=[InputRequired()]
    )

    species = SelectField(
        'Species',
        choices=[('cat', 'Cat'), ('dog', 'Dog'),
                 ('bird', 'Bird'), ('bunny', 'Bunny')]
    )

    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()]
    )

    age = IntegerField(
        'Age',
        validators=[Optional(), NumberRange(min=0, max=100)]
    )

    notes = TextareaField(
        'Notes',
        validators=[Optional()]
    )


class EditPetForm(FlaskForm):
    photo_url = StringField(
        'Photo URL'
        validators=[Optional(), URL()]
    )

    notes = TextareaField(
        'Notes',
        validators=[Optional()]
    )

    available = BooleanField('Available?')

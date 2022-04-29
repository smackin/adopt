from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddNewPetForm(FlaskForm):
    
    name = StringField(
        "Pet Name", 
        validators=[InputRequired()])
    
    species = SelectField(
        "Species",
        choices=[('cat', "Cat"), ('dog', 'Dog'), ('turle', "Turtle"), ('monkey', 'Monkey')])
    photo_url = StringField(
        "Image URL", 
        validators=[Optional(), URL()]
        )
    
    age = IntegerField(
        "Pet Age", 
        validators=[Optional(), NumberRange(min=0, max=30)],
        )
    notes = TextAreaField("Notes")
    
    class EditPetForm(FlaskForm):
        """form to edit existing Pet """
        
        photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
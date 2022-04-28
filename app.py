from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet, connect_db
from forms import AddNewPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Top Secret'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

def connect_db(app):
    db.app = app
    db.init_app(app) 

app.route('/')
def show_all_pets_list():
    """show page that renders all pets present in db"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/pet/new',  methods=["GET", "POST"])
def add_pet():
    form = AddNewPetForm()
    return render_template('add_pet_form.html', form=form)
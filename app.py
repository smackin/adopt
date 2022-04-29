from flask import Flask, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet, connect_db
from forms import AddNewPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.debug =True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'Top Secret'

connect_db(app)

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods=['GET'])
def list_pets():
    """show page that renders all pets present in db"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/pet/new',  methods=["GET","POST"])
def add_pet():
    print("before new form check!!!!!!!!!!!!!!!!!")
    form = AddNewPetForm()
    print("After new form check $$$$$$$$$$$$$$")
    if form.validate_on_submit():
        print("inside of if form valid ^^^^^^^")
        name=form.name.data, 
        species=form.species.data, 
        photo_url=form.photo_url.data, 
        age=form.age.data, 
        notes=form.notes.data
        breakpoint()
        new_pet= Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} has been added to the Adoption List!')
        return redirect('/')
    
    else: 
        print("were now in the else!!!!!!!!!!!!!")
        return render_template('add_pet_form.html', form=form)



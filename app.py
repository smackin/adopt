from flask import Flask, jsonify, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet, connect_db
from forms import AddNewPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.debug =True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'Top Secret'

connect_db(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
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
        new_pet= Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} has been added to the Adoption List!')
        return redirect('/')
    
    else: 
        print("were now in the else!!!!!!!!!!!!!")
        return render_template('add_pet_form.html', form=form)



@app.route('/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):
    """Edit Existing Pet"""
    
    pet= Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated.")
        return redirect(url_for('list_pets'))
    
    else: 
        return render_template("pet_edit_form.html", form=form, pet=pet)

@app.route('/pets/<int:id>', methods=['GET',])
def api_get_pet(id):
    """Return and display info about Pet"""
    
    pet = Pet.query.get_or_404(id)
    info = {"name": pet.name, "age": pet.age}
    
    return jsonify(info)

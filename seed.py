from models import Pet, db
from app import app

#Create Tables

def create_table():
    db.drop_all()
    db.create_all()
    
#Drop and recreate table, hoping to eliminate duplicates in the db.  

create_table()

pet1 = Pet(name='Sammie', species='Dog', photo_url='https://cf.ltkcdn.net/dogs/images/orig/284637-1600x1066-german-shepherd-characteristics.jpg', age=2, notes='Friendly, fun and super active!  Looking for a loving FURever home!', available=True)

pet2 = Pet(name='Lily', species='Dog', photo_url='https://assets.orvis.com/is/image/orvisprd/french-bulldog?wid=1023&src=is($object$:7-3)', age=11, notes='Senior Dog looking for quiet family. ', available=True)

pet3 = Pet(name='Gracie', species='Cat', photo_url='https://cdn.petpress.net/wp-content/uploads/2020/03/12033817/black-and-white-male-cat-names.jpg', age=1, notes='Very cute and spunky, always trying to get into trouble', available=True)

pet4 = Pet(name='Oreo', species='Cat', photo_url='https://static.boredpanda.com/blog/wp-content/uploads/2014/08/cat-black-and-white-photography-fb.jpg', age=3, notes='Loves to snuggle and eat snacks.  Also loves to watch the neighborhood out the window all day.', available=True)

pet5 = Pet(name='Jack', species='Turtle', photo_url='https://www.everythingreptiles.com/wp-content/uploads/2020/07/Pet-Turtle-Names.jpg', age=2, notes='Does not fight crime, does not live underground with 3 other turtles.', available=True)

pet7 = Pet(name='Marcel', species='Monkey', photo_url='https://petkeen.com/wp-content/uploads/2021/06/capuchin-in-the-tree.jpeg', age=7, notes='curious and cute, active and playful, looking for a family with young kids.', available=True)

db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet7])
db.session.commit()


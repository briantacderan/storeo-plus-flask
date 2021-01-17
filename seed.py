from app import app, db
from models import User, Album, Photo

# ADMIN

a1 = User(username="edna_mode", email='edna@example.com')
a2 = User(username="jack_sparrow", email='jack@example.com')

# USERS

u1 = User(username='carlos_bueno', email='carlos@email.com')
u2 = User(username='freida_bueno', email='freida@email.com')
u3 = User(username='julian_bueno', email='julian@email.com')
u4 = User(username='joe_young', email='mighty@example.com')



users = [a1, a2, u1, u2, u3, u4]
passwords = ['incredibles', 'caribbean', 'Carlos1', 'Freida1', 'Julian1', 'charlize']
for i in range(len(users)):
    new = users[i]
    new.set_password(passwords[i])
    db.session.add(new)
    db.session.commit()


               
# COLLECTIONS

baseball = Album(title="Baseball", image="https://content.codecademy.com/courses/rails-auth/img/baseball-1.jpg", user_id=3)

p1 = Photo(caption="Best hitter on the team.", image="https://content.codecademy.com/courses/rails-auth/img/baseball-2.jpg", album_id=1)
p2 = Photo(caption="Defense, Defense!", image="https://content.codecademy.com/courses/rails-auth/img/baseball-3.jpg", album_id=1)
p3 = Photo(caption="Double play", image="https://content.codecademy.com/courses/rails-auth/img/baseball-4.jpg", album_id=1)
p4 = Photo(caption="All about that bunt", image="https://content.codecademy.com/courses/rails-auth/img/baseball-5.jpg", album_id=1)



birthday = Album(title="Birthday", image="https://content.codecademy.com/courses/rails-auth/img/birthday-1.jpg", user_id=4)

p5 = Photo(caption="Turning 21", image="https://content.codecademy.com/courses/rails-auth/img/birthday-2.jpg", album_id=2)
p6 = Photo(caption="Bringing in the style", image="https://content.codecademy.com/courses/rails-auth/img/birthday-3.jpg", album_id=2)
p7 = Photo(caption="Dinner with friends", image="https://content.codecademy.com/courses/rails-auth/img/birthday-4.jpg", album_id=2)
p8 = Photo(caption="Cake", image="https://content.codecademy.com/courses/rails-auth/img/birthday-5.jpg", album_id=2)



hiking = Album(title="Hiking", image="https://content.codecademy.com/courses/rails-auth/img/Hiking-1.jpg", user_id=5)

p9 = Photo(caption="Breakfast of champions", image="https://content.codecademy.com/courses/rails-auth/img/Hiking-2.jpg", album_id=3)
p10 = Photo(caption="Eagle's Cliff", image="https://content.codecademy.com/courses/rails-auth/img/hiking-3.jpg", album_id=3)
p11 = Photo(caption="Steepest part of the mountain", image="https://content.codecademy.com/courses/rails-auth/img/hiking-4.jpg", album_id=3)
p12 = Photo(caption="We made it!", image="https://content.codecademy.com/courses/rails-auth/img/Hiking-5.jpg", album_id=3)



pets = Album(title="Pets", image="https://content.codecademy.com/courses/rails-auth/img/pet-2.jpg", user_id=6)

p13 = Photo(caption="Rover's first bed.", image="https://content.codecademy.com/courses/rails-auth/img/pet-2.jpg", album_id=4)
p14 = Photo(caption="Out for a walk.", image="https://content.codecademy.com/courses/rails-auth/img/pet-3.jpg", album_id=4)
p15 = Photo(caption="Spotted a rabbit", image="https://content.codecademy.com/courses/rails-auth/img/pet-4.jpg", album_id=4)
p16 = Photo(caption="Meeting a kitten", image="https://content.codecademy.com/courses/rails-auth/img/pet-5.jpg", album_id=4)



wedding = Album(title="Wedding", image="https://content.codecademy.com/courses/rails-auth/img/wedding-1.jpg", user_id=2)

p17 = Photo(caption="Flowers", image="https://content.codecademy.com/courses/rails-auth/img/wedding-2.jpg", album_id=5)
p18 = Photo(caption="Setting up the morning of.", image="https://content.codecademy.com/courses/rails-auth/img/wedding-3.jpg", album_id=5)
p19 = Photo(caption="Delicious Cake", image="https://content.codecademy.com/courses/rails-auth/img/wedding-4.jpg", album_id=5)
p20 = Photo(caption="Happy moments!", image="https://content.codecademy.com/courses/rails-auth/img/wedding-5.jpg", album_id=5)


               
albums = [baseball, birthday, hiking, pets, wedding]
for i in range(len(albums)):
    new = albums[i]
    db.session.add(new)
    db.session.commit()      
               
photos = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
for i in range(len(photos)):
    new = photos[i]
    db.session.add(new)
    db.session.commit()

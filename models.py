from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    joined_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    albums = db.relationship('Album', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Album(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    image = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    photos = db.relationship('Photo', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Album {}>'.format(self.title)
    
    
class Photo(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(140))
    image = db.Column(db.String(140))
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return '<Photo {}>'.format(self.caption)
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

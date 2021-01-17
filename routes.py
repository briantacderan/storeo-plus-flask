from app import app, db
from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from models import User, Album, Photo
from forms import RegistrationForm, LoginForm, AlbumForm, PhotoForm
from werkzeug.urls import url_parse


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        if form.remember_me.data:
            login_user(user, remember=True)
        else:
            login_user(user)
        flash('You were successfully logged in')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('albums', username=current_user.username)
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/')
def index():
    return render_template('landing_page.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<username>/albums')
@login_required
def albums(username):
    user = User.query.filter_by(username=username).first()
    albums = Album.query.all()
    if albums is None:
        albums = []
    return render_template('user.html', user=user, albums=albums)


@app.route('/user/<username>/album/new', methods=['GET', 'POST'])
@login_required
def post_album(username):
    user = User.query.filter_by(username=username).first()
    form = AlbumForm()
    if request.method == 'POST' and form.validate():
        new_album = Album(title=form.title.data, 
                          image=form.image.data, 
                          user_id=current_user.id)
        db.session.add(new_album)
        db.session.commit()
        flash('Album successfully created')
        album = Album.query.filter_by(title=new_album.title).first()
        return redirect(url_for('photos', 
                                username=current_user.username,
                                album_id=album.id))
    return render_template('new_album.html', user=user, form=form)


@app.route('/user/<username>/album/<album_id>/delete', methods=['GET', 'DELETE'])
@login_required
def delete_album(username, album_id):
    user = User.query.filter_by(username=username).first()
    album = Album.query.filter_by(id=album_id).first()
    photos = Photo.query.filter_by(album_id=album_id)
    if photos is None:
        photos = []
    else:
        for photo in photos:
            db.session.delete(photo)
            db.session.commit()
    db.session.delete(album)
    db.session.commit()
    flash('Album successfully deleted')
    return redirect(url_for('albums', 
                            username=current_user.username))


@app.route('/user/<username>/album/<album_id>')
@login_required
def photos(username, album_id):
    user = User.query.filter_by(username=username).first()
    album = Album.query.filter_by(id=album_id).first()
    photos = Photo.query.filter_by(album_id=album_id)
    if photos is None:
        photos = []
    return render_template('album.html', user=user, album=album, photos=photos)


@app.route('/user/<username>/album/<album_id>/photo/new', methods=['GET', 'POST'])
@login_required
def post_photo(username, album_id):
    user = User.query.filter_by(username=username).first()
    album = Album.query.filter_by(id=album_id).first()
    form = PhotoForm()
    if request.method == 'POST' and form.validate():
        new_photo = Photo(caption=form.caption.data, image=form.image.data, album_id=album.id)
        db.session.add(new_photo)
        db.session.commit()
        flash('Photo successfully uploaded')
        return redirect(url_for('photos', 
                                username=username,
                                album_id=album_id))
    return render_template('new_photo.html', user=user, album=album, form=form)


@app.route('/user/<username>/album/<album_id>/photo/<id>/delete', methods=['GET', 'DELETE'])
@login_required
def delete_photo(username, album_id, id):
    user = User.query.filter_by(username=username).first()
    album = Album.query.filter_by(id=album_id).first()
    photo = Photo.query.filter_by(id=id).first()
    db.session.delete(photo)
    db.session.commit()
    flash('Photo successfully deleted')
    return redirect(url_for('photos', 
                            username=username,
                            album_id=album_id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

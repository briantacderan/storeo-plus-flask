from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


# to initialize database instance

# $ py
# >>> from app import db
# >>> db.create_all()
# >>> exit()
# py seed.py


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('MAILGUN_SECRET_KEY', None)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storeo_flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

port = int(os.environ.get("PORT", 5000))

login = LoginManager()
login.login_view = 'login'
login.init_app(app)

import routes, models

if __name__ == '__main__':
    app.run(debug=True)

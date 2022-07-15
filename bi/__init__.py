from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    ENV = 'dev'

    if ENV == 'prod':
     app.config['SECRET_KEY'] = 'bibciejbdxhasxhajabchbc'
     app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/butterfly_blog"
    else:
        app.config['SECRET_KEY'] = 'bibciejbdxhasxhajabchbc'
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            "postgresql://oxxlnvxbjchtkc:a5244f271f3497e7b18bffbbcb38e6613d372bdd708fc982816d41bcd95b9dc9@ec2-52-86-56-90.compute-1.amazonaws.com:5432/d5ufnd1qarm2lr"


    db.init_app(app)
    mail.init_app(app)



    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app
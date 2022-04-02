from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    ENV = 'prod'

    if ENV == 'dev':
     app.config['SECRET_KEY'] = 'bibciejbdxhasxhajabchbc'
     app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/butterfly_blog"
    else:
        app.config['SECRET_KEY'] = 'bibciejbdxhasxhajabchbc'
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            "postgresql://gppnardpcpltbm:fc4c9dcd6d6f64048d6781d667e530545283a7e59f7fb545cf02a4bb897aaada@ec2-44-194-4-127.compute-1.amazonaws.com:5432/d54a03ddvlhch6"


    db.init_app(app)
    mail.init_app(app)



    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app
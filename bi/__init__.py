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
        app.config['SQLALCHEMY_DATABASE_URI'] = " postgresql://boskaadjldmhld:b6c15860778013f427a46c97602e01193062c3c014feae6927f00ff8f7b4b593@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d13c2fqfr1tkcq"


    db.init_app(app)
    mail.init_app(app)



    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app
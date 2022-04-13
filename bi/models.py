from . import db

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, unique=True)
    author = db.Column(db.String(50))
    date = db.Column(db.String(15))
    title = db.Column(db.String(100))
    path = db.Column(db.String(100))
    content = db.Column(db.Text)

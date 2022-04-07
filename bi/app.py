import os.path
from flask import *
from datetime import datetime
from .models import Blogpost
from . import *
import random
from .s3 import upload_file
from werkzeug.utils import secure_filename
import smtplib
from email.message import EmailMessage
from sqlalchemy import desc

app = Blueprint('app', __name__)





@app.route('/')
def index():
    posts = Blogpost.query.order_by(desc(Blogpost.id)).limit(4).all()
    return render_template('index.html', posts=posts)

@app.route('/', methods=['POST'])
def index_post():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    EMAIL_ADDRESS = 'btechinfusion@gmail.com'
    EMAIL_PASSWORD = 'posxvopqfrccjurr'

    msg = EmailMessage()
    msg['subject'] = 'Client Enquiry'
    msg['To'] = EMAIL_ADDRESS

    msg.set_content('This is plain text email')

    msg.add_alternative(f'''
    
    <html>
    <body>
    <h3>New enquiry from {name}, {email}</h3>
    <p>{message}</p>
    </body>
    </html>
    
    ''', subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
         smtp.send_message(msg)


    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = Blogpost.query.order_by(desc(Blogpost.id))
    return render_template('blog.html', posts=posts)

@app.route('/blog/<int:blog_id>', methods=['GET', 'POST'])
def post(blog_id):
    post = Blogpost.query.filter_by(blog_id=blog_id).one()
    posts = Blogpost.query.order_by(desc(Blogpost.id))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        EMAIL_ADDRESS = 'btechinfusion@gmail.com'
        EMAIL_PASSWORD = 'posxvopqfrccjurr'

        msg = EmailMessage()
        msg['subject'] = 'Client Comment'
        msg['To'] = EMAIL_ADDRESS

        msg.set_content('This is plain text email')

        msg.add_alternative(f'''

              <html>
              <body>
              <h3>New enquiry from {name}, {email}</h3>
              <p>{message}</p>
              </body>
              </html>

              ''', subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

    return render_template('blog-single.html', post=post, posts=posts)

@app.route('/poster')
def poster():
    blog_id = random.randint(1, 99)
    date = datetime.now()
    now = date.strftime('%d %b %Y')
    return render_template('poster.html', now=now, blog_id=blog_id)

@app.route('/poster', methods=['POST'])
def poster_post():
   if  request.method == 'POST':
    blog_id = request.form['blog_id']
    author = request.form['author']
    date = request.form['date']
    title = request.form['title']
    content = request.form['content']
    f = request.files['file']


    UPLOAD_FOLDER = f'uploads/{blog_id}'
    os.makedirs(f'{UPLOAD_FOLDER}', exist_ok=True)
    BUCKET = 'ease-invoice'

    f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
    upload_file(f"{UPLOAD_FOLDER}/{f.filename}", BUCKET)

    path = f'https://{BUCKET}.s3.eu-central-1.amazonaws.com/{UPLOAD_FOLDER}/{f.filename}'

    post = Blogpost(blog_id=blog_id,author=author,date=date, title=title, path=path, content=content)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('app.blog'))



   return render_template('poster.html')





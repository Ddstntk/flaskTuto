from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Konrad'}
    posts = [
        {   'author': {'username':'Waldemar'},
            'body': 'Począwszy dzień wpisuję post'
        },
        {
            'author': {'username': 'Józef'},
            'body': 'Zażółć gęźlą jaźń'
         }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Jakub'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'It was really beautifull day'
        },
        {
            'author': {'username': 'Catrin'},
            'body': 'The crime movie was breath taking!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

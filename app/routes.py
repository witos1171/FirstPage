from app import app
from flask import render_template
from app.forms import LoginForm


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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)

from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'TY Li',
        'title': 'Blog Post 1',
        'content': 'Hello World!',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Jenny Hsiao',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html', posts=posts, title='Hey!')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('homepage'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

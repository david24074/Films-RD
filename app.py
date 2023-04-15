from src import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from src.models import User
from src.forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html', movies=[])

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
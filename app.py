from src import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from src.models import User, Movie, Director, Actor
from src.forms import LoginForm, SignupForm

@app.route('/')
def index():
    return render_template('index.html', movies=[], current_user=current_user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():# If the validation fails there is no error
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("Je bent nu ingelogd", "success")
            return redirect(url_for("index"))
        else:
            flash("Er bestaat geen account met deze inlog gegevens", "danger")

    return render_template('login.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        if not form.validate_email(form.email):
            flash("Er bestaat al een gebruiker met dit email addres", "danger")
            return render_template('signup.html', form=form)
        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Account aangemaakt", "success")
        return redirect(url_for("index"))
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!', 'success')
    return redirect(url_for('index'))

@app.route('/movie/<id>')
def movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if not movie:
        return redirect(url_for("index"))
    director = Director.query.filter_by(id=movie.directorid).first()
    actors = Actor.query.filter_by(id=movie.directorid)
    return render_template('film.html', current_user=current_user, movie=movie.__dict__, director=director.__dict__, actors=actors.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
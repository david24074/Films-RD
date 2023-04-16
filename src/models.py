from src import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"User of id {self.id} has email {self.email} and the password hash is {self.password}"

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    directorid = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year_released = db.Column(db.Integer, nullable=False)
    trailerurl = db.Column(db.Text, nullable=False)
    posterurl = db.Column(db.Text, nullable=False)

    def __init__(self, title, directorid, year_released, trailerurl, posterurl):
        self.title = title
        self.directorid = directorid
        self.year_released = year_released
        self.trailerurl = trailerurl
        self.posterurl = posterurl

    def __repr__(self):
        return f"Movie with id {self.id} and is called {self.title} was directed by {self.directorid} and came out in {self.year_released}"
    
class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Actor with id {self.id} is called {self.first_name} {self.last_name}"

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    actor_id = db.Column(db.Integer, nullable=False)
    character_name = db.Column(db.Text, nullable=False)

    def __init__(self, movie_id, actor_id, character_name):
        self.movie_id = movie_id
        self.actor_id = actor_id
        self.character_name = character_name

    def __repr__(self):
        return f"Actor {self.actor_id} has a role in movie {self.movie_id} of which the character is called {self.character_name} and the id of this role is {self.id}"

class Director(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Director with id {self.id} is called {self.first_name} {self.last_name}"

app.app_context().push()
db.create_all()

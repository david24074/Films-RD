from src import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False, index=True)
    password = db.Column(db.Text, nullable=False)

    def __init__(self,email,password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"User has email {self.email} and the password hash is {self.password}"

    def check_password(self, password):
        return check_password_hash(self.password, password)

app.app_context().push()
db.create_all()
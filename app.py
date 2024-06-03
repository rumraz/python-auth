from flask import Flask
from flask_login import LoginManager
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    # Load and return the User object corresponding to the user_id
    return User.get(user_id)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

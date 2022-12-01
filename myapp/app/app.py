from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from flask import Flask
from secrets import token_urlsafe
app = Flask(__name__)


app.config['SECRET_KEY'] = token_urlsafe(16) #Générer une clé au hasard


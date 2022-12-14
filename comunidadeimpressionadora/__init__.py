from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b20ca726fdb39834ea563a475126c8fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'               #login_view -> é como se fosse a página que sera redirecionada quando o login_manager fizer a exigencia
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes # importação feita embaixo porque em routes usa o app, e o app foi criado ali em cima
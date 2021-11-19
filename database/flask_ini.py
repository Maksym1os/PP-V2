from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


import database.blueprints.blpr_user, database.blueprints.blpr_note, database.blueprints.blpr_notelog

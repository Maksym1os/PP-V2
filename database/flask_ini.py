from flask import Flask

app = Flask(__name__)

import database.blueprints.blpr_user


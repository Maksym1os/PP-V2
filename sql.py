import app
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine



app.config["Secret"] = "Secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost/db?host=localhost?port=3306"
# engine = create_engine("mysql+pymysql://root:password@127.0.0.1/db?host=localhost?port=3306")
# engine.connect()



db = SQLAlchemy(app)


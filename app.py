from flask import Flask
from sql import Session, user, note
import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, BigInteger, DateTime, BINARY, func
import sys

app = Flask(__name__)


@app.route("/api/v1/hello-world-2")
def hello_world():
    return 'Hello World 2'


session = Session()

user_inst = note(user_id=1, note_id=2, name="stringName")


print(user_inst)
session.close()

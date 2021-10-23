from flask import Flask
import os

import app
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, BigInteger, DateTime, BINARY, func
import sys

app = Flask(__name__)

engine = create_engine("mysql+pymysql://root:password@127.0.0.1/SimpleNotes")

engine.connect();



@app.route("/api/v1/hello-world-2")
def hello_world():
    return 'Hello World 2'




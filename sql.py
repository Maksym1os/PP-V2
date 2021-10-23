import os

import app
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, BigInteger, DateTime, BINARY, func
import sys

# app.config["Secret"] = "Secret"

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost/db?host=localhost?port=3306"


# SessionFactory = sessionmaker(bind=engine)
#
# Session = scoped_session(SessionFactory)
#
# BaseModel = declarative_base()
#
#
#
#
# class user(BaseModel):
#     __tablename__ = "user"
#
#     user_id = Column(Integer, primary_key=True)
#     username = Column(String)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String)
#     password = Column(String)
#     phone = Column(String)
#     user_status = Column(Integer)
#
#
# class note(BaseModel):
#     note_id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, primary_key=True)
#     name = Column(String)



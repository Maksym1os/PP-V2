# import os
# import pymysql
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, String, BigInteger, DateTime, BINARY, func
import sys

# sys.path.append(r"C:\LABS\PP\lab_6\PP_lab")

engine = create_engine("mysql+pymysql://root:password@127.0.0.1/swagger_notes")

engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()
BaseModel.query = Session.query_property()


# db = SQLAlchemy(app)
#

class user(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45), unique=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(50))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(100))
    phone = Column(VARCHAR(20))

    # def __str__(self):
    #     return f"User ID : {self.id}\n" \
    #            f"First name : {self.first_name}" \
    #            f"Last name : {self.last_name}" \
    #            f"Username : {self.username}\n" \
    #            f"Email : {self.email}\n" \
    #            f"Phone : {self.phone}\n"

    # def __init__(self, id, first_name, password, email, username, last_name, phone, user_status=0):
    #     self.id = id
    #     self.first_name = first_name
    #     self.password = password
    #     self.username = username
    #     self.last_name = last_name
    #     self.phone = phone
    #     self.user_status = user_status
    #     self.email = email

    def __init__(self, id, username, password, user_status=0):
        self.id = id
        self.password = password
        self.username = username
        self.user_status = user_status


class note(BaseModel):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.id))
    name = Column(VARCHAR(50))
    content = Column(VARCHAR(500))
    tag = Column(VARCHAR(20))

    def __init__(self, id, user_id, name, content, tag):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.content = content
        self.tag = tag


class connected_user(BaseModel):
    __tablename__ = "connected_user"
    user_id = Column(Integer, ForeignKey(user.id), primary_key=True)
    note_id = Column(Integer, ForeignKey(note.id), primary_key=True)

    def __init__(self, user_id=None, note_id=None):
        self.user_id = user_id
        self.note_id = note_id


class action(BaseModel):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50))
    content = Column(VARCHAR(500))

    def __init__(self, name, content=""):
        self.name = name
        self.content = content


class note_log(BaseModel):
    __tablename__ = "note_log"
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey(note.id, ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey(user.id, ondelete='CASCADE'))
    action_id = Column(Integer, ForeignKey(action.id, ondelete='CASCADE'))
    date = Column(DateTime, server_default=func.now())

    def __init__(self, note_id, user_id, action_id):
        self.note_id = note_id
        self.user_id = user_id
        self.action_id = action_id

# print(user.query.all())

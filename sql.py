import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, String, BigInteger, DateTime, BINARY, func
import sys

# sys.path.append(r"C:\LABS\PP\lab_6\PP_lab")

engine = create_engine("mysql+pymysql://root:password@127.0.0.1/SimpleNotes")

engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()


class user(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(50))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(45))
    phone = Column(VARCHAR(20))
    user_status = Column(Integer)

    def __str__(self):
        return f"User ID : {self.id}\n" \
               f"First name : {self.first_name}" \
               f"Last name : {self.last_name}" \
               f"Username : {self.username}\n" \
               f"Email : {self.email}\n" \
               f"Phone : {self.phone}\n"

class note(BaseModel):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))


class connected_user(BaseModel):
    __tablename__ = "connected_user"
    user_id = Column(Integer, primary_key=True)
    note_id = Column(Integer, primary_key=True)

class action(BaseModel):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))

class note_log(BaseModel):
    __tablename__ = "note_log"
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    action_id = Column(Integer, primary_key=True)

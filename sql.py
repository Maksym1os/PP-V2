import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, BigInteger, DateTime, BINARY, func
import sys

engine = create_engine("mysql+pymysql://root:password@127.0.0.1/SimpleNotes")

engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()


class user(BaseModel):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)
    user_status = Column(Integer)


class note(BaseModel):
    __tablename__ = "note"
    note_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    name = Column(String)

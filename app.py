from flask import Flask
# from sql import Session, User, note, action, note_log
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


# session = Session()
#
# user_inst = user(id=2, username="user1", first_name="fn", last_name="ln", email="@sth", password="pass", phone="234", user_status=0)
# user_inst2 = user(id=3, username="user2", first_name="fn", last_name="ln", email="@sth", password="pass", phone="234", user_status=0)
#
# note_inst = note(id=23, user_id=user_inst.id, name="someNote")
# note_inst2 = note(id=24, user_id=user_inst2.id, name="someNote")
# note_inst3 = note(id=25, user_id=user_inst2.id, name="someNote")
#
# action = action(id=1, name="s")
# note_log = note_log(id=123, note_id=note_inst.id, user_id=user_inst.id, action_id=action.id)
#
# session.add(user_inst)
# session.add(user_inst2)
# session.commit()
# session.add(note_inst3)
# session.add(note_inst)
# session.add(note_inst2)
# session.commit()
# session.add(action)
# session.commit()
# session.add(note_log)
# session.commit()
#
#
# session.commit()

# print(session.query(user).all())
# session.close()


# alembic revision -m "add models" --autogenerate


import base64
import json

import pytest
from pytest import *

from database.flask_ini import app as fl_app
from database.blueprints.blpr_user import *
from json import *
import os
import tempfile

import pytest

@pytest.fixture
def app():
    yield fl_app

@pytest.fixture
def client(app):
    return app.test_client()



class TestUser:
    temp_token= ""
    def test_user_create(self, client):
        temp = {
            'id':'7',
            'username':'username4',
            'password':'password'
        }
        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/user', headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, data=temp)

        assert response.status_code == 200


    def test_duplicate_key(self, client):
        temp = dict(
            id=1,
            username='username',
            password='password'
        )
        response = client.post('http://localhost:8000/user', headers={'Content-Type': 'application/json'}, data=temp)
        assert response.status_code == 400

    def test_login(self, client):
        credentials = base64.b64encode(b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        # TestUser.temp_token += response.data
        assert response.status_code == 200

    def test_login_failed(self, client):
        credentials = base64.b64encode(
            b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa1").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        assert response.status_code == 401

    def test_get_users(self, client):
        response = client.get('http://localhost:8000/user')
        assert response.status_code == 200

    def test_get_user_by_id(self, client):
        credentials = base64.b64encode(b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        temp = response.json
        response = client.get("http://localhost:8000/user/4", headers={"Authorization": f"Bearer {temp}"})
        assert response.status_code == 200

    def test_get_user_by_id_failed(self, client):
        credentials = base64.b64encode(b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa1").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        assert response.status_code == 401

    def test_get_user_by_id_failed2(self, client):
        credentials = base64.b64encode(b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        assert response.status_code == 200
        temp = response.json
        response = client.get("http://localhost:8000/user/1", headers={"Authorization": f"Bearer {temp}"})
        assert response.status_code == 400

    def test_upd_user_by_Id(self, client):
        credentials = base64.b64encode(
            b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        temp = response.json
        data_t = {
            'first_name': 'NEw'
        }
        data_t = json.dumps(data_t)
        response = client.put("http://localhost:8000/user/4", headers={'Authorization': f"Bearer {temp}",'Content-Type': 'application/json'}, data=data_t)

        assert response.status_code == 200

    def test_upd_user_by_Id_failed(self, client):
        credentials = base64.b64encode(
            b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        temp = response.json
        data_t = {
            'first_name': 'NEw'
        }
        data_t = json.dumps(data_t)
        response = client.put("http://localhost:8000/user/1", headers={'Authorization': f"Bearer {temp}",'Content-Type': 'application/json'}, data=data_t)

        assert response.status_code == 400

    # def test_delete_user_by_Id(self, client):
    #     credentials = base64.b64encode(
    #         b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
    #     response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
    #     temp = response.json
    #
    #
    #     response = client.delete("http://localhost:8000/user/4", headers={'Authorization': f"Bearer {temp}"})
    #
    #     assert response.status_code == 200
    #
    #
    # def test_delete_user_by_Id_failed(self, client):
    #     credentials = base64.b64encode(
    #         b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
    #     response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
    #     temp = response.json
    #
    #
    #     response = client.delete("http://localhost:8000/user/1", headers={'Authorization': f"Bearer {temp}"})
    #
    #     assert response.status_code == 400


class TestNote:
    def test_note_create(self, client):
        credentials = base64.b64encode(
            b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        temp = response.json
        data_t = {
            'id': '1',
            'user_id': '4',
            'name': '12312as',
            'content': 'asdaslkd',
            'tag': 'asdkjashd'
        }
        data_t = json.dumps(data_t)
        response = client.post("http://localhost:8000/note", headers={'Authorization': f"Bearer {temp}",'Content-Type': 'application/json'}, data=data_t)

        assert response.status_code == 200

    def test_add_user(self, client):
        credentials = base64.b64encode(
            b"mx@gmail.com:$2b$12$Vrin.JG97VLZ1UgGYh4BMOPiSweJwUUc/JKsYxql2JVXxrN4.qoa6").decode('utf-8')
        response = client.get("http://localhost:8000/login", headers={"Authorization": f"Basic {credentials}"})
        temp = response.json
        data_t = {
            'id': '2',
            'user_id': '4',
            'name': '12312as',
            'content': 'asdaslkd',
            'tag': 'asdkjashd'
        }
        data_t = json.dumps(data_t)
        response = client.post("http://localhost:8000/note", headers={'Authorization': f"Bearer {temp}",'Content-Type': 'application/json'}, data=data_t)

        assert response.status_code == 200
# PP_lab


Python 3.8.10

using virtualenv as virtual environment


1. locate project directory
2. create virtual environment by command
>>> virtualenv venv
3. activate environment
>>> venv\Scripts\activate
4. install requirements
>>> pip install -r requirements.txt
5. type
>>> waitress-serve --port=8000 app:app
6. in web-browser write URL:
>>> http://localhost:8000/api/v1/hello-world-2

Lab_6

1. create revision
>>> alembic stamp head
>
>>> alembic revision -m "add models" --autogenerate
2. upgrade head
>>> alembic upgrade head

Lab_7

alembic downgrade -1

curl -X POST -H "Content-Type:application/json" --data-binary "{\"firstname\": \"Max\"}" http://localhost:5000/api/v1/user


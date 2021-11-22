# PP_lab

> pip freeze -l > requirements.txt


Python 3.8.10

using virtualenv as virtual environment


1. locate project directory
2. create virtual environment by command
> virtualenv venv
3. activate environment
> venv\Scripts\activate
4. install requirements
> pip install -r requirements.txt
5. type
> waitress-serve --port=8000 app:app
6. in web-browser write URL:
> http://localhost:8000/api/v1/hello-world-2

Lab_6

1. create revision
> alembic stamp head
>
> alembic revision -m "add models" --autogenerate
2. upgrade head
> alembic upgrade head
>
> alembic downgrade -1

Lab_7

Users

> curl -X GET http://localhost:5000/user
>
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Max\", \"phone\": \"88005553535\", \"last_name\": \"Last_name\", \"username\": \"fayon\", \"email\": \"mx@gmail.com\", \"password\": \"dfghkgh\"}" http://localhost:5000/user
>
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Danylo\", \"phone\": \"88006653535\", \"last_name\": \"Last_name\", \"username\": \"theDaniel\", \"email\": \"9sarvas9@gmail.com\", \"password\": \"123\"}" http://localhost:5000/user 
> 
> curl -X GET -u 9sarvas9@gmail.com:$2b$12$KKxS/Vk1X7Gey/KQuHLmK.GE7Lb2aVjg3niKks7/t3GP5C8xzSVMa http://localhost:5000/login
> 
> curl -X GET http://localhost:5000/user/4 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4NDY5OCwianRpIjoiMWU2N2E2YzctYjRkYS00OWNiLWFjMTAtNzQzOGU1NzUxNWEyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjlzYXJ2YXM5QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4NDY5OCwiZXhwIjoxNjM3NTg1NTk4fQ.sbB7kzy4iO0fBlLuNJYdvbVNd967ci4Iz5Rf7zkMFrU" 
>
> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Boy\"}" http://localhost:5000/user/2
> 
> curl -X DELETE http://localhost:5000/user/1

Notes

> curl -X POST -H "Content-Type:application/json" --data-binary "{\"user_id\": \"1\", \"name\": \"Title\", \"content\": \"some message\", \"tag\": \"test\"}" http://localhost:5000/note
> 
> curl -X GET http://localhost:5000/note
> 
> curl -X GET http://localhost:5000/note/3
> 
> curl -X GET http://localhost:5000/note/test
> 
> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"name\": \"new name\", \"user_id\": \"7\", \"content\": \"new content\"}" http://localhost:5000/note/3
> 
> curl -X DELETE http://localhost:5000/note/1

Note Log

> curl -X GET http://localhost:5000/note_log
> 
> curl -X GET http://localhost:5000/note_log/3
> 
> curl -X GET http://localhost:5000/note/note_log/153

Lab_8
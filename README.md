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

>> get all users
>
> curl -X GET http://localhost:5000/user
>
>> create user
>
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Max\", \"phone\": \"88005553535\", \"last_name\": \"Last_name\", \"username\": \"fayon\", \"email\": \"mx@gmail.com\", \"password\": \"dfghkgh\"}" http://localhost:5000/user
>
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Danylo\", \"phone\": \"88006653535\", \"last_name\": \"Last_name\", \"username\": \"theDaniel\", \"email\": \"9sarvas9@gmail.com\", \"password\": \"123\"}" http://localhost:5000/user 
> 
>> log in user
> 
> curl -X GET -u mx@gmail.com:$2b$12$MXsM15MraMUb8IQcf8XiQOVoJE2WjmcbBryeEGj5loKp1WfJ7i5mC http://localhost:5000/login
> 
>> get user by id
> 
> curl -X GET http://localhost:5000/user/4 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4NjM5MiwianRpIjoiYTIzNGU2ZjMtZTUxMy00YjQ2LTk4ZjItMzgyYmU1N2YyMjI0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4NjM5MiwiZXhwIjoxNjM3NTg3MjkyfQ.j3X-GFQZfLEXnUG_R7n5uRx31zz1X-Se4a5v-bdTsmk" 
>
>> get user by username
> 
> curl -X GET http://localhost:5000/user/fayon -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4NjM5MiwianRpIjoiYTIzNGU2ZjMtZTUxMy00YjQ2LTk4ZjItMzgyYmU1N2YyMjI0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4NjM5MiwiZXhwIjoxNjM3NTg3MjkyfQ.j3X-GFQZfLEXnUG_R7n5uRx31zz1X-Se4a5v-bdTsmk"
> 
>> change user by id
> 
> curl -X PUT http://localhost:5000/user/4 -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Boy\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4NzYxOSwianRpIjoiMDRkMDBkYWYtMTQ4ZS00ZjhkLTk4NjItMWY2NGRjYWQ1YmViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4NzYxOSwiZXhwIjoxNjM3NTg4NTE5fQ.QF9nN7kb5rpjvI7FFnaH5uduWIoahClhkWUEnl_a5QI"
> 
>> delete user by id
> 
> curl -X DELETE http://localhost:5000/user/4 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4NzYxOSwianRpIjoiMDRkMDBkYWYtMTQ4ZS00ZjhkLTk4NjItMWY2NGRjYWQ1YmViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4NzYxOSwiZXhwIjoxNjM3NTg4NTE5fQ.QF9nN7kb5rpjvI7FFnaH5uduWIoahClhkWUEnl_a5QI"

Notes

>> create note
> 
> curl -X POST http://localhost:5000/note -H "Content-Type:application/json" --data-binary "{\"user_id\": \"6\", \"name\": \"Title\", \"content\": \"some message\", \"tag\": \"test\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4ODgyOCwianRpIjoiZWFlNzVhMzEtNDUyZS00ODU5LTk4NDctMjc1NzhhYzcxYmFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4ODgyOCwiZXhwIjoxNjM4MTkzNjI4fQ.SAkmbWlKPB8s-wGH1gn5u232RVlsWvmI_R_hjLAblGw"
> 
>> add user
> 
> curl -X PUT http://localhost:5000/note/add/6,3 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4ODgyOCwianRpIjoiZWFlNzVhMzEtNDUyZS00ODU5LTk4NDctMjc1NzhhYzcxYmFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4ODgyOCwiZXhwIjoxNjM4MTkzNjI4fQ.SAkmbWlKPB8s-wGH1gn5u232RVlsWvmI_R_hjLAblGw"
>
>> get all notes 
> 
> curl -X GET http://localhost:5000/note/3 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4ODgyOCwianRpIjoiZWFlNzVhMzEtNDUyZS00ODU5LTk4NDctMjc1NzhhYzcxYmFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4ODgyOCwiZXhwIjoxNjM4MTkzNjI4fQ.SAkmbWlKPB8s-wGH1gn5u232RVlsWvmI_R_hjLAblGw"
> 
>> get note by id 
> 
> curl -X GET http://localhost:5000/note/3
> 
>> get note by tag
> 
> curl -X GET http://localhost:5000/note/test
> 
>>  change note by id
> 
> curl -X PUT http://localhost:5000/note/3 -H "Content-Type:application/json" --data-binary "{\"name\": \"new name\", \"content\": \"new content\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4ODgyOCwianRpIjoiZWFlNzVhMzEtNDUyZS00ODU5LTk4NDctMjc1NzhhYzcxYmFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4ODgyOCwiZXhwIjoxNjM4MTkzNjI4fQ.SAkmbWlKPB8s-wGH1gn5u232RVlsWvmI_R_hjLAblGw"
> 
>> delete note by id 
> 
> curl -X DELETE http://localhost:5000/note/3 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzU4ODgyOCwianRpIjoiZWFlNzVhMzEtNDUyZS00ODU5LTk4NDctMjc1NzhhYzcxYmFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im14QGdtYWlsLmNvbSIsIm5iZiI6MTYzNzU4ODgyOCwiZXhwIjoxNjM4MTkzNjI4fQ.SAkmbWlKPB8s-wGH1gn5u232RVlsWvmI_R_hjLAblGw"

Note Log

> curl -X GET http://localhost:5000/note_log
> 
> curl -X GET http://localhost:5000/note_log/3
> 
> curl -X GET http://localhost:5000/note/note_log/153

Lab_8
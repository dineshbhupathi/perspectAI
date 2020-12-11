# perspectAI

Technology Stack:
Python 3.8.6
Django==3.1.4

clone project using this url:
git clone https://github.com/dineshbhupathi/perspectAI.git

To run project install requirements with below command
pip install -r requirements.txt

apply migrations to database below commands:
python manage.py makemigrations
python manage.py migrate


then run project:(command)
python manage.py runserver


Test Urls With PostMan:
-----------------------
To Login : http://127.0.0.1:8000/api/1.0/login/
----------

sample postman data:

{
    "username":"hr1",
    "password": "dinesh123"
}

sample output:

{
    "token": "aa147892f9bf4d086aed933fe0b5f8cf3dd733c4"
}

To see Employees & Create: http://127.0.0.1:8000/api/1.0/employee/ # you will get a list of employess which is assigned to you 
--------------------------

sample postman data:

{
    "emp_name": "ajay komatireddy",
    "emp_salary": 22500.0,
    "hr": 1
}

sample output:

{
    "id": 10,
    "emp_name": "ajay komatireddy",
    "emp_salary": 22500.0,
    "hr": 1
}


To Update Employee Instance:http://127.0.0.1:8000/api/1.0/employee/1/ #update with employee id
---------------------------

sample postman data:

{
    "id": 1,
    "emp_name": "dinesh",
    "emp_salary": 21200.0,
    "hr": 1
}

sample output:

{
    "id": 1,
    "emp_name": "dinesh",
    "emp_salary": 21200.0,
    "hr": 1
}


To Dalete employee with id: http://127.0.0.1:8000/api/1.0/employee/10/ 
---------------------------
it will delete the instance
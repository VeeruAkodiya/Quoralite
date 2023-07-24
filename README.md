# Quoralite
This project is based on Quora like applications by Using Django Framework where user can Post Questions, make answers to posted questions, Like Answers posted and  login/logout (using Django User Authentication System). 

How To Run Code:

1. Create Virtual Environment and Install Required Packages using `pip install -r requirements.txt`

2. Make changes in Settings.py in Databases Host,User,Port according to you. 

3. Run all Migrations to Test Setup Database table Creation
    python manage.py migrate auth
    python manage.py makemigrations
    python manage.py migrate

5. Start Django Server by `python manage.py runserver`

6. How To Use.

    Step 1 : Create User manually in auth_user table of database OR
            >>python manage.py createsuperuser
            Enter username and Password.

            If you want to add more users follow below steps:
                1.  open  http://127.0.0.1:8000/admin
                2.  login as super user.
                3.  add users to database.
            
    step 2 : To Login Enter username and Password and Click login to send Login Requests.
    step 3 : Post New question by clicking Post Question.
    step 4 : Answer Posted Question by clicking to make answer.
    step 5 : Like Any Answer by clicking Like Answer.
    step 5 : Logout .

   
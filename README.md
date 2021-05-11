# covid_django
## Steps to run
I guess Python and pip is already installed on your PC.
Here are the steps to follow:
- Clone the repo and go to the repo using CMD/Terminal
- pip install virtualenv
- virtualenv venv
- For Windows: .\venv\Scripts\activate | For MacOS/Linux: source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- Now open 127.0.0.0:8000 on any browser, enter city name, and it worked
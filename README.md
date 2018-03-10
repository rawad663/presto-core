# presto-core
Restaurant Reservation - Core (BackEnd) Component


**************API ROUTES**************

register/resto/		expects {"resto_name": "", "description": "", "phone_number": "", "postal_code": "", "user": {"username": "", "email": "", "first_name": "", "last_name": "", "password": ""}}

register/customer/	expects {"user": {"username": "", "email": "", "first_name": "", "last_name": "", "password": ""}}

login/ 	expects {"username": "", "password": ""} and returns {"token":" 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}

restos/ 		gets you a list of all restaurants

restos/<id>/		gets you info of a specific restaurant
	
customers/<id>/		gets you info of a specific customer
	
like-resto/<id>/	expects an empty POST
	
reserve/<customerID>/<restoID>/	expects {"datetime": "YYYY-MM-DD HH:mm"}
	
reservations/		gets you all user's reservations

**************************************

If you don't have the virtualenv setup, follow these steps:

pip install virtualenv

cd ~/presto-core

virtualenv {env name} # I called it ".env", the dot makes it hidden so you don't push that directory to github

source {env name}/bin/activate

If source command doesnt work for WINDOWS:
. {env name}/Scripts/activate
	


pip install Django==1.11

pip install djangorestframework==3.7.7


Debugging:  If trying to launch the app, by doing git push heroku master, and are getting the error: 
	Error while running '$ python manage.py collectstatic --noinput'.

You can run:
	heroku config:set DISABLE_COLLECTSTATIC=1

Look at https://devcenter.heroku.com/articles/django-assets#collectstatic-during-builds for more info

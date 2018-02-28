# presto-core
Restaurant Reservation - Core (BackEnd) Component

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

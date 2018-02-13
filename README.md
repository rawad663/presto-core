# presto-core
presto-core serves as the repository for the django back end of this website.
communication between django and the react project will be dont using the rest_framework

# setup and virtual env
1) You must be running python 3, to do so either
a. $ brew install python3
b. Download anaconda 3.5 at https://www.anaconda.com/download/
2) Set up a virtualenv and activate it
$ pip3 install virtualenv
$ virtualenv -p python3 <desired-path>
$ source <desired-path>/bin/activate
3) To deactivate it later, run:
$ deactivate
4) Your virtualenv must always be running while working on this project.
5) NEVER Commit your virtualenv to the repository
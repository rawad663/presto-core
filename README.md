# presto-core
presto-core serves as the repository for the django back end of this website.
communication between django and the react project will be dont using the rest_framework

# setup and virtual env
1) You must be running python 3, to do so either <br />
a. $ brew install python3 <br />
b. Download anaconda 3.5 at https://www.anaconda.com/download/
2) Set up a virtualenv and activate it <br />
$ pip3 install virtualenv <br />
$ virtualenv -p python3 'desired-path' <br />
$ source 'desired-path'/bin/activate <br />
3) To deactivate it later, run: <br />
$ deactivate
4) Your virtualenv must always be running while working on this project.
5) NEVER Commit your virtualenv to the repository
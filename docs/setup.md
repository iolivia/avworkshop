# Pre-requisites

## Virtual environment
A Pythin virtual environment is simply a sandbox/container which is used to run this application. The reason to use virtual environments is if you have multiple python projects on the same machine and you don't want to pollute your global installs. If this is the only python prohect you are running, feel free to skip this step. 

### Create a python virtual environment 
$ python3 -m venv av_env

### Activate the virtual env
$ source av_env/bin/activate

## Install python packages
$ cd avworkshow
$ pip install -r requirements.txt

# Running the server
$ python manage.py runserver

# Wrapping up
1. Press Ctrl+C to stop the server

2. Deactivate the env by running
$ deactivate

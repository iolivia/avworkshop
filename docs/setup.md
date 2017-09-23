# Create a python virtual environment 
pip3 install virtualenv 
virtualenv my_virtual_env

# Activate the virtual env
my_virtual_env\Scripts\activate

# Deactivate the virtual env
deactivate

# Install python packages 
pip install Django==1.11.5
pip install django-bootstrap3
pip install imdbpie
pip install simplejson
pip install pdb

# Run the server
python manage.py runserver
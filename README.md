# Django and Vue 3 integration

The folder structure for the project is as follows

|- frontend (Here save the Vue 3 project)
|- main (Django main folder)
|- templates (Django templates)
|---- bd.sqlite3 (Default Django database )
|---- manage.py (File to run django)
|---- requirements.txt (packages for the py virtual enviroment)
|---- README.md
|---- .gitignore

## Virtual Enviroment for Python

To create the virtual enviroment in python use:

`python -m virtualenv .venv`

_Note: the name '.venv' is optional, you can choose any_ 

To activate the virtual enviroment in windows:

`.venv/Scripts/activate`

Once activated the virtual enviroment, you can add the packages:

`pip install -r requirements.txt`

Located in the path of `manage.py`, now you can run the django project:

`python manage.py runserver`

Some important packages included in this project are:

  - django==3.2.12
  - django-cors-headers
  - django-rest-framework
  - psycopg2
  - django-webpack-loader


## Initialize Vue 3 Project

To initialize the Vue 3 project, you need initialize the node_modules folder. To do this, you need ubicated in the path of the project:

`cd frontend`
`npm install -y`

and to run Vue 3 project, run the command:

`npm run serve`


# Some dependences to integrate Django and Vue 3


Debe instalarse el webpack bundle y loader en npm y python.

- Npm
https://www.npmjs.com/package/webpack-bundle-tracker 

npm install --save-dev webpack-bundle-tracker

- Python
https://pypi.org/project/django-webpack-loader/

pip install django-webpack-loader
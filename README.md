# Django and Vue 3 integration

This template contains an integration betweeen Django 3.2.12 with Vue 3 CLI. This integration was possible thanks to the [webpack-bundler-tracker](https://www.npmjs.com/package/webpack-bundle-tracker ) and [django-webpack-loader](https://pypi.org/project/django-webpack-loader/) dependencies.

Also it contains another packages to use with Django, like Django Rest Framework and Corsheaders, while Vue 3 already contains Router and Vuex.

The folder structure for the project is as follows

- frontend (Here save the Vue 3 project)
- main (Django main folder)
- templates (Django templates)
  - bd.sqlite3 (Default Django database )
  - manage.py (File to run django)
  - requirements.txt (packages for the py virtual enviroment)
  - README.md
  - .gitignore

# Installation

To install this project you need install the Vue 3 project and later the Virtual Enviroment for Django project.


## Install Vue 3 Project

To initialize the Vue 3 project, you need initialize the node_modules folder. To do this, you need ubicated in the path of the project:

`cd frontend`

`npm install -y`

and to run Vue 3 project, run the command:

`npm run serve`



## Virtual Enviroment for Python and Install Django 3.2.12

The first thing to do is to be located in the path where the manage.py file is located, and then you can create virtual enviroment in python use:

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

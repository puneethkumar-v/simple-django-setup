# Django Setup

## Installing a virtual environment package to maintain dependencies for python projects:

```sh
sudo apt-get install virtualenv
```

## Creating a virtual environment for the project:

```sh
virtualenv example-environment
```

## Activating a virtual environment space:

```sh
cd example-environment
source bin/activate
```

## Installing django inside a virtual env:

```sh
pip install django
```

## To check the version of django installed:

```sh
python3 -m django --version
```

## Initializing a Django Project:

```sh
django-admin startproject example-project
```

## Once the Project is initialized following files and directories will be available:

- example-project - Project Folder
  - manage.py - main file
  - example-project - python package
    - **init**.py
    - settings.py - necessary settings about the project
    - urls.py - file to manage all the urls

## Command to run the project:

```sh
python3 manage.py runserver
```

## App in Django:

- It is a simple module or an extra package of the Software Project
- Single Project can have multiple app inside of it

## Command to create a app inside django project:

```sh
python3 manage.py startapp
```

Once the App in installed it is necessary to include the name of the App in the example-project/settings.py - inside INSTALLED_APPS list

## Project Folder structure after creating a App:

- example-project
  - **init**.py
  - admin.py
  - apps.py
  - migrations
    - **init**.py
  - models.py - All the Database table structures
  - views.py - All the views that are rendered on the web page

## Data Flow:

- Models contains all the Table structures - Basically a Python class as a table name that contains all the attribute names as its local variables
- Model Names have to be registered in the admin.py file
- Creating a view inside view.py - Basically a python function that will return a render function with parameters as request(GET, POST, PUT, DELETE), context(data) and a template file(.html files)
- Views are then registered inside urls.py - It is also a python function that returns path function with parameters as path(url) and view(function must be imported from views.py)
- TEMPLATE: Actual response in the form of html file

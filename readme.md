# How to create a django project?

## step 1 
Create a folder for the project

## step 2
Open in VS code and open a terminal

## step 3
Create a virtual environment for the project

windows: py -m venv venv

## step 4
active the virtual environment
    .\venv\Scripts\activate

## step 5
Install Django dependencies

    Windows: pip install django

## step 6
Run the startproject command to create the project settings
    Both OS: django-admin startproject NAME_OF_PROJECT .
    note: Replace NAME_OF_PROJECT with config or any other name

    expected output: two folders and a single file called manage.py in ROOT

## step 7
Run Django project
    Windows: py manage.py runserver

## step 8
Django command to create apps:

Windows: python manage.py startapp NAME_OF_THE_APP


## Models in Django

When we finish a model structure we need to run these commands in order:

    1. py manage.py makemigrations
    2. py manage.py migrate
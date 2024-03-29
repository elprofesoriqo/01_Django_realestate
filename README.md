# 01_Django_realestate


1. Creating virtual env:
    - virtualenv venv
    Optional:
        - Get-ExecutionPolicy
        - Set-ExecutionPolicy RemoteSigned
    - .\Scripts\Activate.ps1
    - deactivate
2. Instaling inside the env
    - pip install django

3. Starting project:
    - django-admin startproject real_estate

4. Starting files:
    - _init_.py:
        - excutes code
        - to mark a directory as a Python package and to initialize the package
        - Contains code, function definitions, and variable assignments.
        - Facilitates structuring Python packages and organizing code within them.
    - asgi.py:
        - serves as the entry-point for ASGI-compatible web servers to communicate with Django applications asynchronously
        - enabling the deployment of Django projects in an asynchronous environment
    - settings.py:
        - is essential for configuring various aspects of a Django project
        - it should be managed carefully to ensure the proper functioning and security of the application
    - urls.py:
        - plays a crucial role in defining the URL structure of a Django project
        - facilitating the mapping of URLs to views and ensuring proper routing of user requests within the application
    - wsgi.py:
        - enables the interaction between Django applications and WSGI servers
        - ensuring the proper handling of HTTP requests and responses within the application.
        - synchronously

5. Migrations:
    - python manage.py migrate
        - propagate changes made to models into the database schema

6. Starting project:
    - python manage.py runserver 
    - superuser:
        - python manage.py createsuperuser
    - listings:
        python manage.py startapp listings


7. Adding listings to settings

8. Creating model


9. Views
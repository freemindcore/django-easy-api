# DJANGO-EASY-API 
A boilerplate Django REST API project for quickly getting started, easy, secure and fast.
Based on [django-api-framework](https://github.com/freemindcore/django-api-framework) -- a django-ninja/extra powered project.

## Features
-   Automatic CRUD API for all django models
-   Async Django-Ninja APIs (with OpenAPI/Swagger docs)
-   For Django 3.1+, Works with Python 3.8+
-   Twitter [Bootstrap](https://github.com/twbs/bootstrap) v5
-   [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
-   Secure by default. We believe in SSL.
-   Optimized development and production settings
-   Registration via [django-allauth](https://github.com/pennersr/django-allauth)
-   Comes with custom user model ready to go
-   Run tests with unittest or pytest: start with 100% coverage
-   Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
-   Configuration for [Celery](https://docs.celeryq.dev) and [Flower](https://github.com/mher/flower) (the latter in Docker setup only)
-   Integration with [Sentry](https://sentry.io/welcome/) for error logging

### Install
`make install
`
### Start up
`python manage.py runserver_plus`

or 

`uvicorn --reload config.asgi_local:application --lifespan off`


### Unit test
`make test-cov`

```
---------- coverage: platform darwin, python 3.8.10-final-0 ----------
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
easy_api/__init__.py                       2      0   100%
easy_api/conftest.py                       8      0   100%
easy_api/contrib/__init__.py               0      0   100%
easy_api/contrib/sites/__init__.py         0      0   100%
easy_api/users/__init__.py                 0      0   100%
easy_api/users/adapters.py                11      0   100%
easy_api/users/admin.py                   13      0   100%
easy_api/users/apps.py                    10      0   100%
easy_api/users/context_processors.py       3      0   100%
easy_api/users/forms.py                   15      0   100%
easy_api/users/models.py                  13      0   100%
easy_api/users/tasks.py                    6      0   100%
easy_api/users/urls.py                     4      0   100%
easy_api/users/views.py                   27      0   100%
----------------------------------------------------------
TOTAL                                    112      0   100%

```

### You are all set!
Visit http://127.0.0.1:8000 for your website.

Visit http://127.0.0.1:8000/admin for your adminsite.

Visit http://127.0.0.1:8000/api_admin/v1/docs for the automatic interactive API documentation (provided by Swagger UI).

![image](https://github.com/freemindcore/django-easy-api/assets/5857025/880bd2ac-b1f7-4860-8a5e-9a9a514f0421)


### Thanks 
Special thanks to cookiecutter-django for the great starter template

https://github.com/cookiecutter/cookiecutter-django

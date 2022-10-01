# DJANGO-EASY-API 
A boilerplate Django REST API project for quickly getting started, easy, secure and fast.
Based on django-api-framework -- a django-ninja/extra powered project.

## Features
-   Automatic CRUD API for all django models
-   Async Django-Ninja APIs (with OpenAPI/Swagger docs)
-   For Django 3.2, Works with Python 3.9
-   Twitter [Bootstrap](https://github.com/twbs/bootstrap) v5
-   [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
-   Secure by default. We believe in SSL.
-   Optimized development and production settings
-   Registration via [django-allauth](https://github.com/pennersr/django-allauth)
-   Comes with custom user model ready to go
-   Run tests with unittest or pytest
-   Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
-   Configuration for [Celery](https://docs.celeryq.dev) and [Flower](https://github.com/mher/flower) (the latter in Docker setup only)
-   Integration with [Sentry](https://sentry.io/welcome/) for error logging

### Install
`make install
`
### Start up
`uvicorn --reload config.asgi_local:application --lifespan off`

### Thanks 
Special thanks to cookiecutter-django for the great starter template

https://github.com/cookiecutter/cookiecutter-django

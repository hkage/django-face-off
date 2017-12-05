django-face-off
===============

A Django application to provide a user switch for admin users without exposing the actual users
passwords.

Features
--
* Admin form to activate the user switch

Supports
--
* Django >= 1.4

Installation
--

``django-face-off`` is currently in development. There aren't any PyPi packages yet.

Get the latest version:

    $ git clone git@github.com:hkage/django-face-off.git#egg=django-face-off

and run the installation via setup.py:

    $ python setup.py install

Usage
--

Add ``face-off`` to the list of installed apps in your settings:

    INSTALLED_APPS = (
        'face_off'
    )

Add the middleware:

    MIDDLEWARE_CLASSES = (
        'face_off.middleware.UserRepresentationMiddleware',
    )

Run the migration:

    $ python manage.py migrate

Testing
--

    $ py.test

Settings
--

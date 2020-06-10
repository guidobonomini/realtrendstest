Real Trends Test
================

Real Trends Mercadolibre - Test técnico


:License: MIT


Docker
^^^^^^

To run the application, execute the following commands::

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up

Setting Up Your Admin account
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy rtmeli

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest


Deployment - Heroku
^^^^^^




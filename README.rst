django-bnr
==========

BNR exchange rates for django apps.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-bnr

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/PressLabs/django-bnr.git#egg=django_bnr

Add ``django_bnr`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_bnr',
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate django_bnr


Usage
-----

The package provides a python function for getting BNR exchange rates.

.. code-block:: python

    from django_bnr.utils import get_bnr_rate
    get_bnr_rate(date, currency)

It also provides a management command for getting the BNR rates. Running it
daily in a cron ensures you have data cached since BNR offers rates for up to
15 days.

.. code-block:: bash

    ./manage.py get_bnr_rate -c CURRENCY -d DATE


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-bnr

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

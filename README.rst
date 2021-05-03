==================
scottbrian-secdata
==================

Intro
=====

With secdata, you can obtain fundamental data from the SEC data dump txt files. The data can be requested for one or
more companies, and for any raw data point or as ratios.

>>> from scottbrian_secdata.sec_data import SecData
>>> sec_data = SecData()
>>> apple_pe = sec_data.get_ratio(company='AAPL', ratio='pe', date='2020-12-31', period='Y')
>>> print(f'apple_pe={apple_pe:0.1f}')
29.8


.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. image:: https://readthedocs.org/projects/pip/badge/?version=stable
    :target: https://pip.pypa.io/en/stable/?badge=stable
    :alt: Documentation Status


The sec_data.py module contains:

1. SecData class with functions to read SEC data and provide fundamental information.



Installation
============

Linux:

``pip install scottbrian-secdata``


Usage examples:
===============



Development setup
=================

See tox.ini

Release History
===============

* 1.0.0
    * Initial release

Meta
====

Scott Tuttle

Distributed under the MIT license. See ``LICENSE`` for more information.


Contributing
============

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

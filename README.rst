==========
Expires By
==========


.. image:: https://img.shields.io/pypi/v/expires_by.svg
        :target: https://pypi.python.org/pypi/expires_by

.. image:: https://img.shields.io/travis/at3560k/expires_by.svg
        :target: https://travis-ci.com/at3560k/expires_by

.. image:: https://readthedocs.org/projects/expires-by/badge/?version=latest
        :target: https://expires-by.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/at3560k/expires_by/shield.svg
     :target: https://pyup.io/repos/github/at3560k/expires_by/
     :alt: Updates



A dependency that goes bad at a certain time


* Free software: GNU General Public License v3
* Documentation: https://expires-by.readthedocs.io.


Features
--------

* There aren't many features yet.
*  My goal is that `pip install expires-by==$(date +%Y%m%d)` builds
  today, and fails to build tomorrow.
*  More importantly, that `pip install expires-by==$(date +%Y%m%d --date="next year")`
  works for a year, and then the fails.

Why?  Because you should update your dependencies occassionally!

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

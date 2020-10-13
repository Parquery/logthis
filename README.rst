logthis
=======

.. image:: https://github.com/Parquery/logthis/workflows/Check-push/badge.svg
    :target: https://github.com/Parquery/logthis/actions?query=workflow%3ACheck-push
    :alt: Check status

.. image:: https://coveralls.io/repos/github/Parquery/logthis/badge.svg?branch=master
    :target: https://coveralls.io/github/Parquery/logthis
    :alt: Test coverage

.. image:: https://badge.fury.io/py/logthis.svg
    :target: https://pypi.org/project/logthis/
    :alt: PyPI - version

.. image:: https://img.shields.io/pypi/pyversions/logthis.svg
    :target: https://pypi.org/project/logthis/
    :alt: PyPI - Python Version

logthis is a singleton, two-level, colorful, thread-safe, knob-free, logging library for in-house software.

* **singleton**: There is no object to create. There are only two logging functions, ``say()`` and ``err()``.

* **two-level**: There is only the information level and the error level. Nothing else. We found it way too mentally
  involving to have more than two logging levels. We want to avoid unnecessary cognitive load at every message ("Is this
  a warning? Or an information? Or debugging information?"). We don't think that is important. Either there is a problem
  and needs to be resolved (so use ``err()``), or everything is fine and no action is required by the operator (so use
  ``say()``).

* **colorful**: The prefix of a message is colored indicating the log level. This makes reading the logs easier on the
  eyes and helps direct the attention. Colors are included even when the logging is redirected to a file. We inspect
  our logs with Unix utilities (``cat`` and the ilk) and find it cool to preserve colors even when we inspect files such
  as supervisord logs.

* **thread-safe**: We use a global lock so that multi-threaded logging is not garbled. STDOUT and STDERR are flushed on
  every logging.

* **knob-free**: There are no options or targets/sinks/streams to set. The information is written to STDOUT and the
  errors are written to STDERR. We found it daunting to learn and deal with all the special knobs in libraries such as
  Python `logging`.

* **in-house software**: logthis is meant to be used for the software developed and operated in-house. Its output will
  be examined by people who are familiar with the code and would like to inspect it on problems. We include the name of
  the script and the line number in the messages as well as time in UTC so that it is easier to trace bugs and see
  where in the code the logging comes from.

  If you are developing a library or a program for wider audience, then logthis is probably not for you.

Usage
=====

.. code-block:: python

    import logthis

    # inform the user
    logthis.say("Hello!")

    # alert the user that there is an error
    logthis.err("Something bad happened".)

The output is:

.. image:: https://media.githubusercontent.com/media/Parquery/logthis/master/screenshot.png

Installation
============

* Create a virtual environment:

.. code-block:: bash

    python3 -m venv venv3

* Activate it:

.. code-block:: bash

    source venv3/bin/activate

* Install logthis with pip:

.. code-block:: bash

    pip3 install logthis

Development
===========

* Check out the repository.

* In the repository root, create the virtual environment:

.. code-block:: bash

    python3 -m venv venv3

* Activate the virtual environment:

.. code-block:: bash

    source venv3/bin/activate

* Install the development dependencies:

.. code-block:: bash

    pip3 install -e .[dev]

* We use tox for testing and packaging the distribution. Assuming that the virtual environment has been activated and
  the development dependencies have been installed, run:

.. code-block:: bash

    tox

* We also provide a set of pre-commit checks that lint and check code for formatting. Run them locally from an activated
  virtual environment with development dependencies:

.. code-block:: bash

    ./precommit.py

* The pre-commit script can also automatically format the code:

.. code-block:: bash

    ./precommit.py  --overwrite

Versioning
==========
We follow `Semantic Versioning <http://semver.org/spec/v1.0.0.html>`_. The version X.Y.Z indicates:

* X is the major version (backward-incompatible),
* Y is the minor version (backward-compatible), and
* Z is the patch version (backward-compatible bug fix).

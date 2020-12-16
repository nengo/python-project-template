.. image:: https://img.shields.io/pypi/v/nengo-bones.svg
  :target: https://pypi.org/project/nengo-bones
  :alt: Latest PyPI version

.. image:: https://img.shields.io/codecov/c/github/nengo/nengo-bones/master.svg
  :target: https://codecov.io/gh/nengo/nengo-bones
  :alt: Test coverage

**********
NengoBones
**********

The aim of this project is to automate the configuration of repositories
throughout the Nengo ecosystem.  The idea is that we can centralize the
design and maintenance of "meta" project code (such as CI testing
infrastructure) in this project, rather than each repository maintaining that
code independently.

The basic methodology for this project is a templating system in which
there are common templates for meta files that are populated with
data in each downstream project.  Projects control this templating through the
``.nengobones.yml`` configuration file, which defines the information used to
fill in the templates.

Wherever possible, we try to do this templating in such a way that downstream
projects will be automatically updated when an update is made in
``nengo-bones``. However, some files cannot be updated automatically and
require downstream repos to manually run a script to update those files.

Note that this repository itself is configured using the ``nengo-bones``
templating system, so if you would like an example of how to use it, check out
`the source code <https://github.com/nengo/nengo-bones>`__.

Installation
============

NengoBones is designed to be used based on the ``master`` branch (although we
release occasional stable checkpoints to PyPI). This can be installed via

.. code-block:: bash

    git clone https://github.com/nengo/nengo-bones.git
    pip install -e ./nengo-bones

Basic usage
===========

The first step is to fill in the ``.nengobones.yml`` configuration file.  You
can use the one in this repository as a starting point, or see
`the documentation
<https://www.nengo.ai/nengo-bones/examples/configuration.html>`__
for more details.  This file should be
placed in the top level of your project.

All of the manually generated template files can then be rendered by running
this command in the same folder as the ``.nengobones.yml`` file:

.. code-block:: bash

    bones-generate

See ``bones-generate --help`` or
`the documentation <https://www.nengo.ai/nengo-bones/cli.html>`__
for a full list of command line options.

Documentation
=============

- `Command line usage <https://www.nengo.ai/nengo-bones/cli.html>`_
- `Demonstration of available configuration options
  <https://www.nengo.ai/nengo-bones/examples/configuration.html>`_
- `API reference <https://www.nengo.ai/nengo-bones/reference.html>`_

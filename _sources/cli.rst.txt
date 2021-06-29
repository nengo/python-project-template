**********************
Command line interface
**********************

Generating files
================

In general, the only command that downstream repos will ever need to run is

.. code-block:: bash

    bones-generate

from the root directory containing ``.nengobones.yml``.  This updates all of
the templated files that need to be manually updated and committed to the
downstream repository.  Note that there are other files that
``bones-generate`` can generate, but this is done automatically
(i.e., dynamically) by ``nengo-bones`` during continuous integration.

However, it may be helpful when debugging a ``.nengobones.yml`` configuration
to be able to see the rendered output, so we expose all the ``nengo-bones``
functionality through different command line options, which can be found
below.

.. click:: nengo_bones.scripts.generate_bones:main
    :prog: bones-generate
    :show-nested:

.. click:: nengo_bones.scripts.check_bones:main
    :prog: bones-check
    :show-nested:


Other development support scripts
=================================

This repository also contains scripts to automate various development tasks.

.. click:: nengo_bones.scripts.pr_number:main
    :prog: bones-pr-number
    :show-nested:

.. click:: nengo_bones.scripts.format_notebook:main
    :prog: bones-format-notebook
    :show-nested:

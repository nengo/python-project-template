***************
Release History
***************

.. Changelog entries should follow this format:

   version (release date)
   ======================

   **section**

   - One-line description of change (link to Github issue/PR)

.. Changes should be organized in one of several sections:

   - Added
   - Changed
   - Deprecated
   - Removed
   - Fixed

20.5 (unreleased)
=================

**Added**

- Added support for new ``one_page`` option in ``nengo-sphinx-theme``. (`#101`_)
- Added ``tagmanager_id`` option to ``docs_conf.py.template``,
  which will enable Google Tag Manager tracking. This option takes precedence
  over ``analytics_id`` if both are specified. (`#114`_)
- Added the ``bones-format-notebook`` script to apply automated formatting, cleanup,
  and static checking to Jupyter notebooks. (`#32`_)
- Static script will now check that ``bones-format-notebook`` has been applied to all
  notebooks in the ``docs`` directory. (`#32`_)
- Added ``remote-script.sh`` CI script for running other CI scripts on a remote device.
  (`#124`_)
- Added `isort <https://pycqa.github.io/isort/>`_ configuration to
  ``pyproject.toml`` and check import order during static checks. (`#121`_)
- Officially support and test against Python 3.9. (`#136`_)
- Added ``skip`` option to codespell config, which can be used to specify files that
  should be ignored. (`#138`_)
- Added support for projects with type hints through the ``py_typed`` section. (`#140`_)
- Added ``min_python`` option to the main section. The default ``python_requires``
  in ``setup.py`` is now based on this, if not overridden. (`#140`_)
- Added support for changing the main branch name with the ``main_branch``
  config option. (`#145`_)
- Added checksum verification to Codecov upload script. (`#150`_)

**Changed**

- Restrict pylint version to <2.5 due to issue when the package being checked
  is not installed in the current environment. (`#103`_)
- Increased minimum ``black`` version to 20.8b0. (`#104`_)
- Increased minimum ``pylint`` version to 2.5.1 (`#32`_)
- Documentation ``[source]`` links now point to GitHub. (`#117`_)
- Separate tokens, ``PYPI_TOKEN`` and ``PYPI_TEST_TOKEN``, must now be specified
  for deploying to PyPI and TestPyPI, respectively. (`#127`_)
- Builds for this repository now run on TravisCI.com instead of TravisCI.org. (`#130`_)
- Drop support for Python 3.5. (`#123`_)
- Doc script will now install Sphinx>=3.1.2. (`#137`_)
- Codespell ignore words is now specified via the ``codespell.ignore_words`` section
  of ``setup_cfg`` (instead of in the static CI script config). As a result, it will
  now apply to all invocations of codespell (not just from the static script). (`#138`_)
- ``bones-format-notebook --check`` will now require that all ``codespell`` checks pass.
  (`#138`_)

**Fixed**

- Intermittent failures installing miniconda in the remote script have been fixed by
  retrying the miniconda install if it fails. (`#130`_)
- Fixed an issue in which Codecov would not report on files where a file in a
  deeper folder shares the same name. (`#132`_)
- Fixed an issue in which CI scripts did not have access to the same configuration
  options as other templates. (`#144`_)

.. _#32: https://github.com/nengo/nengo-bones/pull/32
.. _#101: https://github.com/nengo/nengo-bones/pull/101
.. _#103: https://github.com/nengo/nengo-bones/pull/103
.. _#104: https://github.com/nengo/nengo-bones/pull/104
.. _#114: https://github.com/nengo/nengo-bones/pull/114
.. _#117: https://github.com/nengo/nengo-bones/pull/117
.. _#121: https://github.com/nengo/nengo-bones/pull/121
.. _#123: https://github.com/nengo/nengo-bones/pull/123
.. _#124: https://github.com/nengo/nengo-bones/pull/124
.. _#127: https://github.com/nengo/nengo-bones/pull/127
.. _#130: https://github.com/nengo/nengo-bones/pull/130
.. _#132: https://github.com/nengo/nengo-bones/pull/132
.. _#136: https://github.com/nengo/nengo-bones/pull/136
.. _#137: https://github.com/nengo/nengo-bones/pull/137
.. _#138: https://github.com/nengo/nengo-bones/pull/138
.. _#140: https://github.com/nengo/nengo-bones/pull/140
.. _#144: https://github.com/nengo/nengo-bones/pull/144
.. _#145: https://github.com/nengo/nengo-bones/pull/145
.. _#150: https://github.com/nengo/nengo-bones/pull/150

0.11.1 (April 13, 2020)
=======================

**Changed**

- Rendered documentation will not be uploaded if the html build fails (it will still
  be uploaded if the linkchecker/doctest builds fail). (`#98`_)
- Rendered documentation will not be uploaded on cron builds. (`#98`_)
- Docs script will now clean up the built doc directory before execution, if it exists
  (e.g., because the docs job is being rerun). (`#96`_)

.. _#96: https://github.com/nengo/nengo-bones/pull/96
.. _#98: https://github.com/nengo/nengo-bones/pull/98

0.11.0 (April 13, 2020)
=======================

**Added**

- Downstream repos will now be automatically updated when nengo-bones is updated.
  (`#97`_)
- Added ``slack_notifications`` option to ``.travis.yml`` to enable Slack notifications
  for failing builds. (`#97`_)

**Changed**

- Will now use ``nengo-bones`` and ``nengo-sphinx-theme`` master builds (instead of the
  latest release), to streamline the process of distributing changes to those core
  repos. (`#97`_)

.. _#97: https://github.com/nengo/nengo-bones/pull/97

0.10.0 (March 19, 2020)
=======================

**Added**

- Added ``autoautosummary_change_modules`` option (for use with
  ``nengo_sphinx_theme.ext.autoautosummary``). (`#86`_)

**Changed**

- Docs script will now use ``nengo_sphinx_theme.ext.backoff``, which adds
  exponential backoff functionality to Sphinx requests. (`#86`_)

.. _#86: https://github.com/nengo/nengo-bones/pull/86

0.9.1 (March 17, 2020)
======================

**Fixed**

- Fixed deployment tag conditional check in ``.travis.yml`` template. (`#83`_)

.. _#83: https://github.com/nengo/nengo-bones/pull/83


0.9.0 (January 28, 2020)
========================

**Changed**

- The ``bones-check`` that TravisCI does now prints diffs for easier
  debugging. (`#80`_)

**Fixed**

- Fixed an issue with the ``.travis.yml`` template caused by the new
  Jinja2 release. (`#80`_)

.. _#80: https://github.com/nengo/nengo-bones/pull/80

0.8.0 (January 10, 2020)
========================

**Changed**

- The default distribution used in builds is now ``xenial``. (`#79`_)

.. _#79: https://github.com/nengo/nengo-bones/pull/79

0.7.3 (January 8, 2020)
=======================

**Removed**

- Removed coverage.py early starting logic. This is no longer necessary as of Nengo
  3.0 and causes problems with the new coverage.py 5.0 release. (`#78`_)

.. _#78: https://github.com/nengo/nengo-bones/pull/78

0.7.2 (December 2, 2019)
========================

**Changed**

- Failing to install miniconda in ``remote.sh`` is no longer considered a build
  error (this can occur, for example, when rerunning a build that already has
  miniconda installed). (`#71`_)

.. _#71: https://github.com/nengo/nengo-bones/pull/71

0.7.1 (November 14, 2019)
=========================

**Added**

- Added support for ``nengo_sphinx_theme.ext.redirects``, which can be used to
  automatically add redirects for renamed documentation pages. (`#68`_)

**Fixed**

- Added locking to ``remote.sh`` script to avoid possible race conditions
  during cleanup. (`#69`_)

.. _#68: https://github.com/nengo/nengo-bones/pull/68
.. _#69: https://github.com/nengo/nengo-bones/pull/69

0.7.0 (November 7, 2019)
========================

**Added**

- Added support for ``sphinx.ext.doctest``, which can be used to automatically
  test code snippets in docstrings. (`#67`_)

**Changed**

- Updated the ``black`` version used in ``pre-commit`` hooks. (`#67`_)

.. _#67: https://github.com/nengo/nengo-bones/pull/67

0.6.0 (October 30, 2019)
========================

**Added**

- Added a ``remote.sh`` CI script template for remotely executing
  commands on an SSH-accessible machine. (`#65`_)

**Fixed**

- Fixed a crash when a file contained the text "Automatically generated
  by nengo-bones", but was not present in the config file. (`#61`_, `#66`_)

.. _#61: https://github.com/nengo/nengo-bones/issues/61
.. _#66: https://github.com/nengo/nengo-bones/pull/66
.. _#65: https://github.com/nengo/nengo-bones/pull/65

0.5.0 (September 3, 2019)
=========================

**Added**

- Added ``nengo_simulator``, ``nengo_simloader`` and ``nengo_neurons``
  options to the ``pytest`` section of the ``setup.cfg`` template to
  support testing changes in Nengo 3.0. (`#58`_)

**Changed**

- The default value for ``pytest.addopts`` in ``setup.cfg`` has been removed
  because Nengo 3.0 does not require ``-p nengo.tests.options``. (`#58`_)

.. _#58: https://github.com/nengo/nengo-bones/pull/58

0.4.2 (August 8, 2019)
======================

**Added**

- Added ``plt_dirname`` option to the ``pytest`` section of the ``setup.cfg``
  template to set the plot directory for pytest-plt. (`#52`_)
- Added ``plt_filename_drop`` option to the ``pytest`` section of the
  ``setup.cfg`` template to set pruning patterns for pytest-plt. (`#52`_)
- Added ``rng_salt`` option to the ``pytest`` section of the ``setup.cfg``
  template to set the salt for pytest-rng. (`#55`_)

.. _#52: https://github.com/nengo/nengo-bones/pull/52
.. _#55: https://github.com/nengo/nengo-bones/pull/55

0.4.1 (July 26, 2019)
=====================

**Added**

- Added ``allclose_tolerances`` option to the ``pytest`` section of the
  ``setup.cfg`` template to set tolerances for pytest-allclose. (`#47`_)

.. _#47: https://github.com/nengo/nengo-bones/pull/47

0.4.0 (July 26, 2019)
=====================

**Added**

- Added style guide and release instructions to documentation. (`#44`_)
- Added templates for ``.pre-commit-config.yaml`` and ``pyproject.toml``
  so downstream repositories can easily adopt Black. (`#49`_)

**Changed**

- We now check that Python source files are autoformatted with Black
  in the ``static.sh`` script. (`#49`_)
- Templates will now be autoformatted with Black during the rendering
  process, if Black is installed. (`#49`_)
- Take advantage of multiprocessing to speed up pylint static checks. (`#49`_)
- The ``E203`` flake8 check and ``bad-continuation`` pylint check are now
  disabled by default. (`#50`_)

.. _#44: https://github.com/nengo/nengo-bones/pull/44
.. _#49: https://github.com/nengo/nengo-bones/pull/49
.. _#50: https://github.com/nengo/nengo-bones/pull/50

0.3.0 (July 19, 2019)
=====================

**Added**

- The ``nengo_bones.templates`` module was added to consolidate code
  that loads and renders templates. (`#45`_)

**Changed**

- The ``docs/conf.py`` template has been updated for new versions of
  Nengo Sphinx Theme. (`#46`_)
- ``static.sh`` and ``examples.sh`` will now check any notebooks in the
  ``docs`` folder (not just ``docs/examples``). (`#46`_)
- ``bones-check`` now checks that the content of the generated files
  matches the expected content, rather than relying on version numbers.
  This means most files will not need to be regenerated when new NengoBones
  versions are released, and that ``bones-check`` will be sensitive to changes
  within a dev version. (`#45`_)

**Fixed**

- The ``static.sh``/``examples.sh`` script will no longer fail if there are no
  notebooks in the ``docs`` folder. (`#46`_)

.. _#45: https://github.com/nengo/nengo-bones/pull/45
.. _#46: https://github.com/nengo/nengo-bones/pull/46

0.2.1 (May 24, 2019)
====================

**Added**

- Added ``codespell_ignore_words`` option to ``static.sh.template``,
  which is a list of words that ``codespell`` will ignore. (`#35`_)
- Added ``analytics_id`` option to ``docs_conf.py.template``,
  which will enable Google Analytics tracking. (`#35`_)

**Changed**

- ``codespell`` will now ignore ``_vendor`` directories. (`#36`_)

**Fixed**

- Fixed an issue with ``static.sh.template`` in which Python files
  that were not converted from notebooks were deleted. (`#16`_)

.. _#16: https://github.com/nengo/nengo-bones/pull/16
.. _#35: https://github.com/nengo/nengo-bones/pull/35
.. _#36: https://github.com/nengo/nengo-bones/pull/36

0.2.0 (May 15, 2019)
====================

**Added**

- Added ``apt_install`` option that can be set in the ``jobs`` section to
  ``apt install`` any custom ``apt`` requirements for a job. (`#14`_)
- Added templates for ``CONTRIBUTING.rst``, ``CONTRIBUTORS.rst``,
  ``LICENSE.rst``, ``MANIFEST.in``, ``docs/conf.py``, ``setup.cfg``, and
  ``setup.py`` (`#17`_)
- Templates will now be automatically loaded from a ``<repo>/.templates``
  directory if it exists. When overriding existing templates, the built-in
  templates can be accessed in ``include`` and ``extend`` tags with the
  ``templates/`` prefix. (`#17`_)
- Added ``flake8`` to the static check script. (`#17`_)
- Added the ``bones-pr-number`` script to predict the next PR number for a
  repository. This helps when writing a changelog entry before a PR has been
  made. (`#18`_)

**Changed**

- The Python version is now specified by the ``python`` option (instead of
  ``python_version``), for consistency with ``.travis.yml``. (`#14`_)
- All ``nengo-bones`` scripts now start with ``bones-``, to make them easier
  to find with autocompletion. ``generate-bones`` is now ``bones-generate``,
  and ``check-bones`` is now ``bones-check``. (`#18`_)

**Removed**

- Removed ``conda`` from the CI setup; all installations should be done
  through ``pip`` instead. (`#14`_)
- Removed the ``--template-dir`` option from the ``generate-bones`` script;
  use a ``.templates`` directory instead. (`#17`_)

**Fixed**

- Order of templated dicts should now be deterministic for
  all Python versions. (`#14`_)

.. _#14: https://github.com/nengo/nengo-bones/pull/14
.. _#17: https://github.com/nengo/nengo-bones/pull/17
.. _#18: https://github.com/nengo/nengo-bones/pull/18

0.1.0 (April 15, 2019)
======================

Initial release of NengoBones!
Thanks to all of the contributors for making this possible!

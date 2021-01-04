# pylint: disable=missing-docstring

__copyright__ = "2018-2021, Applied Brain Research"
__license__ = "Free for non-commercial use; see LICENSE.rst"

from . import config, templates
from .version import version as __version__

all_sections = [
    "travis_yml",
    "codecov_yml",
    "docs_conf_py",
    "setup_cfg",
    "setup_py",
    "contributing_rst",
    "contributors_rst",
    "license_rst",
    "manifest_in",
    "pre_commit_config_yaml",
    "pyproject_toml",
]

all_files = [
    ".travis.yml",
    ".codecov.yml",
    "docs/conf.py",
    "setup.cfg",
    "setup.py",
    "CONTRIBUTING.rst",
    "CONTRIBUTORS.rst",
    "LICENSE.rst",
    "MANIFEST.in",
    ".pre-commit-config.yaml",
    "pyproject.toml",
]

# pylint: disable=missing-docstring

__copyright__ = "2018-2019, Applied Brain Research"
__license__ = "Free for non-commercial use; see LICENSE.rst"

from nengo_bones.version import version as __version__

from nengo_bones.config import load_config

all_templated_files = {
    "docs/conf.py": "docs_conf_py",
    ".codecov.yml": "codecov_yml",
    ".gitignore": "gitignore",
    ".travis.yml": "travis_yml",
    "CONTRIBUTING.rst": "contributing_rst",
    "CONTRIBUTORS.rst": "contributors_rst",
    "LICENSE.rst": "license_rst",
    "MANIFEST.in": "manifest_in",
    "setup.cfg": "setup_cfg",
    "setup.py": "setup_py",
    "version.py": "version_py",  # TODO: how to incorporate pkg_name ?
}

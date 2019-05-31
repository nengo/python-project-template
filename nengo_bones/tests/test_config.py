# pylint: disable=missing-docstring

import os

import pytest

from nengo_bones import config
from nengo_bones.tests import utils


def test_find_config():
    assert config.find_config() == os.path.join(os.getcwd(), ".nengobones.yml")


def test_fill_defaults():
    init_cfg = {
        "travis_yml": {"jobs": [{"script": "docs-test"}]},
        "codecov_yml": {},
        "version": {
            "major": 3, "minor": 2, "patch": 1, "release": False,
        }
    }
    config.fill_defaults(init_cfg)

    assert init_cfg["travis_yml"]["python"] == "3.6"
    assert init_cfg["travis_yml"]["global_vars"] == {}
    assert init_cfg["travis_yml"]["pypi_user"] is None
    assert init_cfg["travis_yml"]["deploy_dists"] == ["sdist"]

    assert init_cfg["travis_yml"]["jobs"][0]["apt_install"] == ["pandoc"]

    assert init_cfg["codecov_yml"]["skip_appveyor"]
    assert init_cfg["codecov_yml"]["abs_target"] == "auto"
    assert init_cfg["codecov_yml"]["diff_target"] == "100%"

    assert init_cfg["version"]["full"] == "3.2.1.dev0"


def test_validate_config():
    mandatory = [
        "project_name", "pkg_name", "repo_name", "travis_yml.jobs",
        "version", "version.major", "version.minor", "version.patch",
        "version.release",
    ]
    init_cfg = {"travis_yml": {}}
    for entry in mandatory:
        with pytest.raises(KeyError, match="must define %s" % entry):
            config.validate_config(init_cfg)

        keys = entry.split(".")
        tmp = init_cfg
        for key in keys[:-1]:
            tmp = tmp[key]
        tmp[keys[-1]] = {}

    config.validate_config(init_cfg)

    init_cfg["ci_scripts"] = {}

    # error when template not defined
    test_cfg = {}
    init_cfg["ci_scripts"] = [test_cfg]
    with pytest.raises(KeyError, match="must define 'template'"):
        config.validate_config(init_cfg)
    test_cfg["template"] = "test"

    # error when pip_install is a string instead of list
    test_cfg["pip_install"] = "pip_req"
    with pytest.raises(TypeError, match="pip_install should be a list"):
        config.validate_config(init_cfg)
    test_cfg["pip_install"] = ["pip_req"]

    # error when pre_commands is a string instead of list
    test_cfg["pre_commands"] = "command"
    with pytest.raises(TypeError, match="pre_commands should be a list"):
        config.validate_config(init_cfg)


def test_missing_config(tmpdir):
    with pytest.raises(RuntimeError, match="Could not find conf_file"):
        config.load_config(tmpdir.join(".does-not-exist.yml"))


def test_load_config(tmpdir):
    truth = {
        "project_name": "Dummy",
        "pkg_name": "dummy",
        "repo_name": "dummyorg/dummy",
        "version": {
            "major": 3,
            "minor": 2,
            "patch": 1,
            "release": False,
            "full": "3.2.1.dev0",
        },
        "author": "A Dummy",
        "author_email": "dummy@dummy.com",
        "copyright_start": 0,
        "copyright_end": 1,
        "ci_scripts": [
            {"template": "static",
             "pip_install": ["static_pip0", "static_pip1"]}
        ],
        "travis_yml": {
            "python": "6.0",
            "global_vars": {
                "TEST_VAR": "test var val"},
            "pypi_user": "dummy_pypi_user",
            "deploy_dists": [
                "sdist",
                "bdist_wheel"
            ],
            "jobs": [{"script": "static", "language": "generic"}],
            "bones_install": "nengo-bones",
        },
        "codecov_yml": {
            "skip_appveyor": False,
            "abs_target": "test_abs",
            "diff_target": "test_diff"
        },
    }

    utils.write_file(tmpdir, ".nengobones.yml", """
        project_name: Dummy
        pkg_name: dummy
        repo_name: dummyorg/dummy
        version:
          major: 3
          minor: 2
          patch: 1
          release: false
        author: A Dummy
        author_email: dummy@dummy.com
        copyright_start: 0
        copyright_end: 1

        ci_scripts:
          - template: static
            pip_install:
              - static_pip0
              - static_pip1

        travis_yml:
          python: "6.0"
          global_vars:
            TEST_VAR: test var val
          pypi_user: dummy_pypi_user
          deploy_dists:
            - sdist
            - bdist_wheel
          jobs:
            - script: static
              language: generic

        codecov_yml:
          skip_appveyor: false
          abs_target: test_abs
          diff_target: test_diff
        """)

    loaded = config.load_config(tmpdir.join(".nengobones.yml"))

    try:
        assert loaded == truth
    except AssertionError:  # pragma: no cover
        print("loaded")
        print("\n".join("%s: %s" % (k, v) for k, v in loaded.items()))
        print("truth")
        print("\n".join("%s: %s" % (k, v) for k, v in truth.items()))
        raise

    # check loading from cwd
    cwd = os.getcwd()
    os.chdir(str(tmpdir))
    try:
        loaded = config.load_config()
    finally:
        os.chdir(cwd)

    assert loaded == truth

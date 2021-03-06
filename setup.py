#!/usr/bin/env python

# Automatically generated by nengo-bones, do not edit this file directly

import io
import pathlib
import runpy

try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "'setuptools' is required but not installed. To install it, "
        "follow the instructions at "
        "https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py"
    )


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


root = pathlib.Path(__file__).parent
version = runpy.run_path(str(root / "nengo_bones" / "version.py"))["version"]

install_req = [
    "black>=20.8b0",
    "click>=7.0",
    "codespell>=2.0.0",
    "flake8>=3.7.7",
    "jinja2>=2.11",
    "jupyter>=1.0.0",
    "pylint>=2.5.1",
    "pyyaml>=5.1",
    "requests>=2.21",
]
docs_req = []
optional_req = []
tests_req = []

setup(
    name="nengo-bones",
    version=version,
    author="Applied Brain Research",
    author_email="info@appliedbrainresearch.com",
    packages=find_packages(),
    url="https://www.nengo.ai/nengo-bones",
    include_package_data=True,
    license="Free for non-commercial use",
    description="Tools for managing Nengo projects",
    long_description=read("README.rst", "CHANGES.rst"),
    zip_safe=False,
    install_requires=install_req,
    extras_require={
        "all": docs_req + optional_req + tests_req,
        "docs": docs_req,
        "optional": optional_req,
        "tests": tests_req,
    },
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "bones-generate=nengo_bones.scripts.generate_bones:main",
            "bones-check=nengo_bones.scripts.check_bones:main",
            "bones-pr-number=nengo_bones.scripts.pr_number:main",
            "bones-format-notebook=nengo_bones.scripts.format_notebook:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Nengo",
        "Intended Audience :: Developers",
        "License :: Free for non-commercial use",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
    ],
)

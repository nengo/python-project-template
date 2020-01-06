# -*- coding: utf-8 -*-
#
# Automatically generated by nengo-bones, do not edit this file directly

import os

import nengo_bones

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "nengo_sphinx_theme",
    "nengo_sphinx_theme.ext.redirects",
    "numpydoc",
    "sphinx_click.ext",
]

# -- sphinx.ext.autodoc
autoclass_content = "both"  # class and __init__ docstrings are concatenated
autodoc_default_options = {"members": None}
autodoc_member_order = "bysource"  # default is alphabetical

# -- sphinx.ext.doctest
doctest_global_setup = """
import nengo_bones
# Testing that doctest_setup works
# with multiple lines
"""

# -- sphinx.ext.intersphinx
intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy", None),
    "python": ("https://docs.python.org/3", None),
    "click": ("https://click.palletsprojects.com/en/7.x", None),
}

# -- sphinx.ext.todo
todo_include_todos = True

# -- numpydoc config
numpydoc_show_class_members = False

# -- nbsphinx
nbsphinx_timeout = -1

# -- sphinx
nitpicky = True
exclude_patterns = [
    "_build",
    "**/.ipynb_checkpoints",
    "tests/test-example.ipynb",
]
linkcheck_timeout = 30
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
linkcheck_ignore = [r"http://localhost:\d+"]
linkcheck_anchors = True
default_role = "py:obj"
pygments_style = "sphinx"
suppress_warnings = ["image.nonlocal_uri"]

project = "Nengo Bones"
authors = "Applied Brain Research"
copyright = "2018-2020 Applied Brain Research"
version = ".".join(nengo_bones.__version__.split(".")[:2])  # Short X.Y version
release = nengo_bones.__version__  # Full version, with tags

# -- HTML output
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "nengo_sphinx_theme"
html_title = "Nengo Bones {0} docs".format(release)
htmlhelp_basename = "Nengo Bones"
html_last_updated_fmt = ""  # Default output format (suppressed)
html_show_sphinx = False
html_favicon = os.path.join("_static", "favicon.ico")
html_theme_options = {
    "nengo_logo": "general-full-light.svg",
    "nengo_logo_color": "#a8acaf",
    "analytics_id": "UA-41658423-2",
}
html_redirects = [
    ("changelog.html", "changes.html"),
]

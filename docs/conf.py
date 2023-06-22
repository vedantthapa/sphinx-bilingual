# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-bilingual'
copyright = '2023, Vedant Thapa'
author = 'Vedant Thapa'

# The full version, including alpha/beta/rc tags
release = "0.1"


# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "sphinx.ext.githubpages",
]


templates_path = ["_templates"]
exclude_patterns = []
html_theme = "furo"
html_static_path = ["_static"]


# auto-api configurations
autoapi_dirs = ["../src/"]


# Add support for multilingual documentation
locale_dirs = ['locale/']
gettext_compact = False

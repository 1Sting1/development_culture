import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Development Culture'
copyright = 'Maksim Kotelnikov'
author = 'Maksim Kotelnikov'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Language settings -------------------------------------------------------
language = 'ru'

# -- Autodoc settings -------------------------------------------------------
master_doc = 'index'

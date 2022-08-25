# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# import sphinx_redactor_theme
project = 'MangrovesDB'
copyright = '2022, Mangroves Labs'
author = 'Mohammad SBeni, Navid Haghighat'

# The full version, including alpha/beta/rc tags
release = '0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'sphinx_code_tabs',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'sphinxemoji.sphinxemoji',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_redactor_theme'
# html_theme_path = [sphinx_redactor_theme.get_html_theme_path()]
# html_theme = 'groundwork'  # furo
html_theme = "sphinx_rtd_theme"
# html_theme = "press"
# html_theme_options = {
#     "external_links": [
#         {"url": "https://mgdb.io", "name": "Website"},
#     ],
#     "navbar_align": "left",
#     "page_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
#     "navbar_center": ["navbar-nav"],
#     "navbar_end": ["theme-switcher", "navbar-icon-links.html", "search-field.html"],
#     "show_toc_level": 1,
#     "github_url": "https://github.com/mangrovesDB/mangroves",
#     "twitter_url": "https://twitter.com/MangrovesDB",
# }
# html_theme_options = {
#     "external_links": [
#         ("Website", "https://mgdb.io"),
#         #("Github", "https://github.com/mangrovesDB/mangroves"),
#     ]
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Logo
# html_logo = "logo_colorless.png"
# html_theme_options = {
#     'logo_only': True,
#     'display_version': False,
# }
# html_css_files = [
#     "css/installer_widget.css",
# ]

# html_js_files = ["js/installer_widget.js"]

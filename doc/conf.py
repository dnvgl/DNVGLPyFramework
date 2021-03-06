# -*- coding: utf-8 -*-
# DNVGLPyFramework documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 17 16:46:32 2009.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import sys

# Third party libraries.
import py
import sphinx_bootstrap_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinxcontrib.autoprogram',
    'sphinx.ext.intersphinx', 'sphinx.ext.autosummary', 'sphinx.ext.doctest',
    'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig', 'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram', 'sphinx.ext.autosummary', 'numpydoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'DNVGLPyFramework'
copyright = '2010, DNV GL SE'
author = u'Berthold Höllmann (DNV GL SE)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(
    py.path.local('../version.txt').read().strip().split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = py.path.local('../version.txt').read().strip()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'  # 'alabaster'  # 'classic'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_logo = "_static/logo.png"

html_theme_options = {
    # 'logo': 'logo.png',
    # 'logo_name': True,
    # 'page_width': None,
    # 'sidebar_width': '20%',
}


def setup(app):
    app.add_stylesheet("custom.css")


html_favicon = "favicon_DNVGL.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'dnvglpyframeworkdoc'

# -- Options for LaTeX output ---------------------------------------------
latex_engine = "xelatex"

latex_keep_old_macro_names = False

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    'papersize': 'a4paper',

    'fontpkg': '''\\usepackage{dnvgl}''',
    'fncychap': '',
    # 'maketitle': '',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
    # 'releasename': "",
    # 'babel': '',
    # 'printindex': '',
    'fontenc': '',
    'inputenc': '',
    # ,DIV=14,BCOR=2mm,headinclude=true,footinclude=false
    'classoptions': 'cmyk,english,noscrpage',
    'utf8extra': '',
    # 'footer': '\\textcopyright DNV GL SE',
    # Additional stuff for the LaTeX preamble.
    'preamble': '''\\hypersetup{%
    pdftex,%
    unicode=true,%
    pdftitle={\\texttt{DNVGLPyFramework}},%
    pdfsubject={Some local framework definitions.},%
    pdfauthor={Berthold Höllmann <berthold.hoellmann@dnvgl.com>},%
    pdfkeywords={DNV GL,Python,framwork},%
    bookmarks=true}
\\makeatletter
\\fancypagestyle{normal}{
  \\fancyhf{}
  \\fancyfoot[LE,RO]{{\\py@HeaderFamily\\thepage}}
  \\fancyfoot[LO]{{\\py@HeaderFamily\\nouppercase{\\rightmark}}}
  \\fancyfoot[RE]{{\\py@HeaderFamily\\nouppercase{\\leftmark}}}
  % \\fancyhead[LE,RO]{{\\py@HeaderFamily \\@title, \\py@release }}
  \\fancyhead{} % {\\py@HeaderFamily \\@title, \\py@release }}
  \\renewcommand{\\headrulewidth}{0.pt}
  \\renewcommand{\\footrulewidth}{0.4pt}
}
\\makeatother
\\setcounter{secnumdepth}{5}
\\setcounter{tocdepth}{5}
'''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'dnvglpyframwork.tex', u'DNVGLPyFramework Documentation',
     author, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'dnvgl.framework', u'DNVGLPyFramework documentation',
              [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'DNVGLPyFramwork', 'DNVGLPyFramework Documentation', author,
     'DNVGLPyFrameworl', 'Misc. helper for python.', 'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

inheritance_graph_attrs = dict(ratio='fill', size='"14.0 18.0"', fontsize=20)
inheritance_node_attrs = dict(fontsize=20, height=.80)
inheritance_node_attrs = dict(
    shape='ellipse',
    fontsize=14,
    height=0.75,
    color='dodgerblue1',
    style='filled')

graphviz_output_format = 'svg'

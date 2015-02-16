# -*- coding: utf-8 -*-

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import sys

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


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../setup_utils'))
sys.path.append(os.path.abspath('.'))

import dnvgl.setup_utils.version as my_version  # isort:skip

autodoc_default_flags = [
    'members', 'undoc-members', 'private-members', 'special-members',
    'inherited-members', 'show-inheritance']

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',
    'numpydoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'DNVGLPyFramework'
copyright = '2010, DNV GL SE'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
VERSION = my_version.Version('../version.txt')
version = VERSION.base_version
# The full version, including alpha/beta/rc tags.
release = VERSION.base_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'dnvglpyframeworkdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # alles loeschen
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    'fontpkg': '',
    # 'fontpkg': r'''\usepackage{dnvgl}''',
    'fncychap': '',
    'fancyhdr': '',
    # 'maketitle': '',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
    # 'releasename': "",
    # 'babel': '',
    # 'printindex': '',
    'fontenc': '',
    'inputenc': '',
    'classoptions': 'cmyk,english,noscrpage',  # ,DIV=14,BCOR=2mm,headinclude=true,footinclude=false
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
\\activateareas % \\usepackage{typearea}
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
'''
}
#     A dictionary mapping 'howto' and 'manual' to names of real
#     document classes that will be used as the base for the two
#     Sphinx classes. Default is to use 'article' for 'howto' and
#     'report' for 'manual'.
latex_docclass = {'howto': 'dnvglartcl', 'manual': 'dnvglreprt'}
# latex_docclass = {'howto': 'scrartcl', 'manual': 'scrreprt'}

# \usepackage{fontspec}
# \setmainfont[ItalicFont={Asap Italic}, BoldFont={Asap Bold}]{Asap}
# \setmonofont[ItalicFont={Source Sans Pro Italic},%
#              BoldFont={Source Sans Pro Bold},%
#              BoldItalicFont={Source Sans Pro Bold Italic}]{Source Sans Pro}}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'dnvglpyframwork.tex', 'DNVGLPyFramework Documentation',
     'Berthold Höllmann', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'dnvgl_framework', 'DNVGLPyFramework documentation',
     ['DNV GL SE (Berthold Höllmann)'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'DNVGLPyFramwork', 'DNVGLPyFramework Documentation',
   'DNV GL SE (Berthold Höllmann)', 'DNVGLPyFrameworl', 'Misc. helper for python.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'DNVGLPyFamework'
epub_author = 'Berthold Höllmann'
epub_publisher = 'DNV GL SE'
epub_copyright = '2013, DNV GL SE'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}


# This value selects what content will be inserted into the main body
# of an autoclass directive. The possible values are:
#   "class"
#       Only the class’ docstring is inserted. This is the default. You
#       can still document __init__ as a separate method using
#       automethod or the members option to autoclass.
#   "both"
#       Both the class’ and the __init__ method’s docstring are
#       concatenated and inserted.
#   "init"
#       Only the __init__ method’s docstring is inserted.
#autoclass_content = 'class'

# The path to the JavaScript file to include in the HTML files in
# order to load MathJax.
#
# The default is the http:// URL that loads the JS files from the
# MathJax CDN. If you want MathJax to be available offline, you have
# to donwload it and set this value to a different path.
#
# The path can be absolute or relative; if it is relative, it is
# relative to the _static directory of the built docs.
#
# For example, if you put MathJax into the static path of the Sphinx
# docs, this value would be MathJax/MathJax.js. If you host more than
# one Sphinx documentation set on one server, it is advisable to
# install MathJax in a shared location.
#
# You can also give a full http:// URL different from the CDN URL.
mathjax_path = "http://srverc/~hoel/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

# This value is a list of autodoc directive flags that should be
# automatically applied to all autodoc directives. The supported flags
# are 'members', 'undoc-members', 'private-members',
# 'special-members', 'inherited-members' and 'show-inheritance'.
#
# If you set one of these flags in this config value, you can use a
# negated form, 'no-flag', in an autodoc directive, to disable it
# once. For example, if autodoc_default_flags is set to ['members',
# 'undoc-members'], and you write a directive like this:
#
#  .. automodule:: foo
#     :no-undoc-members:
#
# the directive will be interpreted as if only :members: was given.
autodoc_default_flags = [
    'members',
    'undoc-members',
    'private-members',
    # 'special-members',
    # 'inherited-members',
    'show-inheritance']

# This value selects if automatically documented members are sorted
# alphabetical (value 'alphabetical'), by member type (value
# 'groupwise') or by source order (value 'bysource'). The default is
# alphabetical.
#
# Note that for source order, the module must be a Python module with
# the source code available.
autodoc_member_order = 'bysource'

# This value selects what content will be inserted into the main body
# of an autoclass directive. The possible values are:
#
#    "class"
#        Only the class’ docstring is inserted. This is the default.
#        You can still document __init__ as a separate method using
#        automethod or the members option to autoclass.
#    "both"
#        Both the class’ and the __init__ method’s docstring are
#        concatenated and inserted.
#    "init"
#        Only the __init__ method’s docstring is inserted.
#autoclass_content = "both"

# WARNING: toctree references unknown document
# You may be able to get rid of these warning by setting
# numpydoc_show_class_members = False in your conf.py. This worked for
# me at least. The real problem is that the
# numpydoc.docscrape_sphinx.SphinxDocString._str_member_list() method
# produces autosummary code which does not work because it gets
# inserted after autosummary runs in the sphinx pipeline. (Or at least
# that is my current best guess.)
numpydoc_show_class_members = False

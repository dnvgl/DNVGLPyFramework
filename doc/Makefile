# Copyright (C) 2007 by Germanischer Lloyd AG

# ======================================================================
# Task      Generate documentation for Tribon XML tools.
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   tribonXML converters
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

DOC_HOST=www-intern
DOC_DIR=/export/WWW-Intern/htdocs/pool/ho/software/info/tribonXML_convert

all test:

doc:
	[ -d tribon_doc ] || mkdir tribon_doc
	PYTHONPATH=../src python -c "from epydoc.cli import cli ; cli()" --config tribon.ini -v --inheritance included
	chmod -R a+r tribon_doc
	scp -r tribon_doc/* $(DOC_HOST):$(DOC_DIR)


# Local Variables:
# compile-command:"make"
# coding:utf-8
# End:

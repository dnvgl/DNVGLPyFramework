# Copyright (C) 2007 by Germanischer Lloyd AG

# ======================================================================
# Module    Makefile
# Task      Generate documentation for Tribon XML tools.
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   tribonXML converters
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

all test:
	@echo "Nothing to be done for $@"

doc:
	[ -d tribon_doc ] || mkdir tribon_doc
	PYTHONPATH=../src python -c "from epydoc.cli import cli ; cli()" --config tribon.ini -v --inheritance included
	chmod -R a+r tribon_doc
	#scp -r tribon_doc/* www-intern:/export/WWW-Intern/htdocs/pool/ho/software/info/temp/tribon


# Local Variables:
# compile-command:"make"
# coding:utf-8
# End:

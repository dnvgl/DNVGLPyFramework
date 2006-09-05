# Copyright (C) 2006 by Germanischer Lloyd AG

# ======================================================================
# Module    Makefile
# Task      makefile for tests for tx2glshipmodel
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   TX2GlShipModel
# ----------------------------------------------------------------------
# Status    $State$
# Date      $Date$
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

PYPLAT=$(shell python -c "from distutils import util; print util.get_platform()")
PYVER=$(shell python -c "import sys ; print sys.version[:3]")

BPATH=../build/lib#.$(PYPLAT)-$(PYVER)
PYTHON = PYTHONPATH=$(BPATH) python #-v

TESTS = 
TESTS += rasterfile_test
TESTS += material_test
TESTS += tx2glshipmodel_test
TESTS += proftable_test
TESTS += coorsys_test
TESTS += tx2glshipmodel_app_test
TESTS += tx2dfile_app_test

PY = $(shell /bin/find ../src -name \*.py)
SRC = $(shell /bin/find ../src -name \*.c)

all:
	true

test:	build $(TESTS)

build:
	cd .. ; make build

tx2glshipmodel_app_test:	../data/TribonXML_3D/basic_ideal.xml	\
		$(PY)	../app/tx2glshipmodel
	$(MAKE) build
	$(PYTHON) ../app/tx2glshipmodel $<
	touch $@

tx2dfile_app_test:	../data/ToPATRAN/general_information.xml	\
		$(PY)	../app/tx2dfile
	$(MAKE) build
	$(PYTHON) ../app/tx2dfile $<
	touch $@

%_test:	%_test.py	$(PY)
	$(MAKE) build
	$(PYTHON) $<
	touch $@

%_dtest:	%.py	$(PY)
	$(PYTHON) $<
	touch $@

clean:
	rm -f $(TESTS) core

vpath %.py $(shell /bin/find ../src -type d)

# Local Variables: ***
# compile-command:"make test" ***
# coding:utf-8 ***
# End: ***

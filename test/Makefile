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
TESTS += tx2glshipmodel_test
TESTS += default_test

PY = $(shell find ../src -name \*.py)
SRC = $(shell find ../src -name \*.c)

all:
	@echo 'PASS'

test:	build $(TESTS)

build:
	cd .. ; make build

default_test:	../data/TribonXML_3D/basic_ideal.xml	$(PY)
	$(PYTHON) ../src/tx2glshipmodel/tx2glshipmodel.py

%_test:	%_test.py	$(PY)
	$(PYTHON) $<
	touch $@

clean:
	rm -f $(TESTS) core


# Local Variables: ***
# compile-command:"make test" ***
# coding:utf-8 ***
# End: ***

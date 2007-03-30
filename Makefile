# Copyright (C) 2006 by Germanischer Lloyd AG

# ======================================================================
# Task      makefile for tribonXML converters
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   tribonXML converters
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

all:	build
	@echo "nothing to do"

test: build
	make -C test  test

doc:
	$(MAKE) -C doc doc

%_test: build
	make -C test $@

%: build
	make -C test $@

build:
	python setup.py build

.PHONY: build

# Local Variables:
# compile-command:"make test"
# coding:utf-8
# End:

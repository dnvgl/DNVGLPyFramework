# Copyright (C) 2010 by Germanischer Lloyd SE

# ======================================================================
# Task      makefile for GLPyFramework
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   GLPyFramework converters
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

all:	build
	@echo "nothing to do"

test: build
	make -C test test

doc:
	$(MAKE) -C doc html

sdist:
	python setup.py sdist

bdist_egg:
	python setup.py bdist_egg

%_test:
	make -C test $@

%:
	make -C test $@

build install:
	python setup.py $@

IGN = $(shell [ -n "$$(svn propget svn:ignore .)" ] && echo "$$(svn propget svn:ignore .)")
clean:
	[ -n "$(IGN)" ] && $(RM) -r $(IGN) || true
	$(MAKE) -C test clean

TAGS:
	find src -name \*.py
	( set -e ;							\
  find src -name \*.c -o -name \*.h -o -name \*.py -o -name \*.pyx	\
    -o -name \*.pxi | xargs etags )

check_clean:
	svn update
	[ -z "$$(svn status -q)" ] || (echo "Working copy is not pristine, exiting.";false)

dist:	check_clean sdist bdist_egg
	devpi --with-docs upload
	devpi test DNVGLPyFramework -e py27,py34

.PHONY: build
.PHONY: doc
.PHONY: test

# Local Variables:
# compile-command:"make test"
# coding:utf-8
# End:

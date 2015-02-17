# -*- coding: utf-8 -*-

# Copyright © 2010 by DNV GL SE

# Compile and distribute DNVGLPyFramework.

# ID: $Id$
# $Date$
# $Revision$
# Author Berthold Höllmann <berthold.hoellmann@dnvgl.com>

SHELL = /bin/sh

all:	build
	@echo "nothing to do"

test: build
	make -C test test

doc:
	$(MAKE) -C doc html

sdist:
	python setup.py $@ --formats gztar,bztar,zip

bdist_egg build_sphinx:
	python setup.py $@

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

dist:	check_clean test sdist bdist_egg build_sphinx
	devpi upload --no-vcs --with-docs
	devpi test DNVGLPyFramework -e py27,py34

.PHONY: build
.PHONY: doc
.PHONY: test

# Local Variables:
# mode: makefile
# ispell-local-dictionary:"english"
# compile-command:"make test"
# End:

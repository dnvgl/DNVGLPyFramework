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
	make -C test test

doc:
	$(MAKE) -C doc html

%_test: 
	make -C test $@

%: 
	make -C test $@

build:
	python setup.py build

IGN = $(shell [ -n "$$(svn propget svn:ignore .)" ] && echo "$$(svn propget svn:ignore .)")
clean:
	[ -n "$(IGN)" ] && rm -f $(IGN) || true
	$(MAKE) -C test clean

TAGS:
	find src -name \*.py 
	( set -e ;										\
          find src -name \*.c -o -name \*.h -o -name \*.py -o -name \*.pyx -o -name \*.pxi 	\
	  | xargs etags )

.PHONY: build
.PHONY:	doc

# Local Variables:
# compile-command:"make test"
# coding:utf-8
# End:

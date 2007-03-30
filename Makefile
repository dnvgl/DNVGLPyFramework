# Copyright (C) 2006 by Germanischer Lloyd AG

# ======================================================================
# Module    Makefile
# Task      makefile for tx2glshipmodel
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   TX2GlShipModel
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

all:	build
	@echo "nothing to do"

test: build
	cd test ; make test

%_test: build
	cd test ; make $@

%_dtest: build
	cd test ; make $@

%: build
	cd test ; make $@

build:
	python setup.py build

.PHONY: build

# Local Variables:
# compile-command:"make test"
# coding:utf-8
# End:

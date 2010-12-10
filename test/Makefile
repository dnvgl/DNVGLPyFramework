# Copyright (C) 2010 by Germanischer Lloyd SE

# ======================================================================
# Task      makefile for tests for GLPyFramework library
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   GPPyFramwork
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

PYPLAT=$(shell python -c "from distutils import util; print util.get_platform()")
PYVER=$(shell python -c "import sys ; print sys.version[:3]")

USE_COMPILED=0

ifeq ($(USE_COMPILED),1)
  export BASE_PATH=../src/tribon
  BPATH=../build/lib:../build/lib.$(PYPLAT)-$(PYVER)
else
  BPATH=../src
endif
GLGEOMETRY_DIR=/data/tmp/hoel/GLGeometry
GLGEOMETRY_PATH=$(GLGEOMETRY_DIR)/build/lib:$(GLGEOMETRY_DIR)/build/lib.$(PYPLAT)-$(PYVER)
TRIBON_DIR=/data/tmp/hoel/tribonXML_convert
TRIBON_PATH=$(TRIBON_DIR)/build/lib:$(TRIBON_DIR)/build/lib.$(PYPLAT)-$(PYVER)

PYTHON = PYTHONPATH=$(BPATH):$(GLGEOMETRY_PATH):$(TRIBON_PATH) python #-v

PYBASE = ../src
PY = $(shell $(FINDDIR)find $(PYBASE) -name \*.py -not -name .\#\* -and -not -name config.py )
UTESTS = $(subst /,.,$(subst $(PYBASE)/,,$(patsubst %.py,%_test,$(PY))))

ifeq ("$GL_ARCH","")
FINDDIR=/bin/
endif


TESTS  = $(UTESTS)

all:
	@true

test:	py_dep build	$(TESTS)

test_all:	test	$(BIG_TESTS)

build:
	make -C .. build

%_test:	%_test.py
	$(PYTHON) $< -v
	touch $@

%_rtest:	%.py	$(PY)	validate_hcm.py
	$(PYTHON) $<
	touch $@

py_dep: gen_py_dep.py $(addsuffix .py,$(UTESTS))
	$(PYTHON) $^ $(PYBASE) > $@

include py_dep

clean:
	rm -f $(TESTS) $(BIG_TESTS) core
	rm -f general_information.sg2 *.glm *.hcf *.hcz
	-find .. -name \*.pyc | xargs rm
	svn propget svn:ignore | xargs rm -rf
	-find . -type l -and -not -name .\#\* | xargs rm

%_test.py:	__generic_test_.py
	[ -f $@ ] || ln -s $< $@

vpath %.py $(shell $(FINDDIR)find ../src -type d|grep -v .svn)

# Local Variables:
# mode:makefile
# mode:flyspell
# ispell-local-dictionary:"en"
# compile-command:"make"
# coding:utf-8
# End:

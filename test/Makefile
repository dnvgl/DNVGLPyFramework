# -*- coding: utf-8 -*-

# Copyright © 2010 by DNV GL SE

# Executing tests for the DNVGLPyFramework library.

# ID: $Id$"
# $Date$
# $Revision$
# Author Berthold Höllmann <berthold.hoellmann@dnvgl.com>

SHELL = /bin/sh

PYPLAT=$(shell python -c "from distutils import util; print util.get_platform()")
PYVER=$(shell python -c "import sys ; print sys.version[:3]")

USE_COMPILED=0

ifeq ($(USE_COMPILED),1)
  export BASE_PATH=../dnvgl_framework
  BPATH=../build/lib:../build/lib.$(PYPLAT)-$(PYVER)
else
  BPATH=../
endif

_empty:=
_space:= $(_empty) $(_empty)
PYTHON = PYTHONPATH=$(BPATH):$(subst $(_space),:,$(shell ls -d ../.eggs/*.egg)) python -tt

PYBASE = ../

ifeq ("$GL_ARCH","")
FINDDIR=/bin/
endif

ifeq ("$(shell uname -o)", "Cygwin")
  U2DPATH=cygpath --mixed
  D2UPATH=cygpath
else
  U2DPATH=echo
  D2UPATH=echo
endif

all:
	@true

test: build	pytest

build:
	make -C .. build

PYTESTPATH=../dnvgl/
GEN_COV=--cov-config .coveragerc $(patsubst %,--cov %,$(PYTESTPATH))    \
  --cov-report term-missing --cov-report html           \
  --cov-report xml --cov-report annotate
PY=$(filter-out %_flymake.py,$(shell $(D2UPATH) $(shell find $(PYTESTPATH) -name \*.py)))
pytest: $(PY)
	$(PYTHON) -m pytest $(GEN_COV) --pep8   \
  --doctest-modules --capture=sys $(PYTESTPATH)
	touch $@

clean:
	[ -n "$(shell svn propget svn:ignore | head -1)" ] &&	\
  svn propget svn:ignore |					\
  while read d ; do						\
    [ -n "$$d" ] && find $$d "$$d" -maxdepth 0 2> /dev/null;	\
  done |							\
  sort -u | tr '\n' '\000' | xargs -0 $(RM) -r || true

vpath %.py $(shell $(FINDDIR)find .. -type d|grep -v .svn)

# Local Variables:
# mode: makefile
# ispell-local-dictionary:"english"
# compile-command:"make test"
# End:

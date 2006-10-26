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

#BPATH=../build/lib.$(PYPLAT)-$(PYVER)
#BPATH=../build/lib
BPATH=../src
PYTHON = PYTHONPATH=$(BPATH) python #-v

TESTS = $(patsubst %.py,%,$(wildcard *_test.py))
TESTS += tx2glshipmodel_app_test
TESTS += tx2dfile_app_test
#TESTS += tx2glshipmodel_big_test

ifeq ("$GL_ARCH","")
FINDDIR=/bin/
endif

PY = $(shell $(FINDDIR)find ../src -name \*.py)
SRC = $(shell $(FINDDIR)find ../src -name \*.c)

AKER_DIR=//glf/Vol1/DATA/FBE/ERC/Projekte/Interfaces/Project/Beispieldaten/Aker

AKER_2D_  = $(wildcard $(AKER_DIR)/*_2D.xml)
AKER_3D_  = $(wildcard $(AKER_DIR)/*_3D.xml)
AKER_3D_  = $(wildcard $(AKER_DIR)/3D/*.xml)
AKER_2D = $(addprefix Aker/,$(patsubst %.xml,%.sg2,$(notdir $(AKER_2D_))))
AKER_3D = $(addprefix Aker/,$(patsubst %.xml,%_3D.glm,$(notdir $(AKER_3D_))))

all:
	true

test:	build $(TESTS)

build:
	cd .. ; make build

tx2glshipmodel_app_test:	../data/TribonXML_3D/basic_small.xml	\
		$(PY)	../app/tx2glshipmodel
	$(MAKE) build
	$(PYTHON) ../app/tx2glshipmodel $< $(basename $(<F)).glm
	diff $(basename $(<F)).glm ref/$(basename $(<F)).glm
	touch $@

tx2glshipmodel_big_test:	../data/TribonXML_3D/basic_ideal.xml	\
		$(PY)	../app/tx2glshipmodel
	$(MAKE) build
	$(PYTHON) ../app/tx2glshipmodel $< $(basename $(<F)).glm
	diff $(basename $(<F)).glm ref/$(basename $(<F)).glm
	touch $@

tx2dfile_app_test:	../data/ToPATRAN/general_information.xml	\
		$(PY)	../app/tx2dfile
	$(MAKE) build
	$(PYTHON) ../app/tx2dfile $< $(basename $(<F)).sg2
	diff $(basename $(<F)).sg2 ref/$(basename $(<F)).sg2
	touch $@

%_test:	%_test.py	$(PY)
	$(MAKE) build
	$(PYTHON) $< -v
	touch $@

%_dtest:	%.py	$(PY)
	$(PYTHON) $<
	touch $@

clean:
	rm -f $(TESTS) core

AKER_ALL:	$(AKER_3D) #	$(AKER_2D)

Aker/%_3D.glm:	$(AKER_DIR)/3D/%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2glshipmodel $< $@

Aker/%_2D.sg2:	$(AKER_DIR)/%_2D.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2dfile $< $(basename $(<F)).sg2

vpath %.py $(shell $(FINDDIR)find ../src -type d)
#vpath %.xml $(AKER_DIR)

# Local Variables: ***
# compile-command:"make test" ***
# coding:utf-8 ***
# End: ***

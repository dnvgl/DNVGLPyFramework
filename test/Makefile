# Copyright (C) 2006, 2007 by Germanischer Lloyd AG

# ======================================================================
# Task      makefile for tests for tribonXML converters
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   tribonXML converters
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

PYPLAT=$(shell python -c "from distutils import util; print util.get_platform()")
PYVER=$(shell python -c "import sys ; print sys.version[:3]")

#BPATH=../build/lib.$(PYPLAT)-$(PYVER)
#BPATH=../build/lib
BPATH=../src
PYTHON = PYTHONPATH=$(BPATH) python #-v

PYBASE = ../src
UTESTS = $(subst /,.,$(subst $(PYBASE)/,,$(patsubst %.py,%_test,$(PY))))

ifeq ("$GL_ARCH","")
FINDDIR=/bin/
endif

PY = $(shell $(FINDDIR)find ../src -name \*.py)

AKER_DIR=../data/Aker

AKER_2D_ = $(wildcard $(AKER_DIR)/2D/*.xml)
AKER_3D_ = $(wildcard $(AKER_DIR)/3D/*.xml)
AKER_2D = $(addprefix Aker/,$(patsubst %.xml,%_2D.sg2,$(notdir $(AKER_2D_))))
AKER_3D = $(addprefix Aker/,$(patsubst %.xml,%_3D.glm,$(notdir $(AKER_3D_))))
AKER_3D_ANSYS = $(addprefix Aker/,$(patsubst %.xml,%_3D.mac,$(notdir $(AKER_3D_))))

HCM_TESTS  = write_pegasusxml_rtest
HCM_TESTS += basic_small_stiff.hcf
HCM_TESTS += Aker/YI9999.hcf
HCM_TESTS += spt78_3D.hcf
HCM_TESTS += spt82_3D.hcf
HCM_TESTS += spt70_3D.hcf
HCM_TESTS += spt74_3D.hcf
HCM_TESTS += Z_7000_3D.hcf
HCM_TESTS += z_9100_3D.hcf
HCM_TESTS += DA2100/da2100_3201.hcf
HCM_TESTS += DA2100/da2100_3321.hcf
HCM_TESTS += DA2100/da2100_3204.hcf
HCM_TESTS += DA2100/da2100_3389.hcf
HCM_TESTS += lm012.hcf
HCM_TESTS += basic_ideal.hcf
HCM_TESTS += basic_small.hcf
HCM_TESTS += Tribon-20080516/ED1_3D.hcf
HCM_TESTS += Tribon-20080516/ED1_3D_2.hcf
HCM_TESTS += conro_1000.hcf
HCM_TESTS += conro_2000.hcf
HCM_TESTS += conro_3000.hcf
HCM_TESTS += conro_4000.hcf
HCM_TESTS += conro_5000.hcf
HCM_TESTS += conro_6000.hcf
HCM_TESTS += conro.hcf


GLM_TESTS  = tx2glshipmodel_app_test
GLM_TESTS += DA2100/da2100_3201.glm
GLM_TESTS += DA2100/da2100_3321.glm
GLM_TESTS += DA2100/da2100_3204.glm
GLM_TESTS += DA2100/da2100_3389.glm
GLM_TESTS += DA2100/da2100_param.sg2
GLM_TESTS += Horn_20071106/li027-28-29.glm
GLM_TESTS += Horn_20071106/li027.glm
GLM_TESTS += Horn_20071106/li028.glm
GLM_TESTS += Horn_20071106/li029.glm
GLM_TESTS += Horn_20071106/li042.glm
GLM_TESTS += Horn_20071106/li043.glm
GLM_TESTS += Tribon-20080516/ED1_3D.glm
GLM_TESTS += Tribon-20080516/ED1_3D_2.glm
GLM_TESTS += SMK_sec12/lm012-idealisation.glm
GLM_TESTS += SMK_sec12/lm012.glm


MAC_TESTS  = SMK_sec12/lm012-idealisation.mac
MAC_TESTS += SMK_sec12/lm012.mac
MAC_TESTS += Horn_20071106/li027-28-29.mac
MAC_TESTS += Horn_20071106/li027.mac
MAC_TESTS += Horn_20071106/li028.mac
MAC_TESTS += Horn_20071106/li029.mac
MAC_TESTS += Horn_20071106/li042.mac
MAC_TESTS += Horn_20071106/li043.mac

li027-28-29_mac_addargs = 
li027_mac_addargs = --min-k=2200
li028_mac_addargs = --min-k=3100
li029_mac_addargs = --min-k=3700
li042_mac_addargs = --min-k=4500
li043_mac_addargs = --min-k=4900

BIG_TESTS += tx2dfile_app_test
BIG_TESTS += tx2glshipmodel_big_test

TESTS  = $(UTESTS)
TESTS += $(GLM_TESTS)
TESTS += $(BIG_TESTS)
#TESTS += $(HCM_TESTS)
#TESTS += $(MAC_TESTS)

# TESTS += DA2100_test
# TESTS += $(PEGASUS_TEST)
# TESTS += DA2100_ANSYS_test
# TESTS += Horn_20071106_test

all:
	@true

test:	py_dep build	$(TESTS)

test_all:	test	$(BIG_TESTS)

test_pegasus: $(PEGASUS_TEST)

build:
	cd .. ; make build

tx2glshipmodel_app_test:	../data/TribonXML_3D/basic_small.xml	\
		$(PY)	../app/tx2glshipmodel
	$(PYTHON) ../app/tx2glshipmodel --validate $< $(basename $(<F)).glm
	diff ref/$(basename $(<F)).glm $(basename $(<F)).glm
	touch $@

tx2glshipmodel_big_test:	../data/TribonXML_3D/basic_ideal.xml	\
		$(PY)	../app/tx2glshipmodel
	$(PYTHON) ../app/tx2glshipmodel --validate $< $(basename $(<F)).glm
	diff ref/$(basename $(<F)).glm $(basename $(<F)).glm
	touch $@

tx2dfile_app_test:	../data/ToPATRAN/general_information.xml	\
		$(PY)	../app/tx2dfile
	$(PYTHON) ../app/tx2dfile --validate $< --output $(basename $(<F)).sg2
	diff ref/$(basename $(<F)).sg2 $(basename $(<F)).sg2
	touch $@

%_test:	%_test.py
	$(PYTHON) $< -v
	touch $@

%_rtest:	%.py	$(PY)	validate_hcm.py
	$(PYTHON) $<
	touch $@

py_dep: gen_py_dep.py $(addsuffix .py,$(UTESTS))
	$(PYTHON) $^ $(PYBASE) > $@

include py_dep

AKER_ALL:	$(AKER_3D)	Aker/aker_rf.sg2	$(AKER_3D_ANSYS)

DA2100_BUILD: $(DA2100)

DA2100/%.glm:	../data/DA2100/%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2glshipmodel --validate $< $@

DA2100/%.sg2:	../data/DA2100/%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2dfile --validate $< --output $@

Aker/%_3D.glm:	$(AKER_DIR)/3D/%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2glshipmodel --validate $< $@

Aker/%_3D.mac:	$(AKER_DIR)/3D/%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2ansys $< --output=$@

Aker/aker_rf.sg2:	$(AKER_2D_) $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2dfile --validate $(AKER_2D_) --output $@

SMK_sec12/%.glm:	../data/SMK_sec12/%.xml
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2glshipmodel --validate $< $@

SMK_sec12/%.mac:	../data/SMK_sec12/%.xml
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2ansys $< --output $@

20090706/%.hcf:	../data/20090706/%.xml	%.ini	$(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2pegasus --cfg=$*.ini $<	\
		--output=$@
	$(PYTHON) validate_hcm.py $@
	touch $@

MP.hcf: $(PY) MP.ini MP.xml 										\
		MP-1.xml MP-2.xml MP-3.xml  MP-5.xml MP-6.xml MP-7.xml MP-41.xml MP-42.xml MP-44.xml
	$(PYTHON) ../app/tx2pegasus --cfg=MP.ini 							\
		MP-1.xml MP-2.xml MP-3.xml  MP-5.xml MP-6.xml MP-7.xml MP-41.xml MP-42.xml MP-44.xml	\
		--output=$@
	$(PYTHON) validate_hcm.py $@

DA2100_test:	$(PY)				\
		../data/DA2100/da2100_3201.xml	\
		../data/DA2100/da2100_param.xml
	$(PYTHON) ../app/tx2pegasus			\
		--cfg=da2100.ini			\
		../data/DA2100/da2100_3201.xml		\
		--param=../data/DA2100/da2100_param.xml	\
		--output=da2100.hcf
	$(PYTHON) validate_hcm.py da2100.hcf
	touch $@

%.ini:
	echo "not valid" > $@

Aker/%.hcf DA2100/%.hcf Tribon-20080516/%.hcf %.hcf:	%.xml	%.ini	$(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2pegasus --cfg=$*.ini $<	\
		--output=$@
	$(PYTHON) validate_hcm.py $@
	touch $@

conro.hcf conro_det.hcf:: $(PY) conro.ini
conro.hcf:: conro_1000.xml conro_2000.xml conro_3000.xml conro_4000.xml conro_5000.xml conro_6000.xml
	$(PYTHON) ../app/tx2pegasus --cfg=conro.ini $^	\
		--output=$@
	$(PYTHON) validate_hcm.py $@

conro_det.hcf:: conro_1000.xml conro_2000.xml conro_3000.xml conro_4000.xml conro_5000.xml conro_6000.xml
	$(PYTHON) ../app/tx2pegasus --cfg=conro.ini $^	\
		--detailed-contour --output=$@
	$(PYTHON) validate_hcm.py $@

DA2100_ANSYS_test:	$(PY)			\
		../data/DA2100/da2100_3201.xml
	$(PYTHON) ../app/tx2ansys			\
		../data/DA2100/da2100_3201.xml		\
		--output=da2100.mac
	touch $@

Horn_20071106/%.mac:	%.xml	$(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2ansys $< --output $@ $($*_mac_addargs)

Horn_20071106/%.glm Tribon-20080516/%.glm:	%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2glshipmodel --validate $< $@

%.glm:	%.xml $(PY)
	@[ -d ${@D} ] || mkdir ${@D}
	$(PYTHON) ../app/tx2glshipmodel --validate $< $@

TRIBON_20080516_test: $(TRIBON_20080516)
	touch $@

clean:
	rm -f $(TESTS) $(BIG_TESTS) core
	rm -f general_information.sg2 *.glm *.hcf
	-find .. -name \*.pyc | xargs rm
	svn propget svn:ignore|xargs rm -rf

vpath %.py $(shell $(FINDDIR)find ../src -type d|grep -v .svn)
vpath %.xml ../data/DA2100
vpath %.xml ../data/Horn_20071006
vpath %.xml ../data/TribonXML_3D
vpath %.xml ../data/SMK_sec12
vpath %.xml $(AKER_DIR)/
vpath %.xml $(AKER_DIR)/3D/
vpath %.xml ../data/SMK
vpath %.xml ../data/Tribon-20080516
vpath %.xml ../data
vpath %.xml ../data/Neptun
vpath %.xml ../data/Neptun-MP-20090708

# Local Variables:
# compile-command:"make test"
# coding:utf-8
# End:

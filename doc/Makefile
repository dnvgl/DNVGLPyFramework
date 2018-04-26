# -*- coding: utf-8 -*-

# Copyright © 2010 by DNV GL SE

# Generate documentation for DNVGLPyFramework.
# Makefile for Sphinx documentation.

# ID: $Id$"
# $Date$
# $Revision$
# Author Berthold Höllmann <berthold.hoellmann@dnvgl.com>

SHELL = /bin/bash

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = DNVGLPyFramework
SOURCEDIR     = .
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%.pdf:: %.dot Makefile
	dot -Tpdf $< -o $@

%.svg:: %.dot Makefile
	dot -Tsvg $< -o $@

%.png:: %.dot Makefile
	dot -Tpng $< -o $@

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%:: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

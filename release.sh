#! /bin/bash

# Copyright © 2018 by DNV GL SE

# Task  : Release latest Fortran2CHeader version

# Author: Berthold Höllmann <berthold.hoellmann@dnvgl.com>

# ID: $Id$
author="$Author$"
date="$Date$"
version="$Revision$"

set -e

# Generate source distribution files.
python setup.py sdist --format=zip,gztar

# Generate binary distribution files (egg and wheel) for
# python2.7 and 3.4.
tox

# connect to devpi (local pypi) server.
devpi use http://srverc.germanlloyd.org/devpi/dnvgl/dist

# upload distribution files to devpi server.
devpi upload dist/DNVGLPyFramework-$(cat version.txt)*

# Local Variables:
# mode: shell-script
# coding: utf-8
# compile-command: "sh release.sh"
# End:

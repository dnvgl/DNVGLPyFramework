#! /bin/bash

# Copyright © 2016 by DNV GL SE

# Task  : Testing DNVGLPyFramework

# Author: Berthold Höllmann <berthold.hoellmann@dnvgl.com>

# ID: $Id$
author="$Author$"
date="$Date$"
version="$Revision$"

set -e

# general definitions

if [ "$(uname -o)" = "Cygwin" ] ; then
    PIPCONFPATH="$(cygpath $APPDATA)/pip"
    PIPCONFEXT=pipini
    PYTHON=python.exe
else
    PIPCONFPATH=$HOME/.pip
    PIPCONF=pip.conf
    PYTHON=python$PYMAJOR
fi

# Generate index server information
get_index_server () {
    UCS=$($PYTHON -c "import sys; print ('UCS4' if sys.maxunicode > 65535 else 'UCS2')")

    if [ "$(uname -o)" = "Cygwin" ] ; then
        PIPARCH=WIN_64
    else
        if [ "$UCS" = "UCS4" ] ; then
            PIPARCH=UBUNTU_14_04_UCS4
        else
            PIPARCH=UBUNTU_14_04
        fi
    fi
    echo "http://srverc.germanlloyd.org/devpi/dnvgl/dist_$PIPARCH/+simple/"
}

aif [ ! -e "$PIPCONFPATH/$PIPCONF" ] ; then
    echo "[global]" > "$PIPCONFPATH/$PIPCONF"
    echo "trusted_host = srverc.germanlloyd.org" >> "$PIPCONFPATH/$PIPCONF"
    echo "index_url = http://srverc.germanlloyd.org/devpi/dnvgl/$PIPARCH/+simple/" >> "$PIPCONFPATH/$PIPCONF"
fi

# ensure pip configuration file exists
gen_pipconf () {
    if [ ! -e "$PIPCONFPATH/$PIPCONF" ] ; then
        if [ ! -d "$PIPCONFPATH" ] ; then
            mkdir -p "$PIPCONFPATH"
        fi
        echo "[global]" > "$PIPCONFPATH/$PIPCONF"
        echo "trusted_host = srverc.germanlloyd.org" >> "$PIPCONFPATH/$PIPCONF"
        echo "index_url = http://srverc.germanlloyd.org/devpi/dnvgl/$PIPARCH/+simple/" >> "$PIPCONFPATH/$PIPCONF"
    fi
}

# set up virtual environment for tests
virt_env () {
    pip$PYMAJOR install --index-url=$INDEX_URL --user --upgrade virtualenv

    VIRTDIR=$(echo "/tmp/DNVGLPyFramework_${TEAMCITY_PROJECT_NAME}_${TEAMCITY_BUILDCONF_NAME}_py$PYVER" | sed "s-[ ;:]-_-g")

    if [ ! -d $VIRTDIR ] ; then
        if [ "$(uname -o)" = "Cygwin" ] ; then
            virtualenv $(cygpath --windows $VIRTDIR) --python=c:/python$PYVER/python.exe
        else
            virtualenv $VIRTDIR --python=python$PYMAJOR
        fi
    fi
}

# install required packages into virtual environment
py_prep () {
    pip$PYMAJOR install --index-url=$INDEX_URL --upgrade pytest pytest-pep8 pytest-cov wheel
    if [ -e requirements$PYMAJOR.txt ] ; then
        pip$PYMAJOR install --index-url=$INDEX_URL --upgrade --requirement=requirements$PYMAJOR.txt
    fi
}

# compile source code
py_build () {
    if [ "$(uname -o)" = "Cygwin" ] ; then
        python setup.py build
    else
a        virtualenv $VIRTDIR --python=python$PYMAJOR
    fi
}

# execute tests
py_test () {
    tox -e py$PYVER -i $INDEX_URL
}

# generate basic distribution files
py_dist_bdist () {
    $PYTHON setup.py bdist bdist
}

# generate binary egg files
py_dist_egg () {
    $PYTHON setup.py bdist_egg
}

# generate binary wheel files
py_dist_wheel () {
    pip$PYMAJOR wheel .
}

# generate different distribution files
py_dist () {
    echo "##teamcity[blockOpened name='py_dist_bdist' description='Generating simple installer']"
    py_dist_bdist
    echo "##teamcity[blockClosed name='py_dist_bdist']"

    echo "##teamcity[blockOpened name='py_dist_egg' description='Generating egg installer']"
    py_dist_egg
    echo "##teamcity[blockClosed name='py_dist_egg']"

    echo "##teamcity[blockOpened name='py_dist_wheel' description='Generating wheel installer']"
    py_dist_wheel
    echo "##teamcity[blockClosed name='py_dist_wheel']"
}

# calling the defined functions

echo "##teamcity[blockOpened name='get_index_server' description='calculate pip index server path']"
INDEX_URL=$(get_index_server)
echo "##teamcity[progressMessage 'INDEX_URL: $INDEX_URL']"
echo "##teamcity[blockClosed name='get_index_server']"

echo "##teamcity[blockOpened name='gen_pipconf' description='generate pip configuration']"
gen_pipconf
echo "##teamcity[blockClosed name='gen_pipconf']"

echo "##teamcity[blockOpened name='virt_env' description='Activating virtual environment']"
virt_env
if [ "$(uname -o)" = "Cygwin" ] ; then
    . $VIRTDIR/Scripts/activate
else
    . $VIRTDIR/bin/activate
fi
echo "##teamcity[blockClosed name='virt_env']"

echo "##teamcity[blockOpened name='py_prep' description='Install prequisites']"
py_prep
echo "##teamcity[blockClosed name='py_prep']"

echo "##teamcity[blockOpened name='py_build' description='Building']"
py_build
echo "##teamcity[blockClosed name='py_build']"

echo "##teamcity[blockOpened name='py_test' description='Testing']"
py_test
echo "##teamcity[blockClosed name='py_test']"

echo "##teamcity[blockOpened name='py_dist' description='Generating binary installer']"
py_dist
echo "##teamcity[blockClosed name='py_dist']"

# Local Variables:
# mode: shell-script
# mode: flyspell
# ispell-local-dictionary: "english"
# coding: utf-8
# compile-command: "sh install_prerequisite.sh"
# End:

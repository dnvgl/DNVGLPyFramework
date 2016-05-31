#! /bin/bash

# Copyright © 2016 by DNV GL SE

# Task  : Testing DNVGLPyFramework

# Author: Berthold Höllmann <berthold.hoellmann@dnvgl.com>

# ID: $Id$
author="$Author$"
date="$Date$"
version="$Revision$"

set -e

if [ "$(uname -o)" = "Cygwin" ] ; then
    PIPCONFPATH="$(cygpath $APPDATA)/pip"
    PIPCONFEXT=pipini
    PIPARCH=dist_WIN_64
else
    PIPCONFPATH=$HOME/.pip
    PIPCONF=pip.conf
    PIPARCH=dist_UBUNTU_14_04
fi

if [ ! -d "$PIPCONFPATH" ] ; then
    mkdir -p "$PIPCONFPATH"
fi

if [ ! -e "$PIPCONFPATH/$PIPCONF" ] ; then
    echo "[global]" > "$PIPCONFPATH/$PIPCONF"
    echo "trusted_host = srverc.germanlloyd.org" >> "$PIPCONFPATH/$PIPCONF"
    echo "index_url = http://srverc.germanlloyd.org/devpi/dnvgl/$PIPARCH/+simple/" >> "$PIPCONFPATH/$PIPCONF"
fi

echo "##teamcity[blockOpened name='virtEnv' description='Activating virtual environment']"

pip$PYMAJOR install --index-url=$INDEX_URL --user --upgrade virtualenv

VIRTDIR=$(echo "/tmp/DNVGLPyFramework_${TEAMCITY_PROJECT_NAME}_${TEAMCITY_BUILDCONF_NAME}" | sed "s-[ ;:]-_-g")

if [ ! -e $VIRTDIR ] ; then
    if [ "$(uname -o)" = "Cygwin" ] ; then
        virtualenv $(cygpath --windows $VIRTDIR) --python=c:/python$PYVER/python.exe
    else
        virtualenv $VIRTDIR --python=python$PYMAJOR
    fi
fi

if [ "$(uname -o)" = "Cygwin" ] ; then
    . $VIRTDIR/Scripts/activate
else
    . $VIRTDIR/bin/activate
fi

echo "##teamcity[blockClosed name='virtEnv']"

echo "##teamcity[blockOpened name='prequisites' description='Install prequisites' timestamp='timestamp']"

pip$PYMAJOR install --index-url=$INDEX_URL --upgrade pytest pytest-pep8 pytest-cov wheel
pip$PYMAJOR install --index-url=$INDEX_URL --upgrade --requirement=requirements.txt

echo "##teamcity[blockClosed name='prequisites']"

echo "##teamcity[blockOpened name='building' description='Building' timestamp='timestamp']"

python$PYMAJOR setup.py build

echo "##teamcity[blockClosed name='building']"

echo "##teamcity[blockOpened name='testing' description='Testing']"

tox -e py$PYVER

echo "##teamcity[blockClosed name='testing']"

echo "##teamcity[blockOpened name='bdist' description='Generating binary installer']"

echo "##teamcity[blockOpened name='simple' description='Generating simple installer']"

python$PYMAJOR setup.py bdist

echo "##teamcity[blockClosed name='simple']"

echo "##teamcity[blockOpened name='egg' description='Generating egg installer']"

python$PYMAJOR setup.py bdist_egg

echo "##teamcity[blockClosed name='egg']"

echo "##teamcity[blockOpened name='wheel' description='Generating wheel installer']"

pip$PYMAJOR wheel .

echo "##teamcity[blockClosed name='wheel']"

echo "##teamcity[blockClosed name='bdist']"

# Local Variables:
# mode: shell-script
# mode: flyspell
# ispell-local-dictionary: "english"
# coding: utf-8
# compile-command: "sh install_prerequisite.sh"
# End:

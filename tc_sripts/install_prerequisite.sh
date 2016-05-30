#! /bin/bash

# Copyright © 2016 by DNV GL SE

# Task  : Install prerequisite for testing

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
    alias cygdrive=echo
fi

if [ ! -d "$PIPCONFPATH" ] ; then
    mkdir -p "$PIPCONFPATH"
fi

if [ ! -e "$PIPCONFPATH/$PIPCONF" ] ; then
    echo "[global]" > "$PIPCONFPATH/$PIPCONF"
    echo "trusted_host = srverc.germanlloyd.org" >> "$PIPCONFPATH/$PIPCONF"
    echo "index_url = http://srverc.germanlloyd.org/devpi/dnvgl/$PIPARCH/+simple/" >> "$PIPCONFPATH/$PIPCONF"
fi

pip$PYMAJOR install --index-url=$INDEX_URL --user --upgrade virtualenv

VIRTDIR=$(echo "/tmp/DNVGLPyFramework_${TEAMCITY_PROJECT_NAME}_${TEAMCITY_BUILDCONF_NAME}" | sed "s-[ ;:]-_-g")

if [ ! -e $VIRTDIR ] ; then
    if [ "$(uname -o)" = "Cygwin" ] ; then
        virtualenv $VIRTDIR --python=c:/python$PYVER/python.exe
    else
        virtualenv $VIRTDIR --python=python$PYMAJOR
    fi
fi

. $(cygdrive $VIRTDIR/bin/activate)

pip$PYMAJOR install --index-url=$INDEX_URL --upgrade pytest pytest-pep8 pytest-cov

pip$PYMAJOR install --index-url=$INDEX_URL --upgrade --requirement=requirements.txt

# Local Variables:
# mode: shell-script
# mode: flyspell
# ispell-local-dictionary: "english"
# coding: utf-8
# compile-command: "sh install_prerequisite.sh"
# End:

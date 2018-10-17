#! /bin/bash

# Copyright © 2018 by DNV GL SE

# Task  : Generate PNG logos from SVN logo.

# Author: Berthold Höllmann <berthold.hoellmann@dnvgl.com>

# ID: $Id$
author="$Author$"
date="$Date$"
version="$Revision$"

sizes="16 32 64 128 256 512 1024"

iname=DNVGLPyFramework-logo-inkscape.svg

for size in $sizes; do
    echo "size: $size"
    oname=DNVGLPyFramework-logo-$size.png
    inkscape --export-png $oname --export-area-drawing --export-width $size $iname
done

inkscape --export-plain-svg DNVGLPyFramework-logo.svg --export-area-drawing $iname


# Local Variables:
# mode: shell-script
# coding: utf-8
# compile-command: "sh gen-png-logos.sh"
# End:

#! /usr/bin/env python
# -*- coding: utf-8 -*-

u""" Wrapper for class `Plane` from `tbplanev1` module by Karsten
Stenzel (<karsten.stenzel@t-online.de>)

:author: `Berthold Hoellmann <hoel@GL-group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2010 by Germanischer Lloyd AG"""

from __future__ import absolute_import

#  ID: $Id$
__date__      = u"$Date$"[5:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import itertools

from ..stenzel.tbplanev1 import Plane as tbPlane

class _FakeKcsUtil(object):
    """Fake kcs_util for Plane implementation by Karsten Stenzel.
"""

    def __init__(self, frmtbl):
        self.frmtbl = []
        [ self.frmtbl.extend(zip(ft.unfold(),
                                 itertools.repeat(ft.spacing)))
          for ft in frmtbl.positions ]
        self.frmtbl = [ a + (b,) for a, b in self.frmtbl ]

    def coord_to_pos(self, dummy, coor):
        """Calculate frame position from coordinate.
"""
        if coor < self.frmtbl[0][1]:
            return (True, None, None)
        lstfrm, lstpos, lstspc = self.frmtbl[0]
        for frame, pos, spacing in self.frmtbl:
            if coor < pos:
                if coor < lstpos-lstspc/2.:
                    return (True, None, None)
                elif coor < pos-spacing/2.:
                    return (None, lstfrm, (coor-lstpos)*1000.)
                else:
                    return (None, frame, (coor-pos)*1000.)
            lstfrm, lstpos, lstspc = frame, pos, spacing
        if coor < lstpos+lstspc/2.:
            return (None, lstfrm, (coor-lstpos)*1000.)
        return (True, None, None)

def injectFrameTable(frmtbl):
    """inject frametable information into tbPlane
"""
    from ..stenzel import tbplanev1
    tbplanev1.hasTribon = True
    tbplanev1.kcs_util = _FakeKcsUtil(frmtbl)

class Plane(tbPlane):
    """
Thin wrapper for Karsten Stenzels Plane class to allow origin and
normal vector to be lists instead of collection of values.
"""
    def __init__(self, origin, normal):
        args = list(origin)+list(normal)
        super(Plane, self).__init__(*args)


# Local Variables:
# mode:python
# mode:flyspell
# pylint-options: "--output-format=parseable --import-graph=planecheck_import.png --init-hook=\"import sys;sys.path.append('..')\" "
# compile-command:"make -C ../../../ test"
# End:

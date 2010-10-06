#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

u"""
Tests for the plane identifier.

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2010 by Germanischer Lloyd AG
"""

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import doctest
import math
import os.path
import unittest

from tribon.util import planecheck
from tribon.xml.txhbd import frametable as frmt

SQRT2 = math.sqrt(2.)

def genFrmtbl():
    frmTab = frmt.FrameTable()
    #frmt.FrameDef(firstFrameNo, firstFramePos, endFrameNo, spacing)
    frmTab.addDefPositon(frmt.FrameDef(-10, -7.,  -1, .7))
    frmTab.addDefPositon(frmt.FrameDef(  0,  0.,  19,  1.))
    frmTab.addDefPositon(frmt.FrameDef( 20, 20., 100,  1.7))
    return frmTab

FRMTBL = genFrmtbl()

class PlanecheckTest(unittest.TestCase):

    def setUp(self):
        pass

    def testFirst(self):
        plane = planecheck.Plane((1, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=1")
        plane = planecheck.Plane((0, 1, 0), (0, 1, 0))
        self.assert_(plane.get_plane_string()=="Y=1")
        plane = planecheck.Plane((0, 0, 1), (0, 0, 1))
        self.assert_(plane.get_plane_string()=="Z=1")
        plane = planecheck.Plane((1, 0, 0), (SQRT2, SQRT2, 0))
        self.assert_(plane.get_plane_string()=="(Y)=0")
        plane = planecheck.Plane((1, 0, 0), (0, SQRT2, SQRT2))
        self.assert_(plane.get_plane_string()=="(Z)=0")
        plane = planecheck.Plane((1, 0, 0), (SQRT2, 0, SQRT2))
        self.assert_(plane.get_plane_string()=="(Z)=0")

    def testInject(self):
        planecheck.injectFrameTable(FRMTBL)
        plane = planecheck.Plane((-11, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=-11")
        plane = planecheck.Plane((1, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=FR1")
        plane = planecheck.Plane((1, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=FR1")
        plane = planecheck.Plane((1.2, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=FR1+199")
        plane = planecheck.Plane((1.7, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=FR2-300")
        plane = planecheck.Plane((156.8, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=FR100+800")
        plane = planecheck.Plane((158, 0, 0), (1, 0, 0))
        self.assert_(plane.get_plane_string()=="X=158")

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(planecheck))

    runner = unittest.TextTestRunner()
    runres = runner.run(suite)
    if runres.errors or runres.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# compile-command:"make tribon.util.planecheck_test"
# End:

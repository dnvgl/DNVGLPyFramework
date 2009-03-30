#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

u"""
Unit tests for tx2pegasus.circle

:author: `Berthold Höllmann <berthold.hoellmann@gl-group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2009 by Germanischer Lloyd AG"""

#  ID: $Id$
__date__      = u"$Date$"[5:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import doctest
import unittest

import numpy as np

from tribon.util.circle import Circle3n

class Circle3nTest(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle3n((-1, 0), (0, 1), (1, 0))
        self.c2 = Circle3n((0, 0), (1, 1), (2, 0))
        self.c3 = Circle3n((0, 1), (1, 2), (2, 1))
        self.c4 = Circle3n((-2, 4), (1, -3), (5, 7))
        self.c5 = Circle3n((-1, 0, 2), (0, 1, 2), (1, 0, 2))
        self.c6 = Circle3n((-1, -2, 0), (0, -2, 1), (1, -2, 0))
        self.c7 = Circle3n((-2, -1, 0), (-2, 0, 1), (-2, 1, 0))
        self.c8 = Circle3n((-2, -1, 0), (2, 0, 1), (0, 1, 0))

    def testRadius(self):
        self.failUnlessAlmostEqual(self.c1.radius, 1.)
        self.failUnlessAlmostEqual(self.c2.radius, 1.)
        self.failUnlessAlmostEqual(self.c3.radius, 1.)
        self.failUnlessAlmostEqual(self.c4.radius, np.sqrt(29.))
        self.failUnlessAlmostEqual(self.c5.radius, 1.)
        self.failUnlessAlmostEqual(self.c6.radius, 1.)
        self.failUnlessAlmostEqual(self.c7.radius, 1.)

    def testCentre(self):
        self.failUnless(np.allclose(self.c1.centre, [0., 0.]))
        self.failUnless(np.allclose(self.c2.centre, [1., 0.]))
        self.failUnless(np.allclose(self.c3.centre, [1., 1.]))
        self.failUnless(np.allclose(self.c4.centre, [3., 2.]))
        self.failUnless(np.allclose(self.c5.centre, [0., 0., 2.]))
        self.failUnless(np.allclose(self.c6.centre, [0., -2., 0.]))
        self.failUnless(np.allclose(self.c7.centre, [-2., 0., 0.]))

    def testPoint(self):
        for c in (self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8):
            num = 10
            self.failUnless(
                np.allclose(
                    [((c.point(u)-c.centre)**2).sum()
                     for u in np.arange(float(num))/float(num) ], c.radius**2))
            num = 100
            self.failUnless(
                np.allclose(
                    [((c.point(u)-c.centre)**2).sum()
                     for u in np.arange(float(num))/53.], c.radius**2) )

    def testPhi(self):
        num = 1000.
        phis = (np.arange(num)/num)*2.*np.pi
        for c in (self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8):
            for point in c.pnt1, c.pnt2, c.pnt3:
                self.failUnless(np.allclose(point, c.point(c.phi(point))))
                self.failUnless(np.allclose([ c.phi(c.point(phi)) for phi in phis ], phis, atol=2e-8),
                                max(phis-[ c.phi(c.point(phi)) for phi in phis ]))

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    suite = unittest.TestSuite()
    from tribon.util import circle
    suite.addTest(doctest.DocTestSuite(circle))

    runner = unittest.TextTestRunner()
    runres = runner.run(suite)
    if runres.errors or runres.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"make test"
# End:

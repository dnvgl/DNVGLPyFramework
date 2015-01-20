#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Unit tests for tx2pegasus.idgen

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG
"""

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import doctest
import unittest

from glframework import idgen

class _Base(object):
    """Base class needed for testing correct bahaviour in derived classes.
"""
    _ID = idgen.IDGen()
    def __call__(self):
        return self._ID()

class DerivA(_Base):
    "First derived class"

class DerivB(_Base):
    "second derived class"

class Test(unittest.TestCase):
    """
Testing the glframework.idgen module,
"""
    def setUp(self):
        self.a_1 = DerivA()
        self.a_2 = DerivA()
        self.b_1 = DerivB()
        self.b_2 = DerivB()

    def testRun(self):
        """Testing correct behavour in derived classes.
"""
        self.assert_(self.a_1() == 0)
        self.assert_(self.b_1() == 1)
        self.assert_(self.a_2() == 2)
        self.assert_(self.b_2() == 3)
        self.assert_(self.a_1() == 4)
        self.assert_(self.b_1() == 5)

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(idgen))

    RUNNER = unittest.TextTestRunner()
    RUNRES = RUNNER.run(SUITE)
    if RUNRES.errors or RUNRES.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# mode:flyspell
# ispell-local-dictionary:"en"
# compile-command:"make test"
# End:

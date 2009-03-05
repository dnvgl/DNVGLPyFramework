#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Unit tests for tx2pegasus.idgen

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:author: `last modified by <%s@GL-Group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG
"""
__doc__ = __doc__ % ("$Author$"[9:-1].strip())

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import doctest
import unittest

from tribon.util.idgen import IDGen

class _Base(object):
    _ID = IDGen()
    def __call__(self):
        return self._ID()

class DerivA(_Base):
    pass

class DerivB(_Base):
    pass

class Test(unittest.TestCase):

    def setUp(self):
        self.A1 = DerivA()
        self.A2 = DerivA()
        self.B1 = DerivB()
        self.B2 = DerivB()

    def testRun(self):
        self.assert_(self.A1() == 0)
        self.assert_(self.B1() == 1)
        self.assert_(self.A2() == 2)
        self.assert_(self.B2() == 3)
        self.assert_(self.A1() == 4)
        self.assert_(self.B1() == 5)

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    suite = unittest.TestSuite()
    from tribon.util import idgen
    suite.addTest(doctest.DocTestSuite(idgen))

    runner = unittest.TextTestRunner()
    runres = runner.run(suite)
    if runres.errors or runres.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

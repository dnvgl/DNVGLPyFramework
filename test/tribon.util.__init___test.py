#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
tests for tribon.util module

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:author: `last modified by <%s@GL-Group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG"""
__doc__ = __doc__ % ("$Author$"[9:-1].strip())

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import doctest
import unittest

from tribon import util

class Test(unittest.TestCase):

    def setUp(self):
        pass

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(util))

    runner = unittest.TextTestRunner()
    runres = runner.run(suite)
    if runres.errors or runres.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

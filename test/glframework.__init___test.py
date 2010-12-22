#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
tests for tribon.util module

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG"""

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import doctest
import unittest

import glframework

class Test(unittest.TestCase):
    """
Testing the glframework module.
"""

    def setUp(self):
        pass

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(glframework))

    RUNNER = unittest.TextTestRunner()
    RUNRES = RUNNER.run(SUITE)
    if RUNRES.errors or RUNRES.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

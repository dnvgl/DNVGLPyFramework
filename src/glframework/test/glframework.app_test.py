#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Unit tests for tx2pegasus.util.app

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

from glframework import app

class Test(unittest.TestCase):
    """
Testing the glframework.app module.
"""

    def setUp(self):
        pass

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(app))

    RUNNER = unittest.TextTestRunner()
    RUNRES = RUNNER.run(SUITE)
    if RUNRES.errors or RUNRES.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"make test"
# End:

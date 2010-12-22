#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
tests for tribon.xml.ship.material.__init__

:author: `Berthold Hoellmann <hoel@GL-group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2010 by Germanischer Lloyd AG"""

from __future__ import absolute_import

#  ID: $Id$
__date__      = u"$Date$"[5:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"


import unittest
import doctest
import sys

MODNAME = sys.argv[0][:-8]
if MODNAME.endswith('.__init__'):
    MODNAME = MODNAME[:-9]

__import__(MODNAME)
MODULE = sys.modules[MODNAME]

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    SUITE = unittest.TestSuite()
    SUITE.addTest(doctest.DocTestSuite(MODULE))

    RUNNER = unittest.TextTestRunner()
    RUNRES = RUNNER.run(SUITE)
    if RUNRES.errors or RUNRES.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

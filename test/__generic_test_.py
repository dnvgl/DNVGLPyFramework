#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

u"""
tests for tribon.xml.ship.material.__init__

:author: `Berthold Hoellmann <hoel@GL-group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2010 by Germanischer Lloyd AG"""

#  ID: $Id$
__date__      = u"$Date$"[5:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"


import unittest
import doctest
import sys

modname = sys.argv[0][:-8]
if modname.endswith('.__init__'):
    modname = modname[:-9]

module = __import__(modname)

if __name__ == '__main__':

    doctest.set_unittest_reportflags(doctest.REPORT_CDIFF)

    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(module))

    runner = unittest.TextTestRunner()
    runres = runner.run(suite)
    if runres.errors or runres.failures:
        raise Exception("failed test occured")

    unittest.main()

# Local Variables:
# mode:python
# compile-command:"make test"
# End:


# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"python setup.py build"
# End:


# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"python setup.py build"
# End:

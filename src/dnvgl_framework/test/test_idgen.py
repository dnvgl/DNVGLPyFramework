#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for `dnvgl_framework.idgen` module.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Third party libraries.
import pytest

from .. import idgen

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2007 by DNV GL SE"


class _Base(object):
    """Base class needed for testing correct bahaviour in derived classes.
"""
    _ID = idgen.IDGen()

    def __call__(self):
        return self._ID()


class DerivA(_Base):
    "First derived class."


class DerivB(_Base):
    "Second derived class."


class TestIDGen(object):
    """
Testing the `dnvgl_framework.idgen` module.
"""

    @pytest.fixture
    def a_1(self):
        return DerivA()

    @pytest.fixture
    def a_2(self):
        return DerivA()

    @pytest.fixture
    def b_1(self):
        return DerivB()

    @pytest.fixture
    def b_2(self):
        return DerivB()

    def testRun(self, a_1, a_2, b_1, b_2):
        """Testing correct behavour in derived classes.
"""
        assert a_1() == 0
        assert b_1() == 1
        assert a_2() == 2
        assert b_2() == 3
        assert a_1() == 4
        assert b_1() == 5

# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "make -C ../../../test test"
# End:

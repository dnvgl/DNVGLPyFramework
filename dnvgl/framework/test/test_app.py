#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for `dnvgl_framwork.app` module.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Third party libraries.
import pytest

# DNV GL libraries.
from dnvgl.framework import app

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2009 by DNV GL SE"


class TestApp(object):

    @pytest.fixture()
    def app_1(self):
        class this_app(app.Application):
            _optionList = []
        return this_app([])

    @pytest.fixture()
    def app_2(self):
        class this_app(app.Application):
            _optionList = []
        return this_app(["--factor", "1"])

    def test_factor_1(self, app_1):

        assert app.Application.args.factor == .001

    def test_factor_2(self, app_2):

        assert app.Application.args.factor == 1.


# Local Variables:
# mode: python
# compile-command: "cd ../../..;python setup.py test"
# End:

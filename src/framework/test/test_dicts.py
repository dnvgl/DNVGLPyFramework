#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing the different dict implementations in `gl.utils.dicts`.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Third party libraries.
import pytest

from ..dict import SortedDict, CaseInsensitiveDict

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2015 by DNV GL SE"


class TestSortedDict(object):

    def test_outp(self):
        probe = SortedDict(c=3)
        probe['b'] = 2
        probe['a'] = 1
        assert probe.items() == [('a', 1), ('b', 2), ('c', 3)]


class TestCaseInsensitiveDict(object):

    def test_init_1(self):
        assert CaseInsensitiveDict(A=1, B=2) == {'a': 1, 'b': 2}

    @pytest.fixture
    def dict_data(self):
        return CaseInsensitiveDict({'a': 1, 'B': 2}, d=3, E=4, A=5)

    def test_init_2(self, dict_data):
        assert dict_data == {'a': 5, 'b': 2, 'd': 3, 'e': 4}

    def test_init_3(self):
        probe = CaseInsensitiveDict((('A', 5), ('b', 2), ('D', 3), ('e', 4)))
        assert probe == {'a': 5, 'b': 2, 'd': 3, 'e': 4}

    def test_getitem_1(self, dict_data):
        assert dict_data['A'] == 5

    def test_getitem_2(self, dict_data):
        assert dict_data['e'] == 4

    def test_getitem_3(self, dict_data):
        assert dict_data['d'] == 3

    def test_update_1(self, dict_data):
        dict_data.update({'A': 1, 'B': 22})
        assert dict_data == {'a': 1, 'b': 22, 'd': 3, 'e': 4}

    def test_update_2(self, dict_data):
        dict_data.update((('A', 1), ('B', 22)))
        assert dict_data == {'a': 1, 'b': 22, 'd': 3, 'e': 4}


# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "python setup.py build"
# End:

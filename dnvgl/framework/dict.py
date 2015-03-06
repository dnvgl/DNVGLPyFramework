#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Various specialized dict implementations for `gl`.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import collections

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2015 by DNV GL SE"


class SortedDict(dict):

    def items(self):
        keys = list(self.keys())
        keys.sort()
        return zip(keys, [self.get(x) for x in keys])


class CaseInsensitiveDict(dict):

    def __init__(self, inp=None, **kw):
        # test inp for mapping
        if isinstance(inp, (collections.Mapping)):
            for k, v in inp.items():
                self[k] = v
        # test inp for iteratable
        elif inp is not None:
            for k, v in inp:
                self[k] = v
        # add kw content
        for k, v in kw.items():
            self[k] = v

    def update(self, inp):
        # test inp for mapping
        if isinstance(inp, (collections.Mapping)):
            for k, v in inp.items():
                self[k] = v
        # test inp for iteratable
        else:
            for k, v in inp:
                self[k] = v

    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())


# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "python setup.py build"
# End:

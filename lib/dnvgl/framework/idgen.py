#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate unique ids. Allow for registering additional ids that are
exclude from furter usage.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import collections

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010 by DNV GL SE"


class IDGen(object):
    """
>>> id = IDGen()
>>> assert id() == 0
>>> assert id() == 1
>>> assert id() == 2
>>> id.exclude(3)
>>> assert id() == 4
>>> id = IDGen(10)
>>> assert id() == 10
>>> id.set(2)
>>> assert id() == 2
>>> assert id() == 3
>>> id.set(3)
Traceback (most recent call last):
  ...
ValueError: Value 3 already used or in exclude list.
>>> id.exclude(range(10))
>>> assert id() == 11
"""

    def __init__(self, start=None):
        self._excludes = set()
        self._ID = start or 0
        self._counter = self.__counter()
        self.__set = False

    def __call__(self):
        return next(self._counter)

    def __retval(self):
        """
Search for next value to return by `__counter`.
"""
        while self._ID in self._excludes:
            self._ID += 1
        self.exclude(self._ID)
        return self._ID

    def __counter(self):
        """
Generator function to return the next usable ID value.
"""
        while 1:
            yield self.__retval()
            if not self.__set:
                self._ID += 1
            else:
                self.__set = False

    def set(self, val):
        """
Set the next value to be returned.
"""
        if val in self._excludes:
            raise ValueError(
                "Value {} already used or in exclude list.".format(val))
        self._ID = val
        self.__set = True

    def exclude(self, val):
        """
Add a list of values `val` to be excluded from this generator.

:Parameters:
  val
    List of values to be excluded from returning.
"""
        if isinstance(val, collections.Sequence):
            self._excludes.update(val)
        else:
            self._excludes.add(val)

# Local Variables:
# mode: python
# compile-command: "cd ../../..;python setup.py test"
# End:

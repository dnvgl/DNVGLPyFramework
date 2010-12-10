#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Generate unique ids. Allow for registering additional ids that are
exclude from furter usage.

:author: `Berthold Höllmann <berthold.hoellmann@GL-Group.com>`__
:newfield project: Project
:project: tx2pegasus
:copyright: Copyright © 2007 by Germanischer Lloyd
"""

from __future__ import absolute_import

#  CVSID: $Id$
__date__         = u"$Date$"
__version__      = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import operator

class IDGen(object):
    """
>>> id = IDGen()
>>> id()
0
>>> id()
1
>>> id()
2
>>> id.exclude(3)
>>> id()
4
>>> id = IDGen(10)
>>> id()
10
>>> id.set(2)
>>> id()
2
>>> id.exclude(range(10))
>>> id()
10
"""
    def __init__(self, start=None):
        self._excludes = []
        self._ID = start or 0
        self._counter = self.__counter()
        self.__set = False

    def __call__(self):
        return self._counter.next()

    def __retval(self):
        """
Search for next value to return by `__counter`.
"""
        while self._ID in self._excludes:
            self._ID += 1
        return self._ID

    def __counter(self):
        """
Generator function to return the next usable ID value.
"""
        while 1:
            yield self.__retval()
            if not self.__set:
                self._ID += 1

    def set(self, val):
        """
Set the next value to be returned.
"""
        self._ID = val
        self.__set = True

    def exclude(self, val):
        """
Add a list of values `val` to be excluded from this generator.

:Parameters:
  val
    List of values to be excluded from returning.
"""
        if operator.isSequenceType(val):
            self._excludes.extend(val)
        else:
            self._excludes.append(val)

# Local Variables:
# mode:python
# compile-command:"make -C ../../../ test"
# End:

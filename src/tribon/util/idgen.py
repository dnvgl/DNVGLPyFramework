#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
generate unique ids. Allow for registering additional ids that are
exclude from furter usage.

:author: `Berthold Höllmann <berthold.hoellmann@GL-Group.com>`__
:author: `last modified by <%s@GL-Group.com>`__
:newfield project: Project
:project: tx2pegasus
:copyright: Copyright © 2007 by Germanischer Lloyd
"""
__doc__ = __doc__ % ("$Author$"[9:-1].strip())

#  CVSID: $Id$
__date__         = u"$Date$"
__version__      = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

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
    """
    def __init__(self, start=None):
        self._excludes = []
        self._ID = start or 0
        self._counter = self.__counter()

    def __call__(self):
        return self._counter.next()

    def __counter(self):
        while 1:
            while self._ID in self._excludes:
                self._ID += 1
            yield self._ID
            self._ID += 1

    def exclude(self, val):
        self._excludes.append(val)

# Local Variables:
# mode:python
# compile-command:"make -C ../../../text test"
# End:

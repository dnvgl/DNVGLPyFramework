#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
A lightweight Application framwork

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: GLPyFramwork
:copyright: Copyright (C) 2010 by Germanischer Lloyd SE
"""

from __future__ import absolute_import

#  CVSID: $Id$
__date__      = u"$Date$"[6:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

from .idgen import IDGen

__all__ = locals().keys()

# Local Variables:
# mode:python
# mode:flyspell
# ispell-local-dictionary:"en"
# compile-command:"make -C ../../ test"
# End:

#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""A lightweight Application framwork.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

from .idgen import IDGen  # noqa

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010 by DNV GL SE"


__all__ = locals().keys()

# Local Variables:
# mode: python
# compile-command: "cd ../../;python setup.py test"
# End:

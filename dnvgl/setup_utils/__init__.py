#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Processing version numbers.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# ID$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2015 by DNV GL SE"

__all__ = locals().keys()

# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "make -C ../../ test"
# End:

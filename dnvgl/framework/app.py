#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""A lightweight Application framwork.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import argparse

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010 by DNV GL SE"


class Application(object):
    """
Base Class for Applications.

This class is a base class applications. It allows access to the
program options from all parts of the program.

:CVariables:
  args
    parsed options as from `argparse.ArgumentParser.parse_args`
  _optionList
    option list for creating `ArgumentParser` instance
  _usage
    usage information
  _version
    version information for actual application
  _description
    description for actual application
  _minArgs
    required minimum length of args
  _maxArgs
    allowed maximum length of args
"""
    args = None
    _optionList = None
    _usage = None
    _version = None
    _description = None

    def __init__(self, args=None):
        parser = argparse.ArgumentParser(
            usage=self._usage, description=self._description)
        parser.add_argument('--version', action='version',
                            version='%(prog)s {}'.format(self._version))
        for (name, options) in self._optionList:
            parser.add_argument(*name, **options)
        parser.add_argument('--factor', action='store', default=1. / 1000.,
                            metavar="FACTOR", type=float,
                            help="""Factor for length units.
        DEFAULT: %(default)s""")
        Application.args = parser.parse_args(args)

    def __call__(self):
        return self.main()

# Local Variables:
# mode: python
# compile-command: "cd ../../;python setup.py test"
# End:

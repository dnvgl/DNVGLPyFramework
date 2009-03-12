#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

u"""
Application framework for Tribon converters

:author: `Berthold Höllmann <berthold.hoellmann@gl-group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2009 by Germanischer Lloyd AG"""

#  ID: $Id$
__date__      = u"$Date$"[5:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import optparse

class Application(object):
    """
Base Class for Applications.

This class is the base class for all applications from the GL
TribonXML converter suite. It allows access to the program options
from all parts of the program.

:CVariables:
  options
    parsed options as from `optparse.OptionParser.parse_args`
  args
    args part from `optparse.OptionParser.parse_args`
  _optionList
    option list for creating `OptionParser' instance
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
    options = None
    args = None
    _optionList = None
    _usage = None
    _version = None
    _description = None
    _minArgs = 1
    _maxArgs = None

    def __init__(self):
        parser = optparse.OptionParser(option_list=self._optionList,
                                       usage=self._usage,
                                       version=self._version,
                                       description = self._description)
        Application.options, Application.args = parser.parse_args()

        if (len(self.args) != 1 or
            (self._maxArgs and len(self.args) > self._maxArgs)):
            parser.error("incorrect number of arguments")

    def __call__(self):
        return self.main()

# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"make -C ../../../ test"
# End:

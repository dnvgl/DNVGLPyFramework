#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
A lightweight Application framwork

:author: `Berthold Höllmann <berthold.hoellmann@gl-group.com>`__
:newfield project: Project
:project: GLPyFramwork
:copyright: Copyright (C) 2010 by Germanischer Lloyd SE
"""

from __future__ import absolute_import

#  ID: $Id$
__date__ = u"$Date$"[5:-1]
__version__ = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import argparse


class Application(object):
    """
Base Class for Applications.

This class is a base class applications. It allows access to the
program options from all parts of the program.

:CVariables:
  options
    parsed options as from `argparse.ArgumentParser.parse_args`
  args
    args part from `argparse.ArgumentParser.parse_args`
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
    options = None
    args = None
    _optionList = None
    _usage = None
    _version = None
    _description = None
    _minArgs = 1
    _maxArgs = None
    _numargs = 1

    def __init__(self, args=None):
        optionList = (self._optionList or []) + (
            (('', '--factor'),
             {"action": 'store', "default": 1. / 1000.,
              "metavar": "FACTOR", "type": "float",
              "help": "Factor for length units. DEFAULT: [%default]"}))
        parser = argparse.ArgumentParser(usage=self._usage,
                                         description=self._description)
        parser.add_argument('--version', action='version',
                            version='%(prog)s {}'.format(self._version))
        for (name, args) in optionList:
            parser.add_argument(*name, **args)
        Application.options, Application.args = parser.parse_args(args)

        if  (len(self.args) < self._numargs or
             (self._maxArgs and len(self.args) > self._maxArgs)):
            print "self.args: ", self.args
            parser.error("incorrect number of arguments")

    def __call__(self):
        return self.main()

# Local Variables:
# mode:python
# mode:flyspell
# ispell-local-dictionary:"en"
# compile-command:"make -C ../../ test"
# End:

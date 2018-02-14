#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Logging formatter for tribonXML_convert.

Taken from "The Python: Rag", August  2009.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import logging
import logging.handlers
from functools import wraps

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2011 by DNV GL SE"


# Create a global logger
_DNVGL_LOGGER = None

# Set default DEBUG_ON True - in which case debug messages
# are saved to the log file. Or set it to False - in which
# case only INFO and ERROR messages are saved to the log file
_DEBUG_ON = True


def set_logger(options, debug_on=_DEBUG_ON):
    "Set up the logger"

    global _DNVGL_LOGGER

    _DNVGL_LOGGER = logging.getLogger("tx_logger")

    if options.logfile is None:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s *** %(levelname)s ***: %(message)s',
            filename='tx2pegasus.log',
            filemode='w')
    else:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s *** %(levelname)s ***: %(message)s',
            filename=options.logfile,
            filemode='w')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('* %(levelname)s *: %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    # Set the logger level
    if debug_on:
        _DNVGL_LOGGER.setLevel(logging.DEBUG)
    else:
        _DNVGL_LOGGER.setLevel(logging.INFO)

    # Set the format
    form = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Add the log message handler to the logger
    # The location of the logfile is given here as 'logfile.txt'
    # in an actual application I would take a bit of care
    # where this is located
    handler = logging.handlers.RotatingFileHandler("logfile.txt",
                                                   maxBytes=20000,
                                                   backupCount=5)
    handler.setFormatter(form)
    _DNVGL_LOGGER.addHandler(handler)


def info_log(message):
    "Log message with level info"
    if _DNVGL_LOGGER:
        _DNVGL_LOGGER.info(str(message))


def warn_log(message):
    "Log message with level warning"
    if _DNVGL_LOGGER:
        _DNVGL_LOGGER.warning(str(message))


def debug_log(message):
    "Log message with level debug"
    if _DNVGL_LOGGER:
        _DNVGL_LOGGER.debug(str(message))


def error_log(message):
    "Log message with level error"
    if _DNVGL_LOGGER:
        _DNVGL_LOGGER.error(str(message))


def logmethod(func):
    "Creates a decorator to log a method"
    @wraps(func)
    def wrapper(self, *args, **kwds):
        debug_log("%s in %s called" % (func.__name__, self.__class__.__name__))
        return func(self, *args, **kwds)
    return wrapper


def exception_log(message):
    "Log message with level error plus exception traceback"
    if _DNVGL_LOGGER:
        _DNVGL_LOGGER.exception(str(message))

# Local Variables:
# mode: python
# compile-command: "cd ../../;python setup.py test"
# End:

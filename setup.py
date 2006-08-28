#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2006 by Germanischer Lloyd AG

"""
======================================================================
Module    setup
Task      setup for tx2glshipmodel
----------------------------------------------------------------------
Author    Berthold Höllmann <hoel@GL-Group.com>
Project   TX2GlShipModel
----------------------------------------------------------------------
Status    $State$
Date      $Date$
======================================================================
"""

#  CVSID: $Id$
__author__       = ("2006 Germanischer Lloyd (author: $Author$) " +
                    "hoel@GL-Group.com")
__date__         = "$Date$"
__version__      = "$Revision$"[10:-1]
__package_info__ = """ """

from distutils.core import setup, Extension

setup(name='AIS',
      version='0.4',
      description='Processing AIS data streams',
      author='Berthold Höllmann, Germanischer Lloyd AG',
      author_email='berthold.hoellmann@gl-group.com',
      url='http://www.gl-group.com',
      packages=['tx2glshipmodel'],
      package_dir = {'': 'src'},

     )

# Local Variables: ***
# mode:python ***
# compile-command:"make test" ***
# End: ***

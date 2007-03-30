#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup and install for TX2GlShipModel,

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:author: `last modified by <%s@GL-Group.com>`__
:newfield project: Project
:project: TX2GlShipModel
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG
"""
__doc__ = __doc__ % ("$Author$"[9:-1].strip())

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

from distutils.core import setup

setup(name='TX2GlShipModel',
      version='0.1',
      description='convert Tribon XML export files to GLShipmodel import files',
      author='Berthold Höllmann, Germanischer Lloyd AG',
      author_email='berthold.hoellmann@gl-group.com',
      url='http://www.gl-group.com',
      packages=['tx2glshipmodel'],
      package_dir = {'': 'src'},
      )

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

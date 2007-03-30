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
import distutils.sysconfig
import glob
import os.path
import sys

tribonXSD = glob.glob(os.path.join("src", "tribon", "xsd", "*.xsd"))
pegasusXSD = glob.glob(os.path.join("src", "tribon", "pegasus", "xsd", "*.xsd"))
if sys.platform[:6]=='win32':
    data_files = [(os.path.join("tribon", "xsd"), tribonXSD),
                  (os.path.join("tribon", "pegasus", "xsd"), pegasusXSD)]
else:
    data_files = [(os.path.join(distutils.sysconfig.get_python_lib(),
                                "tribon", "xsd"), tribonXSD),
                  (os.path.join(distutils.sysconfig.get_python_lib(),
                                "tribon", "pegasus", "xsd"), pegasusXSD)]

setup(name='TX2GlShipModel',
      version='0.1',
      description='convert Tribon XML export files to GLShipmodel import files',
      author='Berthold Höllmann, Germanischer Lloyd AG',
      author_email='berthold.hoellmann@gl-group.com',
      url='http://www.gl-group.com',
      packages=['tribon',
                'tribon.glshipmodel',
                'tribon.pegasus',
                'tribon.poseidon',
                'tribon.xml'],
      package_dir={'': 'src'},
      data_files=data_files,
      )

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup and install for TX2GlShipModel,

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: TX2GlShipModel
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG
"""

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
if sys.platform[:6] == 'win32':
    data_files = [(os.path.join("tribon", "xsd"), tribonXSD),
                  (os.path.join("tribon", "pegasus", "xsd"), pegasusXSD)]
else:
    data_files = [(os.path.join(distutils.sysconfig.get_python_lib(),
                                "tribon", "xsd"), tribonXSD),
                  (os.path.join(distutils.sysconfig.get_python_lib(),
                                "tribon", "pegasus", "xsd"), pegasusXSD)]

setup(name='TX2GlShipModel',
      version='0.2',
      description='convert Tribon XML export files to GLShipmodel import files',
      author='Berthold Höllmann, Germanischer Lloyd AG',
      author_email='berthold.hoellmann@gl-group.com',
      url='http://www.gl-group.com',
      # (cd src/;find . -type d|grep -v .svn |grep -v xsd|sed "s#^\./##g"|sed "s#^\.##g"|sed "s#/#.#g")
      packages=[
          'tribon',
          'tribon.ansys',
          'tribon.glshipmodel',
          'tribon.pegasus',
          'tribon.pegasus.hullcondition',
          'tribon.pegasus.hullcondition.shipdata',
          'tribon.pegasus.hullcondition.hullstructure',
          'tribon.poseidon',
          'tribon.stenzel',
          'tribon.util',
          'tribon.xml',
          'tribon.xml.txhbd',
          'tribon.xml.ship',
          'tribon.xml.ship.block',
          'tribon.xml.ship.block.planepanel',
          'tribon.xml.ship.block.planepanel.plategroup',
          'tribon.xml.ship.block.planepanel.stiffenergroup',
          'tribon.xml.ship.material',
          'tribon.xml.ship.barsection',
          ],
      package_dir={'': 'src'},
      data_files=data_files,
      )

# Local Variables:
# mode:python
# compile-command:"make test"
# End:

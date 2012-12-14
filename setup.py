#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup and install for GLPyFramework,

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: GLPyFramework
:copyright: Copyright (C) 2010 by Germanischer Lloyd SE
"""

#  CVSID: $Id$
__date__ = "$Date$"
__version__ = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

from setuptools import setup

setup(name='GLPyFramework',
      version='0.2',
      description='Lightwight framwork for GL Python applications.',
      author='Berthold Höllmann, Germanischer Lloyd AG',
      author_email='berthold.hoellmann@gl-group.com',
      url='http://www.gl-group.com',
      # (cd src/;find . -type d|grep -v .svn |grep -v xsd|sed "s#^\./##g"|
      #  sed "s#^\.##g"|sed "s#/#.#g")
      packages=['glframework', ],
      package_dir={'': 'src'},
      )



# Local Variables:
# mode:python
# mode:flyspell
# ispell-local-dictionary:"en"
# compile-command:"make test"
# End:

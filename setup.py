#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup and install for DNVGLPyFramework.
"""

from __future__ import division, print_function, absolute_import

# Standard libraries.
import os.path
from setuptools import setup, find_packages

# Third party libraries.
import py

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010, 2015 by DNV GL SE"

VERSION = py.path.local('version.txt').read().strip

for TARGET in [py.path.local('dnvgl').join(i).join('__version__.py') for i in
               ("framework", "setup_utils")]:
    TARGET.write(
        """# Automatically generated version file.

__version__ = \"{}\"\n""".format(VERSION))


if __name__ == '__main__':
    setup(
        name='DNVGLPyFramework',
        version=VERSION(),
        setup_requires=['pytest', 'pytest-cov', 'pytest-pep8', 'packaging'],
        install_requires=['py', 'packaging'],
        description='Lightweight framwork for DNV GL Python applications.',
        author='Berthold Höllmann, DNV GL SE',
        author_email='berthold.hoellmann@dnvgl.com',
        url='http://www.dnvgl.com',
        namespace_packages=['dnvgl'],
        packages=find_packages('.', exclude=[
            "*.__pycache__", "*.__pycache__.*", "__pycache__.*",
            "__pycache__"]),
        classifiers=['Development Status :: 6 - Mature',
                     'Intended Audience :: Developers',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: Utilities',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3'])

# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "make test"
# End:

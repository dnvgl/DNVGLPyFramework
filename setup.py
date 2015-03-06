#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup and install for DNVGLPyFramework.
"""

from __future__ import division, print_function, absolute_import

# Standard libraries.
import os.path
from setuptools import setup, find_packages

# DNV GL libraries.
from dnvgl.setup_utils.version import Version

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010, 2015 by DNV GL SE"

VERSION = Version('version.txt')

VERSION.write([os.path.join('dnvgl', i, '__version__.py') for i in
               ("framework", "setup_utils")])

if __name__ == '__main__':
    setup(
        name='DNVGLPyFramework',
        version=VERSION(),
        setup_requires=['pytest', 'pytest-cov', 'pytest-pep8'],
        install_requires=['py'],
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
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: Utilities',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3'])

# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "make test"
# End:

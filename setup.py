#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup and install for DNVGLPyFramework.
"""

from __future__ import division, print_function, absolute_import

# Standard libraries.
import os
from setuptools import setup, find_packages

# Third party libraries.
import py

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010, 2015 by DNV GL SE"

VERSION = py.path.local('version.txt').read().strip

for TARGET in [py.path.local('lib/dnvgl').join(i) for i in
               ("framework", "platform_utils", "setup_utils")]:
    TARGET.join('__version__.py').write(
        """# Automatically generated version file.

__version__ = \"{}\"\n""".format(VERSION()))

TESTS_REQUIRE = ['pytest', 'pytest-cov', 'pytest-pep8', 'packaging'],
PACKAGES = find_packages('lib', exclude=(
    "*.__pycache__", "*.__pycache__.*", "__pycache__.*",
    "__pycache__/", "flycheck*.py[cd]?"))
PACKAGE_DATA = {
    'dnvgl.framework': [os.path.join("test", "*.py")],
    'dnvgl.platform_utils': [os.path.join("test", "*.py")],
    'dnvgl.setup_utils': [os.path.join("test", "*.py")]}

if __name__ == '__main__':
    setup(
        name='DNVGLPyFramework',
        version=VERSION(),
        setup_requires=['tox', 'pytest-runner'],
        install_requires=['py', 'packaging', 'PyInstaller', 'jinja2'],
        tests_require=TESTS_REQUIRE,
        extras_require={'test': TESTS_REQUIRE},
        namespace_packages=['dnvgl'],
        package_dir={'': 'lib'},
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        entry_points={
            'console_scripts': [
                'dnvgl_pyplat = dnvgl.platform_utils:pyplat_cmd',
                'dnvgl_pyver = dnvgl.platform_utils:pyver_cmd']})

# Local Variables:
# mode: python
# compile-command: "python3 setup.py test"
# End:

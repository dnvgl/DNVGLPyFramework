#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup and install for DNVGLPyFramework.
"""

from __future__ import division, print_function, absolute_import

# Standard libraries.
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


if __name__ == '__main__':
    setup(
        name='DNVGLPyFramework',
        version=VERSION(),
        license='Other/Proprietary License',
        keywords='DNVGL AML FMI FMU',
        setup_requires=['tox', 'pytest-runner'],
        install_requires=['py', 'packaging', 'PyInstaller', 'jinja2'],
        tests_require=TESTS_REQUIRE,
        extras_require={'test': TESTS_REQUIRE},
        description='Lightweight framwork for DNV GL Python applications.',
        author='Berthold Höllmann, DNV GL SE',
        author_email='berthold.hoellmann@dnvgl.com',
        url='http://www.dnvgl.com',
        namespace_packages=['dnvgl'],
        package_dir={'': 'lib'},
        packages=find_packages('lib', exclude=(
            "*.__pycache__", "*.__pycache__.*", "__pycache__.*",
            "__pycache__/", "flycheck*.py[cd]?")),
        entry_points={
            'console_scripts': [
                'dnvgl_pyplat = dnvgl.platform_utils:pyplat_cmd',
                'dnvgl_pyver = dnvgl.platform_utils:pyver_cmd']},
        classifiers=[
            'Development Status :: 6 - Mature',
            'Intended Audience :: Developers',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Topic :: Software Development :: Libraries',
            'Topic :: Utilities',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3'])

# Local Variables:
# mode: python
# compile-command: "python3 setup.py test"
# End:

#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Handle module version number.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import sys
import subprocess

# Third party libraries.
import py
from packaging.version import Version as pVersion

# DNV GL libraries.
from dnvgl.framework.cached_property import cached_property

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2015 by DNV GL SE"


class VersionError(Exception):
    pass


class Version(object):

    """Handle Project version numbers for setup and others."""

    postfile = ".postcnt"

    def __init__(self, vers_file=None):
        """
:param str `vers_file`: Name of file to read version number from.
"""
        base = py.path.local(sys.argv[0]).dirpath()
        if vers_file is None:
            self.base_dir = base if base.isdir() else py.path.local('.')
            self.vers_file = base.join("version.txt")
        else:
            self.vers_file = py.path.local(vers_file)
            self.base_dir = self.vers_file.dirpath()

    @property
    def release(self):
        return not (self.base_version.is_prerelease or
                    self.base_version.is_postrelease)

    @property
    def base_version(self):
        return pVersion(self.vers_file.read())

    @property
    def sub_rev(self):

        if os.environ.get("SVN_REVISION"):
            return "+{}".format(os.environ["SVN_REVISION"])

        path = py.path.local(self.base_dir.strpath)

        svn_info = subprocess.check_output(
            ["svnversion", "-c", path.strpath],
            stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        return "+{}".format(
            (svn_info.decode('ascii').split(':')[-1]).strip())

    @cached_property(ttl=0)
    def get_version(self):
        """Return current source version string.
        """
        svn_rev = self.sub_rev
        if svn_rev.endswith('M'):
            if self.release:
                raise VersionError("""
***ERROR***
Attempt to generate release from SVN repository that still has changes.
""")
        if self.release:
            return str("{}".format(self.base_version))
        return str("{}{}".format(self.base_version, svn_rev.lower()))

    def __call__(self):
        """Returns current source version string when class instance is called.
        """
        return self.get_version

    def write(self, targets):
        """Write a python module with the version information.

Only actually writes the version info file when a "good" version
number is avaliable.

:param list 'targets': List of version files to write.
"""
        if (sys.version_info < (3, 4) and
                isinstance(targets, basestring) or
                isinstance(targets, str)):
            targets = [targets]
        for target in targets:
            with open(target, 'w') as out:
                out.write("""# Automatically generated version file.

__version__ = \"{}\"\n""".format(self.get_version))

# Local Variables:
# mode: python
# compile-command: "python setup.py build"
# End:

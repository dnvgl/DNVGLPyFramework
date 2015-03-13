#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Handle module version number.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import re
import sys
import subprocess

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2015 by DNV GL SE"


class Version(object):
    """Handle Project version numbers for setup and others."""

    rev_mask = re.compile(r"Revision: (?P<revision>[\d]+)")

    def __init__(self, vers_file=None, release=None):
        """
:param str `vers_file`: Name of file to read version number from.
:param bool `release`: Set to `True` for a release.
"""
        if release is None:
            self.release = os.getenv('RELEASE') is not None
        else:
            self.release = release
        if vers_file is None:
            base = os.path.dirname(__file__)
            self.base_dir = base if base else os.path.abspath('.')
            self.vers_file = os.path.join(self.base_dir, "version.txt")
        else:
            self.vers_file = os.path.abspath(vers_file)
            self.base_dir = os.path.dirname(self.vers_file)
        (self.base_version, self.svn_revision) = (
            self._base_version, self._svn_revision or "")

    @property
    def _base_version(self):
        return open(self.vers_file, 'r').readline().strip()

    @property
    def _svn_revision(self):

        if os.environ.get("SVN_REVISION_1"):
            return os.environ["SVN_REVISION_1"]

        path = os.path.abspath(self.base_dir)

        svn_info = b''

        while (len(svn_info.decode('ascii').split(':')) <= 1 and
               len(os.path.split(path)[-1]) > 1):
            svn_info = subprocess.check_output(
                ["svnversion", "-c", path],
                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            path = os.path.join(*os.path.split(path)[:-1])

        return len(svn_info.decode('ascii').split(':')) > 1 and \
            (svn_info.decode('ascii').split(':')[-1]).strip()

    @property
    def get_version(self):
        """Return current source version string.
        """
        if self.release:
            return str("{}".format(self.base_version))
        else:
            return str("{}.dev{}".format(self.base_version, self.svn_revision))

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
        if (sys.version_info < (3, 4) and isinstance(targets, basestring)) or \
           isinstance(targets, str):
            targets = [targets]
        for target in targets:
            with open(target, 'w') as out:
                out.write("""# Automatically generated version file.

__version__ = \"{}\"\n""".format(self.get_version))

# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "python setup.py build"
# End:

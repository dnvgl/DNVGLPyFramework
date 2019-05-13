#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Handle module version number.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import sys
import codecs
import subprocess

# Third party libraries.
import py
import jinja2
from packaging.version import Version as pVersion

# DNV GL libraries.
from dnvgl.framework.cached_property import cached_property

__date__ = "$Date::                            $" [7:-1]
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2015 by DNV GL SE"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berthold.hoellmann@dnvgl.com"
__scm_version__ = "$Revision$" [10:-1]


class VersionError(Exception):
    pass


class Version(object):
    """Handle Project version numbers for setup and others."""

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
        self._copyright = None

    @property
    def copyright(self):
        if self._copyright is not None:
            return u'__copyright__ = """{}"""\n'.format(
                self._copyright.replace(u'"', u'\\"'))
        return ""

    @copyright.setter
    def copyright(self, inp):
        self._copyright = inp

    @property
    def release(self):
        return not (self.base_version.is_prerelease or
                    self.base_version.is_postrelease)

    @property
    def base_version(self):
        return pVersion(self.vers_file.read())

    @property
    def sub_rev(self):
        if os.environ.get("GIT_REVISION"):
            return "+{}".format(os.environ["GIT_REVISION"])
        if os.environ.get("SVN_REVISION"):
            return "+{}".format(os.environ["SVN_REVISION"])

        if self.base_dir.join('.svn').isdir():
            return self.svn_ref()
        elif self.base_dir.join('.git').isdir():
            return self.git_ref()
        return ""

    def svn_ref(self):

        path = py.path.local(self.base_dir.strpath)

        svn_info = subprocess.check_output(
            ["svnversion", "-c"],
            cwd=path.strpath,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE)
        return "+{}".format((svn_info.decode('ascii').split(':')[-1]).strip())

    def git_ref(self):

        path = py.path.local(self.base_dir.strpath)

        git_info = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=path.strpath,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE)
        flag_info = subprocess.check_output(
            ["git", "status", "--short", "--untracked-files=no"],
            cwd=path.strpath,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE)
        changed = False
        for line in flag_info.decode().split('\n'):
            if line.strip().startswith('M'):
                changed = True
                break
        return "+{}{}".format(
            git_info.decode('ascii').strip(),
            '.m' if changed else "")

    @cached_property(ttl=0)
    def get_version(self):
        """Return current source version string.
        """
        svn_rev = self.sub_rev
        if svn_rev.endswith('M'):
            if self.release:
                text = "\n*** ERROR ***\n"
                if self.base_dir.join('.svn').isdir():
                    text = """
***ERROR***
Attempt to generate release from SVN repository that still has changes.
"""
                elif self.base_dir.join('.git').isdir():
                    text = """
***ERROR***
Attempt to generate release from GIT repository that still has changes.
"""

                raise VersionError(text)
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
            with codecs.open(target, 'w', encoding='utf8') as out:
                out.write(u"""\
# -*- coding: utf-8 -*-
# Automatically generated version file.
from __future__ import unicode_literals

__version__ = \"{}\"\n{}""".format(self.get_version, self.copyright))

    def parse_template(self, template_name):
        """
        Takes jinja2 template file `<some name>.in` from
        `template_name` and writes `<some name>` with `{{ version }}`
        replaced by version number.
        """
        assert template_name.endswith(".in")

        with open(template_name) as inp:
            template = jinja2.Template(inp.read())
        with open(template_name[:-3], 'w') as outp:
            for l in template.generate(version=self.get_version):
                outp.write(l)

# Local Variables:
# mode: python
# compile-command: "python ../../../setup.py test"
# End:

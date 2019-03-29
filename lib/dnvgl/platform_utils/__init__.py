#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Determine python platform name for DNV GL python projects.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import re
import sys
import copy
import argparse
from os.path import isfile
from distutils import util

from .__version__ import __version__

# ID: $Id$
__date__ = "$Date::                            $"[7:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2003 by DNV GL SE"


BRAND_FILES = (
    ("SUSE", '/etc/SuSE-release', r'VERSION = (?P<version>[0-9]+)'),
    ("SLES", '/etc/SuSE-release', r'VERSION = (?P<version>[0-9]+)'),
    ("UBUNTU", '/etc/os-release', r'VERSION_ID="(?P<version>[0-9]+.[0-9]+)"'))


def pyplat(ext=False):
    "Determine current platform string."
    res = util.get_platform()
    for brand, brand_file, ver_info in BRAND_FILES:
        if isfile(brand_file) and ext:
            info = ''.join(open(brand_file).readlines())
            if brand == "SLES" and \
               info.find('SUSE Linux Enterprise Server') >= 0:
                ver = re.search(ver_info, info)
                if ver:
                    if int(ver.groupdict()['version']) == 11:
                        return "%s-SLES11" % res
            elif brand == "UBUNTU":
                ver = re.search(ver_info, info)
                if ver:
                    return "%s-UBUNTU%s" % (res, ver.groupdict()['version'])

    return res


def print_pyplat(ext=False):
    print(pyplat(ext))


def pyver():
    return sys.version[:3]


def print_pyver():
    print(pyver())


class _CMD(object):
    """Command line tool."""

    def __init__(self):
        """Initiate command line tool.

        """
        self.options = self.parser.parse_args()


class PyPlat_CMD(_CMD):
    """PyPlat command line utility."""

    parser = argparse.ArgumentParser(
        description='Get information on current computing plaform.')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(__version__))
    parser.add_argument('-e', '--ext', default=False, required=False,
                        action='store_true',
                        help="Provide extra information.")

    def __init__(self):
        """Initiate.
        """
        super(PyPlatVer_CMD, self).__init__()

    def __call__(self):
        print_pyplat(self.options.ext)


def pyplat_cmd():
    PyPlat_CMD()()


class PyVer_CMD(_CMD):

    """PyPlat command line utility."""

    parser = argparse.ArgumentParser(
        description='Get information on current python version.')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(__version__))

    def __init__(self):
        """Initiate.
        """
        super(PyVer_CMD, self).__init__()

    def __call__(self):
        print_pyver()


def pyver_cmd():
    PyVer_CMD()()


if __name__ == "__main__":
    print_pyplat()
    print_pyver()

# Local Variables:
# mode: python
# compile-command: "cd ../..;python setup.py test"
# End:

#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use PyInstaller to build binary executables from python scripts.

distutils extension.

Use `pyinstaller_specs` argument to `setup` command to specify
PyInstaller `spec` files.
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import distutils
import contextlib
from distutils.dist import Distribution

# Third party libraries.
from PyInstaller.__main__ import run

try:
    from pip import main as pip_main
except ImportError:
    from pip._internal import main as pip_main

# ID: $Id$
__date__ = "$Date::                            $"[7:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2018 by DNV GL SE"


PATH = os.getcwd()
EXE_BUILD_DIR = "build_exe"
# add option to setup command
Distribution.pyinstaller_specs = []


@contextlib.contextmanager
def remember_cwd(tmp_dir):
    curdir = os.getcwd()
    os.chdir(tmp_dir)
    try:
        yield
    finally:
        os.chdir(curdir)


class PyInstallerCommand(distutils.cmd.Command):

    description = "Custom command for running pyInstaller on spec files."
    user_options = []
    pyinstaller_specs = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # install code
        pip_main(['install', '.'])

        specs = self.distribution.pyinstaller_specs

        print("specs: {}".format(specs))

        for spec in specs:
            pyi_args = [
                "--noconfirm", "--onefile", "--distpath=.", "--clean",
                os.path.join(PATH, spec)]

            with remember_cwd(EXE_BUILD_DIR):
                run(pyi_args)

# pyinstaller --noconfirm --onefile --distpath=. --clean  fmi2aml.spec


# Local Variables:
# mode: python
# compile-command: "cd ../../;python setup.py test"
# End:

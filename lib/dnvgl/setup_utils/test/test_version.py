#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing `dnvgl.setup_utils.version`
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import sys
import subprocess

# Third party libraries.
import pytest

# DNV GL libraries.
from dnvgl.setup_utils import version

# ID: $Id$
__date__ = "$Date::                            $"[7:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2016 by DNV GL SE"


@pytest.fixture(params=(
    ("0.0.1", 123, "0.0.1", True),
    ("1.2.3", 123, "1.2.3", True),
    ("1.2.3", "123M", "1.2.3", None),
    ("1.2.3.dev2", 123, "1.2.3.dev2+123", False),
    ("1.2.3.dev2", "123M", "1.2.3.dev2+123m", False),
    ("1.2.3a1", 123, "1.2.3a1+123", False),
    ("1.2.3b1", 123, "1.2.3b1+123", False),
    ("1.2.3.a1", 123, "1.2.3a1+123", False),
    ("1.2.3.b1", 123, "1.2.3b1+123", False)))
def ver_string(request):
    return request.param


def test_ver_explicit_path(tmpdir, monkeypatch, ver_string):
    ver, rev, ref, rel = ver_string
    monkeypatch.setattr(subprocess, "check_output",
                        lambda x, *arg, **kw:
                        bytes("1:{}".format(rev).encode("utf-8")))
    v = tmpdir.join('version.txt')
    v.write(ver)
    probe = version.Version(v)
    if rel is not None:
        assert probe() == ref
    else:
        with pytest.raises(version.VersionError):
            probe()


def test_ver_explicit_path_env(tmpdir, monkeypatch, ver_string):
    ver, rev, ref, rel = ver_string
    monkeypatch.setenv('SVN_REVISION', rev)
    monkeypatch.setattr("subprocess.check_output",
                        lambda x, *arg, **kw: bytes("1:666"))
    v = tmpdir.join('version.txt')
    v.write(ver)
    probe = version.Version(v)
    if rel is not None:
        assert probe() == ref
    else:
        with pytest.raises(version.VersionError):
            probe()


def test_ver_implicit_path(tmpdir, monkeypatch, ver_string):
    ver, rev, ref, rel = ver_string
    v = tmpdir.join('version.txt')
    v.write(ver)
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    monkeypatch.setattr("subprocess.check_output",
                        lambda x, *arg, **kw:
                        bytes("1:{}".format(rev).encode("utf-8")))
    probe = version.Version()
    if rel is not None:
        assert probe() == ref
    else:
        with pytest.raises(version.VersionError):
            probe()


def test_ver_implicit_path_env(tmpdir, monkeypatch, ver_string):
    ver, rev, ref, rel = ver_string
    v = tmpdir.join('version.txt')
    v.write(ver)
    monkeypatch.setenv('SVN_REVISION', rev)
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    monkeypatch.setattr("subprocess.check_output",
                        lambda x, *arg, **kw: bytes("1:666"))
    probe = version.Version()
    if rel is not None:
        assert probe() == ref
    else:
        with pytest.raises(version.VersionError):
            probe()


def test_release(tmpdir, monkeypatch, ver_string):
    ver, rev, ref, rel = ver_string
    v = tmpdir.join('version.txt')
    v.write(ver)
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    monkeypatch.setattr("subprocess.check_output",
                        lambda x, *arg, **kw:
                        bytes("1:{}".format(rev).encode("utf-8")))
    probe = version.Version()
    if rel is not None:
        assert probe.release == rel


def test_release_env(tmpdir, monkeypatch, ver_string):
    ver, rev, ref, rel = ver_string
    v = tmpdir.join('version.txt')
    v.write(ver)
    monkeypatch.setenv('SVN_REVISION', rev)
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    monkeypatch.setattr("subprocess.check_output",
                        lambda x, *arg, **kw: bytes("1:666"))
    probe = version.Version()
    if rel is not None:
        assert probe.release == rel


def test_write(tmpdir, monkeypatch):
    v = tmpdir.join('version.txt')
    v.write("1.2.3")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version()
        probe.write(tmpdir.join("__version.py").strpath)
        assert tmpdir.join("__version.py").read() == '''\
# Automatically generated version file.

__version__ = "1.2.3"
'''


def test_parse_template(tmpdir, monkeypatch):
    v = tmpdir.join('version.txt')
    v.write("1.2.3")
    tmpl = tmpdir.join('parse_template_test.in')
    tmpl.write("""Just a test
{{ version }}
""")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version()
        probe.parse_template(str(tmpl))
        assert tmpdir.join("parse_template_test").read() == '''\
Just a test
1.2.3'''

# Local Variables:
# mode: python
# compile-command: "cd ../../..;python setup.py test"
# End:

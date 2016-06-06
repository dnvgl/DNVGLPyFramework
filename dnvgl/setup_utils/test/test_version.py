#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing `dnvgl.setup_utils.version`
"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals)

# Standard libraries.
import os
import sys

# Third party libraries.
import pytest

from .. import version

# ID: $Id$
__date__ = "$Date::                            $"[7:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2016 by DNV GL SE"


@pytest.fixture(params=(
    ("3", "1.2.3", True),
    ("3", "1.2.dev3", False),
    ("3M", "1.2.3.post1", False)))
def ver_string(request):
    return request.param


def test_ver_explicit_path(tmpdir, monkeypatch, ver_string):
    rev, ref, rel = ver_string
    monkeypatch.setenv('SVN_REVISION_1', rev)
    if rel:
        monkeypatch.setenv('RELEASE', "1")
    else:
        monkeypatch.delenv('RELEASE', raising=False)
    v = tmpdir.join('version.txt')
    v.write("1.2")
    probe = version.Version(v.strpath)
    assert probe() == ref


def test_ver_implicit_path(tmpdir, monkeypatch, ver_string):
    rev, ref, rel = ver_string
    monkeypatch.setenv('SVN_REVISION_1', rev)
    if rel:
        monkeypatch.setenv('RELEASE', "1")
    else:
        monkeypatch.delenv('RELEASE', raising=False)
    v = tmpdir.join('version.txt')
    v.write("1.2")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version()
        assert probe() == ref


def test_ver_call_with_release(tmpdir, monkeypatch, ver_string):
    rev, ref, rel = ver_string
    monkeypatch.setenv('SVN_REVISION_1', rev)
    monkeypatch.delenv('RELEASE', raising=False)
    v = tmpdir.join('version.txt')
    v.write("1.2")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version(release=rel)
        assert probe() == ref


def test_svnversion(tmpdir, monkeypatch, ver_string):
    rev, ref, rel = ver_string
    monkeypatch.delenv('SVN_REVISION_1', raising=False)
    monkeypatch.delenv('RELEASE', raising=False)
    v = tmpdir.join('version.txt')
    v.write("1.2")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    monkeypatch.setattr("subprocess.check_output",
                        lambda x, *arg, **kw:
                        bytes("1:{}".format(rev).encode("utf-8")))
    with v.dirpath().as_cwd():
        probe = version.Version(release=rel)
        assert probe() == ref


def test_with_postfile(tmpdir, monkeypatch):
    monkeypatch.setenv('SVN_REVISION_1', "3M")
    monkeypatch.delenv('RELEASE', raising=False)
    v = tmpdir.join('version.txt')
    v.write("1.2")
    p = tmpdir.join(version.Version.postfile)
    p.write("3")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version()
        assert probe() == "1.2.3.post3"


def test_with_release_error(tmpdir, monkeypatch):
    monkeypatch.setenv('SVN_REVISION_1', "3M")
    monkeypatch.setenv('RELEASE', "1")
    v = tmpdir.join('version.txt')
    v.write("1.2")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version()
        with pytest.raises(version.VersionError):
            probe()


def test_write(tmpdir, monkeypatch):
    monkeypatch.setenv('SVN_REVISION_1', "3")
    monkeypatch.setenv('RELEASE', "1")
    v = tmpdir.join('version.txt')
    v.write("1.2")
    monkeypatch.setattr("sys.argv", (v.strpath, ))
    with v.dirpath().as_cwd():
        probe = version.Version()
        probe.write(tmpdir.join("__version.py").strpath)
        assert tmpdir.join("__version.py").read() == '''\
# Automatically generated version file.

__version__ = "1.2.3"
'''


# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "python setup.py build"
# End:

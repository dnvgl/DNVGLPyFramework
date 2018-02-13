..
  Task: Documenting the `dnvgl.setup_utils` library.

  ID: $Id$"

  :Authors:
    - `Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__
  :Organization: DNV GL SE
  :Version: $Revision$
  :Date: $Date$
  :datestamp: %Y-%m-%d
  :Copyright: Copyright © 2015 by DNV GL SE

=================================
Using :py:mod:`dnvgl.setup_utils`
=================================

:py:mod:`dnvgl.setup_utils` provides helper modules for the setup
process. Currently a module for helping with maintaining version
numbers is available.

By default the version numbers returned by the
:py:class:`dnvgl.setup_utils.version.Version` contain the current svn
revision as `dev` part. When the parameter `release` of
:py:class:`dnvgl.setup_utils.version.Version` is set to `True`, or if
it is left `None` and the environment Variable `RELEASE` is set, a
release version number is generated.

The class instance can be used to define version numbers in the
`setup.py` file,::

  VERSION = Version('version.txt')
  ...
  setup(version=VERSION(),
  ...

or in the `sphinx` `conf.py` file via instantiating::

  import dnvgl.setup_utils.version as my_version
  VERSION = my_version.Version('../version.txt')
  version = '.'.join(VERSION.base_version.split('.')[:2])
  release = VERSION()

For bootstrapping in the `setup.py` file one could use::

  try:
      from dnvgl.setup_utils.version import Version
  except ImportError:
      class Version:
          def __init__(self, *args, **kwds):
              pass

          def write(self, files):
              pass

          def __call__(self):
              return "0.0.-1"

Using :py:mod:`dnvgl.setup_utils.build_exe`
===========================================

This module allows to add a `build_exe` command to `setup.py` to build
binary executables from python scripts using PyInstaller.

To your `setup.py` add_argument::

  from dnvgl.setup_utils.version import Version

  setup(
    ...
    cmdclass={"build_exe": PyInstallerCommand},
    pyinstaller_specs=("build_exe/exe_1.spec",
                       "build_exe/exe_2.spec"),
    ...)

Now `python setup.py build_exe` will process the given `.spec` files
using PyInstaller.

..
  Local Variables:
  mode: rst
  ispell-local-dictionary: "english"
  compile-command: "make html"
  coding: utf-8
  End:

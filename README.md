Simple Framework for DNV GL Python applications. ![logo](doc/DNVGLPyFramework_logo.svg "Logo Title Text")
=========================================================================================================

This Package provides some simple, basic functionality for Python
projects developed at DNV GL.

For one, it is a namespace package, using the `dnvgl` namespace to be
reused by other packages as well.

The module `dnvgl.setup_utils` provides some helper functionality for
the setup process. Currently it contains the module `version` for
hanling version numbers in a consitent fassion and an extension to
generate executables using PyInstaler.

The module `dnvgl.framework` contains misc modules for application
definition and helper functions.

The module `dnvgl.platform_utils` contains code to determine the
python platform name for DNV GL python projects.

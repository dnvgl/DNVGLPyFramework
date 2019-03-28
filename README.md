..
  ID: $Id$"

  :Authors:
    - `Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__
  :Organization: DNV GL SE
  :Version: $Revision$
  :Date: $Date$
  :datestamp: %Y-%m-%d
  :Copyright: Copyright © 2015 by DNV GL SE

==================================================
 Simple Framework for DNV GL Python applications.
==================================================

This Package provides some simple, basic functionality for Python
projects developed at DNV GL.

For one, it is a namespace package, using the `dnvgl` namespace to be
reused by other packages as well.

The module `dnvgl.setup_utils` provides some helper functionality for
the setup process. Currently it contains the module `version` for
hanling version numbers in a consitent fassion.

The module `dnvgl.framework` contains misc modules for application
definition and helper functions.

..
  Local Variables:
  mode: rst
  ispell-local-dictionary: "english"
  compile-command: "make html"
  coding: utf-8
  End:

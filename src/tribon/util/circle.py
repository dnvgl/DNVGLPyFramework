#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Circle calculations

:author: `Berthold Höllmann <berthold.hoellmann@gl-group.com>`__
:newfield project: Project
:project: Tribon XML converter
:copyright: Copyright (C) 2009 by Germanischer Lloyd AG"""

from __future__ import absolute_import

#  ID: $Id$
__date__      = u"$Date$"[5:-1]
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import numpy as np
import numpy.linalg as la

class Circle3n(object):
    """
Class to manage circle information for circles build from 3 nodes on
the circumference.
"""

    def __init__(self, pnt1, pnt2, pnt3):
        """
>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> print c.radius, c.centre
1.0 [-0. -0.]
"""
        self.pnt1 = np.array(pnt1, dtype=np.dtype("float"))
        self.pnt2 = np.array(pnt2, dtype=np.dtype("float"))
        self.pnt3 = np.array(pnt3, dtype=np.dtype("float"))
        self.__radius = None
        self.__centre = None

    def __calc(self):
        """
Calculate circle properties centre and radius from three points on the
circle circumference.

After solving the linear system of equations:

  - A + B(-x1) + C(-y1) = -(x1² + y1²)
  - A + B(-x2) + C(-y2) = -(x2² + y2²)
  - A + B(-x3) + C(-y3) = -(x3² + y3²)

centre and radius are calculated from:

  xm = B/2, ym = C/2, und r² = xm² + ym² - A

Derivation and formula taken from
<http://www.arndt-bruenner.de/mathe/scripts/kreis3p.htm>
"""
        a = np.ones((3, 3))
        a[0, 1:] = -self.pnt1
        a[1, 1:] = -self.pnt2
        a[2, 1:] = -self.pnt3
        b = np.array((-(self.pnt1**2).sum(),
                      -(self.pnt2**2).sum(),
                      -(self.pnt3**2).sum()))
        x = la.solve(a, b)
        self.__centre = x[1:]/2
        self.__radius = np.sqrt((self.__centre**2).sum() - x[0])

    def get_radius(self):
        """
Return radius of current circle.

If not yet done, calculate radius and centre using the `__calc` method.
"""
        if self.__radius is None:
            self.__calc()
        return self.__radius

    radius = property(get_radius, doc="Radius belonging to circle.")

    def get_centre(self):
        """
Return centre of current circle.

If not yet done, calculate radius and centre using the `__calc` method.
"""
        if self.__centre is None:
            self.__calc()
        return self.__centre

    centre = property(get_centre,
                      doc="Centre position belonging to given circle.")

    def point(self, phiVal):
        """
Calculate a point on the circle circumference given by the parametric
variable `phiVal`. Meaningful values for `phiVal` come from the interval [0..2pi[,
whereas each value for `phiVal` returns a point on the circumference.

:Parameters:
  phiVal : `float`
    Parametric coordinate on the circumference.

:Returns:
  (float, float)
    Cartesian coordinates of point belonging to ``phiVal`` on circumference.

>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> print c.point(0)
[ 0.  1.]
"""
        return (np.array((np.sin(phiVal), np.cos(phiVal)))*
                self.radius)+self.centre

    def phi(self, point):
        """
Reverse lookup for parametric coordinate belonging to a given point.

:Parameters:
  point : (float, float)
    Point on circumference.

:Returns:
  float
    Parametric coordinate belonging to ``point``


>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> np.allclose((0, 1), c.point(c.phi((0, 1))))
True
"""
        x, y = np.asarray(point, dtype=np.dtype(float))
        rad = self.radius
        xm, ym = self.centre
        norm = (point-self.centre)/rad
        if np.sometrue(norm > 1.) or np.sometrue(norm < -1.):
            if (np.sometrue(norm > 1.) and
                np.allclose(norm[np.nonzero(norm > 1.)], 1.)):
                norm[np.nonzero(norm > 1.)] = 1.
            if (np.sometrue(norm < -1.) and
                np.allclose(norm[np.nonzero(norm < -1.)], -1.)):
                norm[np.nonzero(norm < -1.)] = -1.
        n = np.array(
            [ f(v)
              for f, v in zip((np.arcsin, np.arccos), norm) ])
        if (x-xm) >= 0:
            if (y-ym)/rad >= 0:
                return n[0]
            else:
                return n[1]
        else:
            if (y-ym)/rad >= 0:
                return n[0]+2.*np.pi
            else:
                return 2.*np.pi-n[1]


if __name__ == "__main__":
    from matplotlib import pylab
    C_COLL = ((Circle3n((-1, 0), ( 0   ,  1   ), ( 1, 0)), 'bo'),
              (Circle3n(( 0, 0), ( 1   ,  1   ), ( 2, 0)), 'gv'),
              (Circle3n(( 0, 1), ( 1   ,  2   ), ( 2, 1)), 'r^'),
              (Circle3n((-2, 4), ( 1   , -3   ), ( 5, 7)), 'c<'),
              (Circle3n(( 6, 8), ( 2   , -2   ), (-1, 5)), 'm>'),
              (Circle3n(( 4, 6), ( 4.58, -3.74), (-3, 3)), 'yD'))
    for (c, m) in C_COLL:
        data = np.array([ c.point(phi)
                          for phi in np.arange(0, 2*np.pi+.01, .01) ])
        pylab.plot([c.pnt1[0]], [c.pnt1[1]], m, [c.pnt2[0]], [c.pnt2[1]], m,
                   [c.pnt3[0]], [c.pnt3[1]], m,
                   data[:,0], data[:,1], "%c-" % m[0] )
    pylab.show()

# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"make -C ../../../ test"
# End:


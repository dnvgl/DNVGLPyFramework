#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Circle calculations

:author: `Berthold Höllmann <berthold.hoellmann@gl-group.com>`__
:newfield project: Project
:project: Tribon XML converter
:copyright: Copyright (C) 2009 by Germanischer Lloyd AG"""

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

    def __init__(self, point1, point2, point3):
        """
>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> print c.radius, c.centre
1.0 [-0. -0.]
"""
        self.point1 = np.array(point1, dtype=np.dtype("float"))
        self.point2 = np.array(point2, dtype=np.dtype("float"))
        self.point3 = np.array(point3, dtype=np.dtype("float"))
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
        a[0, 1:] = -self.point1
        a[1, 1:] = -self.point2
        a[2, 1:] = -self.point3
        b = np.array((-(self.point1**2).sum(),
                      -(self.point2**2).sum(),
                      -(self.point3**2).sum()))
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

    centre = property(get_centre, doc="Centre position belonging to given circle.")

    def point(self, u):
        """
Calculate a point on the circle circumference given by the parametric
variable `u`. Meaningful values for u come from the interval [0..2pi[,
whereas each value for `u` returns a point on the circumference.

:Parameters:
  u : `float`
    Parametric coordinate on the circumference.

:Returns:
  (float, float)
    Cartesian coordinates of point belonging to ``u`` on circumference.

>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> print c.point(0)
[ 0.  1.]
"""
        return (np.array((np.sin(u), np.cos(u)))*self.radius)+self.centre

    def u(self, point):
        """
Reverse lookup for parametric coordinate belonging to a given point.

:Parameters:
  point : (float, float)
    Point on circumference.

:Returns:
  float
    Parametric coordinate belonging to ``point``


>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> np.allclose((0, 1), c.point(c.u((0, 1))))
True
"""
        x, y = np.asarray(point, dtype=np.dtype(float))
        r = self.radius
        xm, ym = self.centre
        norm = (point-self.centre)/r
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
            if (y-ym)/r >= 0:
                return n[0]
            else:
                return n[1]
        else:
            if (y-ym)/r >= 0:
                return n[0]+2.*np.pi
            else:
                return 2.*np.pi-n[1]


# Local Variables:
# mode:python
# mode:flyspell
# compile-command:"make -C ../../../ test"
# End:

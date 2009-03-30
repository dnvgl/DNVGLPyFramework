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
the circumference in 3D space.
"""
    def __init__(self, pnt1, pnt2, pnt3):
        """
>>> c = Circle3n((-1, 0), (0, 1), (1, 0))
>>> print c.radius, c.centre
1.0 [-0.  0.]
"""
        self.__pnt1 = np.zeros(3, dtype=np.dtype("float"))
        self.__pnt2 = np.zeros(3, dtype=np.dtype("float"))
        self.__pnt3 = np.zeros(3, dtype=np.dtype("float"))

        self.__dimens = len(pnt1)
        self.__pnt1[:self.__dimens] = pnt1
        self.__pnt2[:self.__dimens] = pnt2
        self.__pnt3[:self.__dimens] = pnt3
        self.__radius = None
        self.__centre = None
        self.__s = None
        self.__t = None

    @property
    def pnt1(self):
        return self.__pnt1[:self.__dimens]

    @property
    def pnt2(self):
        return self.__pnt2[:self.__dimens]

    @property
    def pnt3(self):
        return self.__pnt3[:self.__dimens]

    @property
    def centre(self):
        """
Centre position belonging to given circle.

If not yet done, calculate radius and centre using the `__calc` method.
"""
        if self.__centre is None:
            self.__calc()
        return self.__centre[:self.__dimens]

    @property
    def radius(self):
        if self.__radius is None:
            self.__calc()
        return self.__radius

    @property
    def s(self):
        if self.__s is None:
            self.__calc()
        return self.__s

    @property
    def t(self):
        if self.__t is None:
            self.__calc()
        return self.__t

    def __calc(self):

        x_A, y_A, z_A = self.__pnt1
        x_B, y_B, z_B = self.__pnt2
        x_C, y_C, z_C = self.__pnt3

        a_1 = (y_B*z_C+y_A*(z_B-z_C)-y_C*z_B-(y_B-y_C)*z_A)
        b_1 = -(x_B*z_C+x_A*(z_B-z_C)-x_C*z_B-(x_B-x_C)*z_A)
        c_1 = +(x_B*y_C+x_A*(y_B-y_C)-x_C*y_B-(x_B-x_C)*y_A)
        d_1 = -x_A*(y_B*z_C-y_C*z_B)+y_A*(x_B*z_C-x_C*z_B)-(x_B*y_C-x_C*y_B)*z_A

        D = (self.__pnt1 + self.__pnt2)/2.
        n_2 = self._normalize(self.__pnt2 - self.__pnt1)
        d_2 = -(D * n_2).sum()

        E = (self.__pnt2 + self.__pnt3)/2.
        n_3 = self._normalize(self.__pnt3 - self.__pnt2)
        d_3 = -(E * n_3).sum()

        A = np.zeros((3, 3), dtype=np.dtype('float'))
        A[0, :] = (-a_1, -b_1, -c_1)
        A[1, :] = -n_2
        A[2, :] = -n_3
        b = np.array((d_1, d_2, d_3))

        self.__centre = la.solve(A, b.T)
        self.__s = self.__pnt1 - self.__centre
        self.__radius = np.sqrt(((self.__s)**2).sum())
        self.__t = self._normalize(np.cross(self.__s, (-a_1, -b_1, -c_1)))*self.__radius

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
[-1.  0.]
"""
        return (np.cos(phiVal)*self.s + np.sin(phiVal)*self.t)[:self.__dimens] + self.centre

    @staticmethod
    def _normalize(vec):
        return vec/np.sqrt((vec**2).sum())

    def phi(self, point):
        """
Reverse lookup for parametric coordinate belonging to a given point.

:Parameters:
  point : (float, float, [float])
    Point on circumference.

:Returns:
  float
    Parametric coordinate belonging to ``point``


> >> c = Circle3n((-1, 0), (0, 1), (1, 0))
> >> np.allclose((0, 1), c.point(c.phi((0, 1))))
True
"""
        norm = self._normalize((point-self.centre[:self.__dimens]))
        if np.dot(self._normalize(self.t[:self.__dimens]), norm) >= -1e-8:
            return np.arccos(max(-1., min(1., np.dot(self._normalize(self.s[:self.__dimens]), norm))))
        else:
            return 2*np.pi - np.arccos(max(-1., min(1., np.dot(self._normalize(self.s[:self.__dimens]), norm))))

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


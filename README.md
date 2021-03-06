[![TravisCI](https://travis-ci.org/scikit-fmm/scikit-fmm.svg?branch=master)](https://travis-ci.org/scikit-fmm/scikit-fmm)[![PyPI version](https://badge.fury.io/py/scikit-fmm.svg)](http://pypi.python.org/pypi/scikit-fmm)

# scikit-fmm: the fast marching method for Python

`scikit-fmm` is a Python extension module which implements the fast marching method.
The fast marching method is used to model the evolution of boundaries
and interfaces in a variety of application areas. More specifically,
the fast marching method is a numerical technique for finding
approximate solutions to boundary value problems of the Eikonal
equation:

F(x) | grad T(x) | = 1

Typically, such a problem describes the evolution of a closed curve as
a function of time T with speed F(x)>0 in the normal direction at a
point x on the curve. The speed function is specified, and the time at
which the contour crosses a point x is obtained by solving the
equation.

scikit-fmm is a simple module which provides functions to calculate
the signed distance and travel time to an interface described by the
zero contour of the input array phi.

```python
import skfmm
import numpy as np
phi = np.ones((3, 3))
phi[1, 1] = -1
skfmm.distance(phi)
```

  ```python
   array([[ 1.20710678,  0.5       ,  1.20710678],
          [ 0.5       , -0.35355339,  0.5       ],
          [ 1.20710678,  0.5       ,  1.20710678]])
  ```
---
```python
skfmm.travel_time(phi, speed = 3.0 * np.ones_like(phi))
```

   ```python
   array([[ 0.40236893,  0.16666667,  0.40236893],
          [ 0.16666667,  0.11785113,  0.16666667],
          [ 0.40236893,  0.16666667,  0.40236893]])
   ```
---

The input array can be of 1, 2, 3 or higher dimensions and can be a
masked array. A function is provided to compute extension velocities.

### Documentation
* Release Version: http://packages.python.org/scikit-fmm
* Development Version: http://scikit-fmm.readthedocs.org/en/latest/

### PyPI
* http://pypi.python.org/pypi/scikit-fmm

### Requirements
* Numpy >= 1.0.2
* Building requires a C/C++ compiler (gcc, MinGW, MSVC)

### Bugs, questions, patches, feature requests, discussion & cetera
* Open a GitHub pull request or a GitHub issue
* Email list: http://groups.google.com/group/scikit-fmm
  * Send an email to scikit-fmm+subscribe@googlegroups.com to subscribe.

### Installing
* Via pip: `pip install scikit-fmm`
* From source: `python setup.py install`
* 64-bit Windows binaries from Christoph Gohlke:
  * http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-fmm
* 64-bit Conda package for Py27:
  * https://binstar.org/jmargeta/scikit-fmm

### Running Tests
* `python -c "import skfmm; skfmm.test(True)"`
* When running the tests from the source directory use `python setup.py develop`
* Tests are doctests in `skfmm/__init__.py`

### Building documentation
* Requires sphinx and numpydoc
* `make html`

### Version History:
* 0.0.1: February 13 2012
  * Initial release
* 0.0.2: February 26th 2012
  * Including tests and docs in source distribution. Minor changes to
    documentation.
* 0.0.3: August 4th 2012
  * Extension velocities.
  * Fixes for 64 bit platforms.
  * Optional keyword argument for point update order.
  * Bug reports and patches from three contributors.
* 0.0.4: October 15th 2012
   * Contributions from Daniel Wheeler:
     * Bug fixes in extension velocity.
     * Many additional tests and migration to doctest format.
     * Additional optional input to extension_velocities() for FiPy compatibly.
* 0.0.5: May 12th 2014
   * Fix for building with MSVC (Jan Margeta).
   * Corrected second-order point update.
* 0.0.6: February 20th 2015
   * Documentation clarification (Geordie McBain).
   * Python 3 port (Eugene Prilepin).
   * Python wrapper for binary min-heap.
   * Freeze equidistant narrow-band points simultaneously.
* 0.0.7: October 21st 2015
   * Bug fix to upwind finite difference approximation for negative
     phi from Lester Hedges.
* 0.0.8: March 9th 2016
   * Narrow band capability: an optional "narrow" keyword argument
     limits the extent of the marching algorithm (Adrian Butscher).

Copyright 2016 The scikit-fmm team.

BSD-style license. See LICENSE.txt in the source directory.

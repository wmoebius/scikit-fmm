#!/usr/bin/env python
import os
import sys
import setuptools

long_description = """scikit-fmm is a Python extension module which implements the fast
marching method.

- Signed distance functions
- Travel time transforms (solutions to the Eikonal equation)
- Extension velocities

https://github.com/scikit-fmm/scikit-fmm
"""

DISTNAME         = "scikit-fmm"
DESCRIPTION      = "An extension module implementing the fast marching method"
MAINTAINER       = "Jason Furtney"
MAINTAINER_EMAIL = "jkfurtney@gmail.com"
VERSION          = "0.0.8"
URL              = 'https://github.com/scikit-fmm/scikit-fmm'
LICENSE          = 'BSD'
KEYWORDS         = "fast marching method, Eikonal equation, interface, boundary"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True)

    config.add_subpackage('skfmm')

    return config

def setup_package():
    from numpy.distutils.core import setup
    setup(
        name             = DISTNAME,
        version          = VERSION,
        maintainer       = MAINTAINER,
        maintainer_email = MAINTAINER_EMAIL,
        description      = DESCRIPTION,
        url              = URL,
        license          = LICENSE,
        keywords         = KEYWORDS,
        long_description = long_description,
        configuration    = configuration,
        install_requires = ['numpy >= 1.0.2'],
        classifiers      = ["Development Status :: 5 - Production/Stable",
                            "License :: OSI Approved :: BSD License",
                            "Operating System :: OS Independent",
                            "Topic :: Scientific/Engineering",
                            "Intended Audience :: Science/Research",
                            "Programming Language :: C++",
                            "Programming Language :: Python :: 2",
                            "Programming Language :: Python :: 3"])

if __name__ == '__main__':
    setup_package()

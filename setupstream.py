#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:01:47 2022

@author: federica
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("cythonfnstream.pyx", 
                            compiler_directives={"language_level": "3"}),
                            include_dirs=[numpy.get_include()])

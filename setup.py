# only one file for compiling

# build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules= cythonize('gradientDescent.pyx'))
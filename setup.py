import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'src'), np.get_include()]

# Define extensions
# Form is: Extension(end_module_name, [sources], include_dirs, language)
stl_cont = Extension("hbspy.stlcontainers", ["hbspy/stlcontainers.pyx"],
                     include_dirs=incdirs, language="c++")

xdress_extras = Extension("hbspy.xdress_extra_types",
                          ["hbspy/xdress_extra_types.pyx"],
                          include_dirs=incdirs, language="c++")

Foobar = Extension("foopy.Foobar",
                   ["foopy/Foobar.pyx"],
                   include_dirs=incdirs, language="c++")

Foobar2 = Extension("foopy.Foobar2",
                   ["foopy/Foobar2.pyx"],
                   include_dirs=incdirs, language="c++")

# List modules we want to build
ext_modules = [stl_cont, xdress_extras, Foobar, Foobar2]

setup(
  name = 'hbspy',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['hbspy']
)

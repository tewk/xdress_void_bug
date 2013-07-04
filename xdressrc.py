## Do basic setup
package = 'foopy'  # top-level python package name
packagedir = 'foopy'  # location of the generated python package
sourcedir = 'src'  # location of the original C++ source

## List the plugins we need. This step is optional, but we use it because we
# need to filter out some types
plugins = ('xdress.stlwrap', 'xdress.autoall', 'xdress.autodescribe',
           # 'xdress.doxygen',
           'xdress.descfilter',
           'xdress.cythongen')

# Which types to ignore or exclude in the wrappers
#skiptypes = ['Point', 'Point3d', 'APoint3d']
#skipmethods = {'HNurbs': ['print']}

## Which stl containers we need for this code
stlcontainers = [
    # NOTE: There is an xdress bug that makes it fail to compile if a 'set' or
    #       'map' container isn't included in this list.
    ('set', 'uint'),
    ('vector', 'float64'),  # DoubleVec
    ('vector', 'int32'),  # IntVec
    ('vector', ('vector', 'int32')),  # IntVecVec
    ('vector', ('vector', 'float64'))   # DoubleVecVec
    ]

## Which classes to create wrappers for.
classes = [
    # classname, source filename[, destination filename]
    ('Foobar', 'Test', 'Foobar'),
    # ('Point3d', 'Point')
    ('Foobar2', 'Test2', 'Foobar2'),
    ]

## Which functions to create wrappers for
functions = [
# function, source filename[, destination filename]
# ('linearParameterizeNURBS', 'HNurbs')
]

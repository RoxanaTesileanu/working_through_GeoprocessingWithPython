Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from distutils.core import setup
>>> import numpy
>>> import os
>>> os.chdir('/home/roxana/working_through_GeoprocessingWithPython/ospybook-1.0/ospybook')
>>> setup(
    name='ospybook',
    version='1.0',
    author='Chris Garrard',
    author_email='garrard.chris@gmail.com',
    packages=['ospybook'],
    url='https://github.com/cgarrard/osgeopy-code/',
    license='LICENSE.txt',
    description='Module for the book Geoprocessing with Python.',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy",
        "matplotlib",
        # "osgeo",
    ],
)

Traceback (most recent call last):
  File "<pyshell#4>", line 10, in <module>
    long_description=open('README.txt').read(),
IOError: [Errno 2] No such file or directory: 'README.txt'
>>> os.chdir('/home/roxana/working_through_GeoprocessingWithPython/ospybook-1.0')
>>> setup(
    name='ospybook',
    version='1.0',
    author='Chris Garrard',
    author_email='garrard.chris@gmail.com',
    packages=['ospybook'],
    url='https://github.com/cgarrard/osgeopy-code/',
    license='LICENSE.txt',
    description='Module for the book Geoprocessing with Python.',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy",
        "matplotlib",
        # "osgeo",
    ],
)

Warning (from warnings module):
  File "/usr/lib/python2.7/distutils/dist.py", line 267
    warnings.warn(msg)
UserWarning: Unknown distribution option: 'install_requires'
>>> from osgeo import ogr
>>> setup(
    name='ospybook',
    version='1.0',
    author='Chris Garrard',
    author_email='garrard.chris@gmail.com',
    packages=['ospybook'],
    url='https://github.com/cgarrard/osgeopy-code/',
    license='LICENSE.txt',
    description='Module for the book Geoprocessing with Python.',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy",
        "matplotlib",
        # "osgeo",
    ],
)

>>> 
>>> import ospybook as pb
>>> from ospybook.vectorplotter import VectorPlotter
>>> vp = Vectorplotter(True)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    vp = Vectorplotter(True)
NameError: name 'Vectorplotter' is not defined
>>> vp = VectorPlotter(True)
>>> firepit = ogr.Geometry(ogr.wkbPoint)
>>> firepit.AddPoint(59.5, 11.5)
>>> vp.plot(firepit, 'rs')
>>> 
>>> 
>>> draw

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    draw
NameError: name 'draw' is not defined
>>> firepit.AddPoint(59.5, 13)
>>> print(fireprint)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(fireprint)
NameError: name 'fireprint' is not defined
>>> print(firepit)
POINT (59.5 13.0 0)
>>> firepit.SetPoint(0, 59.5, 13)
>>> firepit2= ogr.Geometry(ogr.wkbPoint25D)
>>> firepit2.AddPoint(59.5, 11.5, 2)
>>> ### multipoint object
>>> faucets = ogr.Geometry(ogr.wkbMultiPoint)
>>> faucet = ogr.Geometry(ogr.wkbPoint)
>>> faucet.AddPoint(67.5, 16)
>>> faucets.AddGeometry(faucet)
0
>>> faucet.AddPoint(73, 31)
>>> faucets.AddGeometry(faucet)
0
>>> faucet.AddPoint(91, 24.5)
>>> faucets.AddGeometry(faucet)
0
>>> print(faucets)
MULTIPOINT (67.5 16.0 0,73 31 0,91.0 24.5 0)
>>> faucets.GetGeometryRef(1).AddPoint(75, 32)
>>> faucets.GetGeometryCount()
3
>>> for i in range (faucets.GetGeometryCount()) :
	pt = faucets.GetGeometryRef(i)
	pt.AddPoint(pt.GetX() + 2, pt.GetY()0
		    
SyntaxError: invalid syntax
>>> for i in range (faucets.GetGeometryCount()) :
	pt = faucets.GetGeometry(i)
	pt.AddPoint (pt.GetX() +2 , pt.GetY())

	

Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    pt = faucets.GetGeometry(i)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 4169, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Geometry, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> for i in range (faucets.GetGeometryCount()) :
	pt = faucets.GetGeometryRef(i)
	pt.AddPoint((pt.GetX() + 2), pt.GetY())

	
>>> 
>>> vp.plot(faucets, 'rs')
>>> 

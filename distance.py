Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> pt1_2d = ogr.Geometry(ogr.wkbPoint)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pt1_2d = ogr.Geometry(ogr.wkbPoint)
NameError: name 'ogr' is not defined
>>> from osgeo import ogr
>>> pt1_2d = ogr.Geometry(ogr.wkbPoint)
>>> pt1_2d.AddPoint(15,15)
>>> pt2_2d = ogr.Geometry(ogr.wkbPoint)
>>> pt2_2d.AddPoint(15, 19)
>>> print(pt1_2d.Distance(pt2_2d)


      )
4.0
>>> # returns a distance of 4 units
>>> pt1_25d=ogr.Geometry(ogr.wkbPoint25D)
>>> pt1_25d.AddPoint(15, 15, 0)
>>> pt2_25d= ogr.Geometry(ogr.wkbPoint25D)
>>> pt2_25d.AddPoint(15,19,3)
>>> print(pt1_25d.Distance(pt2_25d)

      )
4.0
>>> # but the real distance is 5!
>>> 
>>> # OGR DOESN'T TAKE Z VALUES INTO ACCOUNT WHEN PERFORMING SPATIAL OPERATIONS!
>>> ring = ogr.Geometry(ogr.wkbLinearRing)
>>> ring.AddPoint(10, 10)
>>> ring.AddPoint(10, 20)
>>> ring.AddPoint(20, 10)
>>> ring.AddPoint(20, 20)
>>> poly_2d = ogr.Geometry(ogr.wkbPolygon)
>>> poly_2d.AddGeometry(ring)
0
>>> poly_2d.CloseRings()
>>> print(poly_2d.GetArea())
0.0
>>> ring = ogr.Geometry(ogr.wkbLinearRing)
>>> ring.AddPoint(10, 10)
>>> poly_2d.IsValid()
False
>>> ring.AddPoint(10, 20)
>>> ring.AddPoint(20,20)
>>> ring.AddPoint(20, 10)
>>> poly_2d.ogr.Geometry(ogr.wkbPolygon)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    poly_2d.ogr.Geometry(ogr.wkbPolygon)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 4169, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Geometry, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> poly_2d = ogr.Geometry(ogr.wkbPolygon)
>>> poly_2d.AddGeometry(ring)
0
>>> poly_2d.CloseRings()
>>> print(poly_2d.GetArea())
100.0
>>> # again if we were to take a 2.5D geometry object it will return a flawed answer! 

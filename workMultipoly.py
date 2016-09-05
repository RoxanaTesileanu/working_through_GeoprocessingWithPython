Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> ring = ogr.Geometry(org.wkbLinearRing)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ring = ogr.Geometry(org.wkbLinearRing)
NameError: name 'org' is not defined
>>> ring = ogr.Geometry(ogr.wkbLinearRing)
>>> ring.AddPoint(58, 38.5)
>>> ring.AddPoint(53, 6)
>>> ring.AddPoint(99.5, 19)
>>> ring.AddPoint(73, 42)
>>> yard = ogr.Geometry(ogr.wkbPolygon)
>>> yard.AddGeometry(ring)
0
>>> yard.CloseRings()
>>> print(yard)
POLYGON ((58.0 38.5 0,53 6 0,99.5 19.0 0,73 42 0,58.0 38.5 0))
>>> yard.IsValid()
True
>>> ring = yard.GetGeometryRef(0)
>>> for i in range (ring.GetPointCount()) : ring.SetPoint(i, (ring.GetX(i) - 5, ring.GetY(i))




						      )


Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for i in range (ring.GetPointCount()) : ring.SetPoint(i, (ring.GetX(i) - 5, ring.GetY(i))
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 4407, in SetPoint
    return _ogr.Geometry_SetPoint(self, *args, **kwargs)
TypeError: Required argument 'y' (pos 4) not found
>>> for i in range (ring.GetPointCount()) :
	ring.SetPoint(i, (ring.GetX(i) -5), ring.GetY(i))

	
>>> box1 = ogr.Geometry(ogr.wkbLinearRing)
>>> box1.AddPoint(87.5, 25.5)
>>> box1.AddPoint(89,25.5)
>>> box1.AddPoint(87.5, 24)
>>> garden1 = ogr.Geometry(ogr.wkbPolygon)
>>> garden1.AddGeometry(box1)
0
>>> 
>>> box2 = ogr.Geometry(ogr.wkbLinearRing)
>>> box2.AddPoint(89, 23)
>>> box2.AddPoint(92, 23)
>>> box2.AddPoint(92, 22)
>>> box2.AddPoint(89, 22)
>>> garden2 = ogr.Geometry(ogr.wkbPolygon)
>>> garden2.AddGeometry(box2)
0
>>> 
>>> gardens = ogr.Geometry(ogr.wkbMultipolygon)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    gardens = ogr.Geometry(ogr.wkbMultipolygon)
AttributeError: 'module' object has no attribute 'wkbMultipolygon'
>>> gardens = ogr.Geometry(ogr.wkbMultiPolygon)
>>> gardens.AddGeometry(garden1)
0
>>> gardens.AddGeometry(garden2)
0
>>> gardens.CloseRings()
>>> print(gardens)
MULTIPOLYGON (((87.5 25.5 0,89.0 25.5 0,87.5 24.0 0,87.5 25.5 0)),((89 23 0,92 23 0,92 22 0,89 22 0,89 23 0)))
>>> gardens.IsValid()
True
>>> for i in range (gardens.GetGeometryCount()) :
	ring = gardens.GetGeometryRef(i).GetGeometryRef(0)
	for j in range(ring.GetPointCount()) :
		ring.SetPoint(j, (ring.GetX(j) +1), (ring.GetY(j) +0.5))

		
>>> ###### Polygons with holes
>>> 
>>> lot = ogr.Geometry(ogr.wkbLinearRing)
>>> lot.AddPoint(58, 38.5)
>>> lot.AddPoint(53, 6)
>>> lot.AddPoint(99.5, 19)
>>> lot.AddPoint(73, 42)
>>> 
>>> house = ogr.Geometry(ogr.wkbLinearRing)
>>> house.AddPoint(67.5, 29)
>>> house.AddPoint(69, 25.5)
>>> house.AddPoint(64, 23)
>>> house.AddPoint(69, 15)
>>> house.AddPoint(82.5, 22)
>>> house.AddPoint(76, 31.5)
>>> 
>>> yard = ogr.Geometry(ogr.wkbPolygon)
>>> yard.AddGeometry(lot)
0
>>> yard.AddGeometry(house)
0
>>> yard.CloseRings()
>>> 
>>> print(yard)
POLYGON ((58.0 38.5 0,53 6 0,99.5 19.0 0,73 42 0,58.0 38.5 0),(67.5 29.0 0,69.0 25.5 0,64 23 0,69 15 0,82.5 22.0 0,76.0 31.5 0,67.5 29.0 0))
>>> for i in range (yard.GetGeometryCount()) :
	ring = yard.GetGeometryRef(i)
	for j in range (ring.GetPointCount()) :
		ring.SetPoint(j, (ring.SetX(j) -5), ring.SetY(j))

		

Traceback (most recent call last):
  File "<pyshell#102>", line 4, in <module>
    ring.SetPoint(j, (ring.SetX(j) -5), ring.SetY(j))
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 4169, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Geometry, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> for i in range(yard.GetGeometryCount()) :
	ring=yard.GetGeometryRef(i)
	for j in range (ring.GetPointCount()) :
		ring.SetPoint(j, (ring.GetX(j) -5), ring.GetY(j))

		
>>> 

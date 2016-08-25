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

	
>>> 

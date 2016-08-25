Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path_ds= '//home//roxana/myyard1.shp
SyntaxError: EOL while scanning string literal
>>> path_ds = '//home//roxana//myyard1.shp'
>>> ds = ogr.Open(path_ds, 1)
>>> ring = ogr.Geometry(ogr.wkbLinearRing)
>>> ring.AddPoint(58,38.5)
>>> ring.AddPoint(53, 6)
>>> ring.AddPoint(99.5, 15)
>>> ring.AddPoint(73, 42)
>>> yard.AddGeometry(ring)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    yard.AddGeometry(ring)
NameError: name 'yard' is not defined
>>> yard = ogr.Geometry(ogr.wkbPolygon)
>>> yard.AddGeometry(ring)
0
>>> yard.CloseRings()
>>> yard.IsValid()
True
>>> lyr = ds.GetLayer(0)
>>> print(lyr.GetName())
myyard1
>>> lyr.GetGeometryColumn()
''
>>> lyr_geom = lyr.GetGeometryColumn()
>>> lyr.CreateFeature(*yard)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    lyr.CreateFeature(*yard)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: in method 'Layer_CreateFeature', argument 2 of type 'OGRFeatureShadow *'
>>> lyr.CreateFeature(yard, ogr.wkbPolygon)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    lyr.CreateFeature(yard, ogr.wkbPolygon)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: Layer_CreateFeature() takes exactly 2 arguments (3 given)
>>> lyr.CreateFeature(yard, lyr_geom)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lyr.CreateFeature(yard, lyr_geom)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: Layer_CreateFeature() takes exactly 2 arguments (3 given)
>>> lyrdfn = lyr.GetLayerDefn()
>>> lyr.GetFeature
<bound method Layer.GetFeature of <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fc0f00a0030> >>
>>> lyr.GetFeatureCount()
0
>>> myfeat = ogr.Feature(lyrdfn)
>>> lyrgeom = lyr.GetGeomType ()
>>> myfeat = SetGeometry(lyrgeom)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    myfeat = SetGeometry(lyrgeom)
NameError: name 'SetGeometry' is not defined
>>> myfeat.SetGeometry(lyrgeom)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    myfeat.SetGeometry(lyrgeom)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 2374, in SetGeometry
    return _ogr.Feature_SetGeometry(self, *args)
TypeError: in method 'Feature_SetGeometry', argument 2 of type 'OGRGeometryShadow *'
>>> myfeat.SetGeometry(ogr.wkbPolygon)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    myfeat.SetGeometry(ogr.wkbPolygon)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 2374, in SetGeometry
    return _ogr.Feature_SetGeometry(self, *args)
TypeError: in method 'Feature_SetGeometry', argument 2 of type 'OGRGeometryShadow *'
>>> lyr.geometry

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lyr.geometry
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1060, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> lyrgeom = lyr.geometry()

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lyrgeom = lyr.geometry()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1060, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> myfeat.SetGeometry(yard)
0
>>> lyr.CreateFeature(myfeat)
0
>>> lyr.GetFeatureCount()
1
>>> del ds
>>> 

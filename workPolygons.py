Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
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
>>> yard.GetSpatialRef()

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    yard.GetSpatialRef()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 4169, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Geometry, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> yard.GetBoundary
<bound method Geometry.GetBoundary of <osgeo.ogr.Geometry; proxy of <Swig Object of type 'OGRGeometryShadow *' at 0x7fba0c6718a0> >>
>>> print (yard.GetBoundary)
<bound method Geometry.GetBoundary of <osgeo.ogr.Geometry; proxy of <Swig Object of type 'OGRGeometryShadow *' at 0x7fba0c6718a0> >>
>>> yard.GetSpatialReference()
>>> print (yard.GetSpatialReference)
<bound method Geometry.GetSpatialReference of <osgeo.ogr.Geometry; proxy of <Swig Object of type 'OGRGeometryShadow *' at 0x7fba0c6718a0> >>
>>> spref= yard.GetSpatialReference()
>>> geom = yard.GetGeometryType()
>>> driver = ogr.GetDriverByName('json')
>>> ds = driver.CreateDataSource('myyard')

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ds = driver.CreateDataSource('myyard')
AttributeError: 'NoneType' object has no attribute 'CreateDataSource'
>>> ds = driver.CreateDataSource ('myyard')

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ds = driver.CreateDataSource ('myyard')
AttributeError: 'NoneType' object has no attribute 'CreateDataSource'
>>> driver = ogr.GetDriverByName('GeoJSON')
>>> ds = driver.CreateDataSource('myyard')
>>> ds.CreateLayer('yardlyr', spref, geom)
<osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fba080ba930> >
>>> ds.GetLayer
<bound method DataSource.GetLayer of <osgeo.ogr.DataSource; proxy of <Swig Object of type 'OGRDataSourceShadow *' at 0x7fba080ba9c0> >>
>>> ds.GetLayer(0)
<osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fba080baae0> >
>>> yardlyr = ds.GetLayer(0)
>>> print (yardlyr.GetName())
yardlyr
>>> yardlyr.CreateFeature(yard)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    yardlyr.CreateFeature(yard)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: in method 'Layer_CreateFeature', argument 2 of type 'OGRFeatureShadow *'
>>> yardlyr.CreateFeature(yard)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    yardlyr.CreateFeature(yard)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: in method 'Layer_CreateFeature', argument 2 of type 'OGRFeatureShadow *'
>>> ds = driver.CreateDataSource('myyard.json')
>>> ds.CreateLayer('yardlyr', spref, geom)
<osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fba080bab10> >
>>> yardlyr = ds.GetLayer(0)
>>> print (yardlyr.GetName())
yardlyr
>>> yardlyr.CreateFeature(yard)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    yardlyr.CreateFeature(yard)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: in method 'Layer_CreateFeature', argument 2 of type 'OGRFeatureShadow *'
>>> lyrdfn = yardlyr.GetLayerDefn()
>>> yardfeat=ogr.FeatureDefn
>>> yardlyr.CreateField('objects', geom)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    yardlyr.CreateField('objects', geom)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1821, in CreateField
    return _ogr.Layer_CreateField(self, *args, **kwargs)
TypeError: in method 'Layer_CreateField', argument 2 of type 'OGRFieldDefnShadow *'
>>> yardlyr.CreateField('objects', ogr.wkbPolygon)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    yardlyr.CreateField('objects', ogr.wkbPolygon)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1821, in CreateField
    return _ogr.Layer_CreateField(self, *args, **kwargs)
TypeError: in method 'Layer_CreateField', argument 2 of type 'OGRFieldDefnShadow *'
>>> yardlyr.CreateField('objects')

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    yardlyr.CreateField('objects')
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1821, in CreateField
    return _ogr.Layer_CreateField(self, *args, **kwargs)
TypeError: in method 'Layer_CreateField', argument 2 of type 'OGRFieldDefnShadow *'
>>> yardlyr.CreateField('objects', lyrdfn)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    yardlyr.CreateField('objects', lyrdfn)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1821, in CreateField
    return _ogr.Layer_CreateField(self, *args, **kwargs)
TypeError: in method 'Layer_CreateField', argument 2 of type 'OGRFieldDefnShadow *'
>>> yardfeat=ogr.FeatureDefn()
>>> 
>>> yardlyr.CreateField(ogr.FieldDefn('objects', ogr.OFTInteger))
0
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path1 = 'ROU_adm.gpkg'
>>> ds1 = ogr.Open(path1, 1)
>>> country_lyr=ds1.GetLayer(0)
>>> print (country_lyr.GetName)
<bound method Layer.GetName of <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fcd89b1e600> >>
>>> print (country_lyr.GetName())
ROU_adm0
>>> path2 = '//home//roxana//Desktop//data//Romania1.shp
SyntaxError: EOL while scanning string literal
>>> path2 = '//home//roxana//Desktop//data//Romania1.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> filtered_lyr = ds2.GetLayer(0)
>>> print (filtered_lyr.GetName())
Romania1
>>> rou_feat = country_lyr.GetFeature(1)
>>> rou_geom = rou_feat.geometry().Clone()
>>> rou_geom.TransformTo(filtered_lyr.GetSpatialRef())
0
>>> for i in range (filtered_lyr.GetFeatureCount()) :
	features = filtered_lyr.GetFeature(i)
	filtered_geom = features.geometry()
	intersection = filtered_geom.Intersection(rou_geom)
	filtered_lyr.SetSpatialFilter(intersection)
	newlayer = ds2.CopyLayer(filtered_lyr, 'Romania3')

	


>>> for i in range (filtered_lyr.GetFeatureCount()) :
	features = filtered_lyr.GetFeature(i)
	filtered_geom = features.geometry()
	intersection = filtered_geom.Intersection(rou_geom)
	filtered_lyr.SetSpatialFilter(intersection)
	newlayer = ds2.CopyLayer(filtered_lyr, 'Romania4')

	
>>> del ds2
>>> 
=============================== RESTART: Shell ===============================
>>> from osgeo import ogr
>>> path1 = 'ROU_adm.gpkg'
>>> ds1 = ogr.Open(path1, 1)
>>> country_lyr=ds1.GetLayer(0)
>>> print (country_lyr.GetName())
ROU_adm0
>>> path2 = '//home//roxana//Desktop//data//Romania1.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> filtered_lyr = ds2.GetLayer(0)
>>> print (filtered_lyr.GetName())
Romania1
>>> rou_feat = country_lyr.GetFeature(1)
>>> rou_geom = rou_feat.geometry().Clone()
>>> rou_geom.TransformTo(filtered_lyr.GetSpatialRef())
0
>>> intersection = filtered_lyr.Intersection(rou_geom)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    intersection = filtered_lyr.Intersection(rou_geom)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 2179, in Intersection
    return _ogr.Layer_Intersection(self, *args, **kwargs)
TypeError: Required argument 'result_layer' (pos 3) not found
>>> intersection = filtered_lyr.Intersection(rou_geom, 'Romaniaf')

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    intersection = filtered_lyr.Intersection(rou_geom, 'Romaniaf')
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 2179, in Intersection
    return _ogr.Layer_Intersection(self, *args, **kwargs)
TypeError: in method 'Layer_Intersection', argument 2 of type 'OGRLayerShadow *'
>>> intersection = filtered_lyr.Intersection(country_lyr, 'Romaniaf')

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    intersection = filtered_lyr.Intersection(country_lyr, 'Romaniaf')
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 2179, in Intersection
    return _ogr.Layer_Intersection(self, *args, **kwargs)
TypeError: in method 'Layer_Intersection', argument 3 of type 'OGRLayerShadow *'
>>> for feat in filtered_lyr :
	geom = feat.GetGeometryRef()
	filtered_geom =
	
SyntaxError: invalid syntax
>>> filtered_lyr.GetGeomType()
3
>>> union_filtered = ogr.Geometry(3)
>>> for feat in filtered_lyr :
	geom = feat.GetGeometryRef()
	union_filtered = union_filtered.Union(geom)

	

>>> intersection = union_filtered.Intersection(rou_geom)
>>> intersection.GetArea()
44735706152.163994
>>> driver = ogr.GetDriverByName('ESRI Shapefile')
>>> destshp= driver.CreateDataSource('Intersection.shp')
>>> destlayer=destshp.CreateLayer('myintersection', geom_type=ogr.wkbMultipolygon)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    destlayer=destshp.CreateLayer('myintersection', geom_type=ogr.wkbMultipolygon)
AttributeError: 'module' object has no attribute 'wkbMultipolygon'
>>> destlayer=destshp.CreateLayer('myintersection', geom_type=ogr.wkbMultiPolygon)
>>> destlayer.CreateFeature(intersection)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    destlayer.CreateFeature(intersection)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1522, in CreateFeature
    return _ogr.Layer_CreateFeature(self, *args)
TypeError: in method 'Layer_CreateFeature', argument 2 of type 'OGRFeatureShadow *'
>>> intersection_geom = intersection.geometry().Clone()

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    intersection_geom = intersection.geometry().Clone()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 4169, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Geometry, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> print intersection.GetGeometryName()
MULTIPOLYGON
>>> intersection_feat = ogr.Geometry(3)
>>> intersection_feat = ogr.Feature(filtered_lyr.GetLayerDefn())
>>> intersection_feat = SetGeometry(intersection)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    intersection_feat = SetGeometry(intersection)
NameError: name 'SetGeometry' is not defined
>>> intersection_feat.SetGeometry(intersection)
0
>>> del ds

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    del ds
NameError: name 'ds' is not defined
>>> del destshp
>>> driver.DeleteDataSource('Intersection.shp')
0
>>> driver.CreateDataSource('Intersection.shp')
<osgeo.ogr.DataSource; proxy of <Swig Object of type 'OGRDataSourceShadow *' at 0x7f43a4094c00> >
>>> driver.DeleteDataSource('Intersection.shp')
6
>>> driver.DeleteDataSource('Intersection.shp')
6
>>> destshp= driver.CreateDataSource('Intersection.shp')
>>> destlyr = destshp.CreateLayer('myintersection', ogr.wkbMultiPolygon)

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    destlyr = destshp.CreateLayer('myintersection', ogr.wkbMultiPolygon)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 786, in CreateLayer
    return _ogr.DataSource_CreateLayer(self, *args, **kwargs)
TypeError: in method 'DataSource_CreateLayer', argument 3 of type 'OSRSpatialReferenceShadow *'
>>> destlyr=destshp.CreateLayer('myintersection', geom_type=ogr.wkbMultiPolygon)
>>> destlyr_defn = destlyr.GetLayerDefn()
>>> myfeat = ogr.Feature(destlyr_defn)
>>> myfeat.SetGeometry(intersection)
0
>>> destlyr.CreateFeature(myfeat)
0
>>> del destshp
>>> intersection_geom = intersection.Clone()
>>> myfeat.SetGeometry(intersection_geom)
0
>>> destlyr.CreateFeature(myfeat)
0
>>> del destshp

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    del destshp
NameError: name 'destshp' is not defined
>>> driver.DeleteDataSource('Intersection.shp')
0
>>> destshp= driver.CreateDataSource('Intersection.shp')
>>> destlyr=destshp.CreateLayer('myintersection', geom_type=ogr.wkbMultiPolygon)
>>> destlyr_defn = destlyr.GetLayerDefn()
>>> myfeat = ogr.Feature(destlyr_defn)
>>> myfeat.SetGeometry(intersection_geom)
0
>>> destlyr.CreateFeature(myfeat)
0
>>> del destshp
>>> destlyr.GetSpatialRef()

=============================== RESTART: Shell ===============================
>>> 

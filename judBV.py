Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path = '//home//roxana//working_through_GeoprocessingWithPython//ROU_adm.gpkg'
>>> ds = ogr.Open(path, 1)
>>> if ds is None :
	print ('not open')
else :
	print ('ds open')

	
ds open
>>> lyr0 = ds.GetLayer(0)
>>> lyr0.GetName()
'ROU_adm0'
>>> lyr1 = ds.GetLayer(1)
>>> lyr1.GetName()
'ROU_adm1'
>>> lyr2=ds.GetLayer(2)
>>> lyr2.GetName()
'ROU_adm2'
>>> BVfeat = lyr1.GetFeature(8)
>>> BVgeom = BVfeat.geometry().Clone()
>>> lyr2.SetSpatialFilter(BVgeom)
>>> out_lyr= ds.CreateLayer(lyr2, 'judBV')

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    out_lyr= ds.CreateLayer(lyr2, 'judBV')
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 786, in CreateLayer
    return _ogr.DataSource_CreateLayer(self, *args, **kwargs)
TypeError: in method 'DataSource_CreateLayer', argument 2 of type 'char const *'
>>> out_lyr = ds.CreateLayer(lyr2, 'judbv')

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    out_lyr = ds.CreateLayer(lyr2, 'judbv')
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 786, in CreateLayer
    return _ogr.DataSource_CreateLayer(self, *args, **kwargs)
TypeError: in method 'DataSource_CreateLayer', argument 2 of type 'char const *'
>>> out_lyr = ds.CopyLayer(ly2, 'judBV')

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    out_lyr = ds.CopyLayer(ly2, 'judBV')
NameError: name 'ly2' is not defined
>>> out_lyr = ds.CopyLayer(lyr2, 'judBV')
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> ds = 'myaerial.tif'
>>> fn = 'myaerial.tif'
>>> ds= gdal.Open(fn, gdal.GA_Update)
>>> sr = osr.SpatialReference()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sr = osr.SpatialReference()
NameError: name 'osr' is not defined
>>> import osr
>>> sr = osr.SpatialReference()
>>> sr.SetWellKnownGeogCS('WGS84')
0
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, 302),
	 gdal.GCP(535.1, -283.1, 0, 536, 286),
	 gdal.GCP(518.7, -248.6, 0, 519, 250),
	 619, -215.3, 0, 621, -218)]
>>> ds.SetProjection(sr.ExportToWkt)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ds.SetProjection(sr.ExportToWkt)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 824, in SetProjection
    return _gdal.Dataset_SetProjection(self, *args)
TypeError: in method 'Dataset_SetProjection', argument 2 of type 'char const *'
>>> ds.SetProjection(sr.ExportToWkt())
0
>>> ds.SetGeoTransform(gdal.GCPsToGeoTransform(gcps))

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ds.SetGeoTransform(gdal.GCPsToGeoTransform(gcps))
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 712, in GCPsToGeoTransform
    return _gdal.GCPsToGeoTransform(*args)
SystemError: error return without exception set
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, 302),
	 gdal.GCP(535.1, -283.1, 0, 536, 286),
	 gdal.GCP(518.7, -248.6, 0, 519, 250),
	 619, -215.3, 0, 621, 218)]
>>> ds.SetGeoTransform(gdal.GCPsToGeoTransform(gcps))

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ds.SetGeoTransform(gdal.GCPsToGeoTransform(gcps))
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 712, in GCPsToGeoTransform
    return _gdal.GCPsToGeoTransform(*args)
SystemError: error return without exception set
>>> 

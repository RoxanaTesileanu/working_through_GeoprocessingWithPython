Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal, osr
>>> import shutil
>>> ds = 'myaerial.tif'
>>> fn = 'myaeria.tif'
>>> ds = gdal.Open(fn, gdal.GA_Update)
>>> sr = osr.SpatialReference()
>>> sr.SetWellKnownGeogCS('WGS84')
0
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, 302),
	 gdal.GCP(535.1, -283.1, 0, 536, 286),
	 gdal.GCP(518.7, -248.6, 0, 519, 250),
	 619, -215.3, 0, 621, -218)]
>>> ds.SetGCPs(gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ds.SetGCPs(gcps, sr.ExportToWkt())
AttributeError: 'NoneType' object has no attribute 'SetGCPs'
>>> ds.SetGCPs(gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ds.SetGCPs(gcps, sr.ExportToWkt())
AttributeError: 'NoneType' object has no attribute 'SetGCPs'
>>> ds.SetGCPs(gcps)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ds.SetGCPs(gcps)
AttributeError: 'NoneType' object has no attribute 'SetGCPs'
>>> ds.SetGCPs(gcps, sr)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ds.SetGCPs(gcps, sr)
AttributeError: 'NoneType' object has no attribute 'SetGCPs'
>>> if ds is None : print 'ds is none'

ds is none
>>> ds = gdal.Open(fn, gdal.GA_Update)
>>> if ds is None : print 'ds is none'

ds is none
>>> ds = gdal.Open(fn, 1)
>>> 
>>> if ds is None : print 'ds is none'

ds is none
>>> fn = 'myaerial.tif'
>>> ds = gdal.Open(fn, gdal.GA_Update)
>>> if ds is None : print 'ds is none'
else : print 'ds open'

ds open
>>> ds.SetGCPs(gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ds.SetGCPs(gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> ds.SetGCPs(gcps)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ds.SetGCPs(gcps)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
TypeError: Dataset_SetGCPs() takes exactly 3 arguments (2 given)
>>> ds.SetGCPs(gcps, sr)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    ds.SetGCPs(gcps, sr)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> ds.SetGCPs(gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    ds.SetGCPs(gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> ds.SetGCPs(ds, gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ds.SetGCPs(ds, gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
TypeError: Dataset_SetGCPs() takes exactly 3 arguments (4 given)
>>> proj = sr.ExportToWkt()
>>> ds.SetGCPs(gcps, proj)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    ds.SetGCPs(gcps, proj)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> proj
'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9108"]],AUTHORITY["EPSG","4326"]]'
>>> mygcps = int(gcps)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    mygcps = int(gcps)
TypeError: int() argument must be a string or a number, not 'list'
>>> mygcps = int(list(gcps))

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    mygcps = int(list(gcps))
TypeError: int() argument must be a string or a number, not 'list'
>>> 
ds.SetGCPs(ds, gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    ds.SetGCPs(ds, gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
TypeError: Dataset_SetGCPs() takes exactly 3 arguments (4 given)
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, -302),
	 gdal.GCP(535.1, -283.1, 0, 536, -286),
	 gdal.GCP(518.7, -248.6, 0, 519, -250),
	 619, -215.3, 0, 621, -218)]
>>> ds.SetGCPs(ds, gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ds.SetGCPs(ds, gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
TypeError: Dataset_SetGCPs() takes exactly 3 arguments (4 given)
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, 302),
	 gdal.GCP(535.1, -283.1, 0, 536, 286),
	 gdal.GCP(518.7, -248.6, 0, 519, 250),
	 619, -215.3, 0, 621, 218)]
>>> 
>>> ds.SetGCPs(gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ds.SetGCPs(gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, -302),
	 gdal.GCP(535.1, -283.1, 0, 536, -286),
	 gdal.GCP(518.7, -248.6, 0, 519, -250),
	 619, -215.3, 0, 621, -218)]
>>> ds.SetGCPs(gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ds.SetGCPs(gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> print gcps
[(<osgeo.gdal.GCP; proxy of <Swig Object of type 'GDAL_GCP *' at 0x7f35a40d8de0> >, <osgeo.gdal.GCP; proxy of <Swig Object of type 'GDAL_GCP *' at 0x7f35a40e9de0> >, <osgeo.gdal.GCP; proxy of <Swig Object of type 'GDAL_GCP *' at 0x7f35a40e9e70> >, 619, -215.3, 0, 621, -218)]
>>> -gcp 232.755 302.041 232.61 -301.186 -gcp 536.327 286.224 535.365 -284.79 -gcp 519.49 250 518.97 -250.868 -gcp 621.02 217.857 619.322 -216.946ds.SetGCPs(gcps, sr.ExportToWkt())
SyntaxError: invalid syntax
>>> ds.SetGCPs((gcp 232.755 302.041 232.61 -301.186 -gcp 536.327 286.224 535.365 -284.79 -gcp 519.49 250 518.97 -250.868 -gcp 621.02 217.857 619.322 -216.946), sr.ExportToWkt())
SyntaxError: invalid syntax
>>> ds.SetGCPs((-gcp 232.755 302.041 232.61 -301.186 -gcp 536.327 286.224 535.365 -284.79 -gcp 519.49 250 518.97 -250.868 -gcp 621.02 217.857 619.322 -216.946), sr.ExportToWkt())
SyntaxError: invalid syntax
>>> ds.SetGCPs((-gcp 232.755 302.041 232.61 -301.186 -gcp 536.327 286.224 535.365 -284.79 -gcp 519.49 250 518.97 -250.868 -gcp 621.02 217.857 619.322 -216.946), sr.ExportToWkt())
SyntaxError: invalid syntax
>>> ds.SetGCPs(int(-gcp 232.755 302.041 232.61 -301.186 -gcp 536.327 286.224 535.365 -284.79 -gcp 519.49 250 518.97 -250.868 -gcp 621.02 217.857 619.322 -216.946), sr.ExportToWkt())
SyntaxError: invalid syntax
>>> ds.SetGCPs(4, gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ds.SetGCPs(4, gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
TypeError: Dataset_SetGCPs() takes exactly 3 arguments (4 given)
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, 302),
	 gdal.GCP(535.1, -283.1, 0, 536, 286),
	 gdal.GCP(518.7, -248.6, 0, 519, 250),
	 619, -215.3, 0, 621, 218)]
>>> ds.SetGCPs(4, gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    ds.SetGCPs(4, gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
TypeError: Dataset_SetGCPs() takes exactly 3 arguments (4 given)
>>> ds.SetGCPs( gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ds.SetGCPs( gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> ds.SetGCPs( gcps, sr.ExportToWkt())

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ds.SetGCPs( gcps, sr.ExportToWkt())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 859, in SetGCPs
    return _gdal.Dataset_SetGCPs(self, *args)
SystemError: error return without exception set
>>> gdal.GCP(-gcp 232.755 302.041 232.61 -301.186 -gcp 536.327 286.224 535.365 -284.79 -gcp 519.49 250 518.97 -250.868 -gcp 621.02 217.857 619.322 -216.946
	 
SyntaxError: invalid syntax
>>> gdal.GCP(232.755 302.041 232.61 -301.186)
SyntaxError: invalid syntax
>>> gcps = [(gdal.GCP(232.6, -298.4,0, 233, 302),
	 gdal.GCP(535.1, -283.1, 0, 536, 286),
	 gdal.GCP(518.7, -248.6, 0, 519, 250),
	 619, -215.3, 0, 621, 218)]
>>> 

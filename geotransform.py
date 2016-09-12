Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> mytif = 'DEM_Sacele/ASTGTM2_N45E025_dem.tif'
>>> ds = gdal.Open(mytif)
>>> gt = ds.GetGeoTransform()
>>> inv_gt = gdal.InvGeoTransform(gt)
>>> if inv_gt is None : print 'inv gt is none'
else : print 'inv gt computed'

inv gt computed
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 45.5, 25.5)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 45.5, 25.5)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 453000, 253000)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 453000, 253000)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 453000, 253000)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 453000, 253000)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> ds.GetGCPProjection()
''
>>> ds.GetProjection()
'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]]'
>>> ds.offsets = gdal.ApplyGeoTransform(inv_gt, 453000.00, 253000.00)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ds.offsets = gdal.ApplyGeoTransform(inv_gt, 453000.00, 253000.00)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 453000.00, 253000.00)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 453000.00, 253000.00)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 455000, 255000)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 455000, 255000)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(453000.00, 253000.00)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(453000.00, 253000.00)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: ApplyGeoTransform() takes exactly 3 arguments (2 given)
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 453000.00, 253000.00)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 453000.00, 253000.00)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 25.5, 45.5)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 25.5, 45.5)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 253000.00, 453000.00)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 253000.00, 453000.00)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(453000, 253000)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(453000, 253000)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: ApplyGeoTransform() takes exactly 3 arguments (2 given)
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 253000, 453000)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 253000, 453000)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 255000, 455000)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 255000, 455000)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: sequence must have length ##size
>>> 

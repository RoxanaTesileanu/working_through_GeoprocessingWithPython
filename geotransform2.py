Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> print gdal.Versioninfo()

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print gdal.Versioninfo()
AttributeError: 'module' object has no attribute 'Versioninfo'
>>> print gdal.Versioninfo

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print gdal.Versioninfo
AttributeError: 'module' object has no attribute 'Versioninfo'
>>> print gdal.Versioninfo(1)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print gdal.Versioninfo(1)
AttributeError: 'module' object has no attribute 'Versioninfo'
>>> print gdal.Versioninfo(0)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print gdal.Versioninfo(0)
AttributeError: 'module' object has no attribute 'Versioninfo'
>>> if gdal.VersionInfo() [0] == '1'
SyntaxError: invalid syntax
>>> if gdal.VersionInfo() [0] == '1' :
	print 'version 1'

	
version 1
>>> mytif = 'DEM_Sacele/ASTGTM2_N45E025_dem.tif'
>>> ds = gdal.Open(mytif)
>>> gt = ds.GetGeoTransform()
>>> success, inv_gt=gdal.InvGeoTransform(gt)
>>> print success
1
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 25,5, 45.5)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    offsets = gdal.ApplyGeoTransform(inv_gt, 25,5, 45.5)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: ApplyGeoTransform() takes exactly 3 arguments (4 given)
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 25.5, 45.5)
>>> print offsets
[1800.5, 1800.5]
>>> realworld = gdal.ApplyGeoTransform(gt, 300, 300)
>>> print realworld
[25.083194444444445, 45.916805555555555]
>>> xoff, yoff = map(int, offsets)
>>> print xoff, yoff
1800 1800
>>> band = ds.GetRasterBand(1)
>>> value = band.ReadAsArray(xoff, yoff, 1, 1) [0,0]
>>> print value
1030
>>> 

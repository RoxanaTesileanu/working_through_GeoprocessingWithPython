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
>>> import numpy as np
>>> # for more than one values :
>>> 
>>> data = band.ReadAsArray()
>>> x,y = map(int, gdal.ApplyGeoTransform(inv_gt, 25.5, 45.5)
	  )
>>> print x,y
1800 1800
>>> value = data[y,x]
>>> print value
1030
>>> # I want to extract a subset with the upper left coordinates 45.5, 25.5 and lower-right coordinates 45.00, 25.00.
>>> 
>>> ulx, uly = 45.5, 25.5
>>> lrx, lry = 45.00, 25.00
>>> offsets_ul = gdal.ApplyGeoTransform(inv_gt, ulx, uly)
>>> offsets_lr = gdal.ApplyGeoTransform(inv_gt, lrx, lry)
>>> print offsets_ul, offsets_lr
[73800.5, 73800.5] [72000.5, 75600.5]
>>> off_ulx, off_uly = map(int, offsets_ul)
>>> off_lrx, off_lry = map(int, offsets_lr)
>>> print off_ulx, off_uly, off_lrx, off_lry)
SyntaxError: invalid syntax
>>> print off_ulx, off_uly, off_lrx, off_lry
73800 73800 72000 75600
>>> # ok I've discovered I acutally have a upper right point and a lower left point.
>>> ulx, uly = 25.5, 45.5
>>> lrx, lry = 25.00, 45.00
>>> offsets_ul = gdal.ApplyGeoTransform(inv_gt, ulx, uly)
>>> offsets_lr = gdal.ApplyGeoTransform(inv_gt, lrx, lry)
>>> print offsets_ul, offsets_lr
[1800.5, 1800.5] [0.5, 3600.5]
>>> off_ulx, off_uly = map(int, offsets_ul)
>>> off_lrx, off_lry = map(int, offsets_lr)
>>> print off_ulx, off_uly, off_lrx, off_lry
1800 1800 0 3600
>>> # I've recomputed x and y  coord. of offsets because I've mixed x with y.
>>> # now I can find out the no. of rows and of columns to extract to get the subset I wanted:
>>> rows = off_uly - off_lry
>>> print rows
-1800
>>> rows = off_lry - off_uly
>>> print rows
1800
>>> off_lrx - off_ulx
-1800
>>> columns = off_lrx - off_ulx
>>> print columns
-1800
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> columns = off_ulx - off_lrx
>>> print columns
1800
>>> new_ds = gtiff_driver('mysubset.tif', columns, rows, 3)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    new_ds = gtiff_driver('mysubset.tif', columns, rows, 3)
TypeError: 'Driver' object is not callable
>>> new_ds = gtiff_driver('mysubset.tif', columns, rows)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    new_ds = gtiff_driver('mysubset.tif', columns, rows)
TypeError: 'Driver' object is not callable
>>> new_ds = gtiff_driver('mysubset.tif', columns, rows, bands=1)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    new_ds = gtiff_driver('mysubset.tif', columns, rows, bands=1)
TypeError: 'Driver' object is not callable
>>> new_ds = gtiff_driver.Create('mysubset.tif', 1800, 1800, bands=1)
>>> 

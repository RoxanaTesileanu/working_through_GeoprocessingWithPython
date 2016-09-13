Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> 
>>> if gdal.VersionInfo() [0] == '1'
SyntaxError: invalid syntax
>>> if gdal.VersionInfo() [0] == '1' :
	print 'version 1'

	
version 1
>>> mytif = 'DEM_Sacele/ASTGTM2_N45E025_dem.tif'
>>> ds = gdal.Open(mytif)
>>> gt = ds.GetGeoTransform()
>>> 
>>> success, inv_gt = gdal.InvGeoTransform(gt)
>>> print success
1
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
>>> value = band.ReadAsArray(xoff, yoff, 1,1) [0,0]
>>> print value
1030
>>> import numpy as np
>>> data = band.ReadAsArray()
>>> x,y = map(int, gdal.ApplyGeoTransform(inv_gt, 25.5, 45.5)
	  )
>>> print x, y
1800 1800
>>> value = data [y,x]
>>> print value
1030
>>> # for my two points: upper right 25.5, 45.5 and lower left 25.0, 45.0:
>>> # extract the subset
>>> 
>>> urx = 25.5
>>> ury = 45.5
>>> llx = 25.0
>>> lly = 45.0
>>> offsets_ur= gdal.ApplyGeoTransform(inv_gt, urx, ury)
>>> offsets_ll= gdal.ApplyGeoTransform(inv_gt, llx, lly)
>>> print offsets_ur, offsets_ll
[1800.5, 1800.5] [0.5, 3600.5]
>>> off_urx, off_ury = map(int, offsets_ur)
>>> off_llx, off_lly = map(int, offsets_ll)
>>> print off_urx, off_ury, off_llx, off_lly
1800 1800 0 3600
>>> # find out the no. of rows and columns:
>>> rows = ury-lly
>>> print rows
0.5
>>> # no, I need the diff in offsets, so:
>>> rows = off_ury - off_lly
>>> print rows
-1800
>>> columns = off_llx - off_urx
>>> print columns
-1800
>>> # now create a ds to put in the subset of 1800 rows and 1800 columns
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> new_ds = gtiff_driver.Create('mysubset1.tif', 1800, 1800, bands=1)
>>> new_ds.SetProjection(ds.GetProjection())
0
>>> # now to set the gt of the new ds I need the upper left point. I know from my sketch it must be 25.0, 45.5
>>> new_gt = list(gt)
>>> print new_gt
[24.999861111111112, 0.0002777777777777778, 0.0, 46.00013888888889, 0.0, -0.0002777777777777778]
>>> # now, I have to change the position 0 and 3 in the list:
>>> new_gt [0] = 25.0
>>> new_gt [3] = 45.5
>>> print new_gt
[25.0, 0.0002777777777777778, 0.0, 45.5, 0.0, -0.0002777777777777778]
>>> new_ds.SetGeoTransform(new_gt)
0
>>> # ok, I can't use the original upper left coordinates that I know because they are not the coordinates of the upper left pixel corner! So, I still need to work at the new_gt !!!
>>> # I need the offsets first:
>>> offsets_ulx, offsets_uly = gdal.ApplyGeoTransform(inv_gt, 25, 45.5)
>>> off_ulx, off_uly = map(int, offsets_ulx, offsets_uly)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    off_ulx, off_uly = map(int, offsets_ulx, offsets_uly)
TypeError: argument 2 to map() must support iteration
>>> off_ulx = map(int, offsets_x)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    off_ulx = map(int, offsets_x)
NameError: name 'offsets_x' is not defined
>>> off_ulx = map(int, offsets_ulx)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    off_ulx = map(int, offsets_ulx)
TypeError: argument 2 to map() must support iteration
>>> offsets = gdal.ApplyGeoTransform(inv_gt, 25, 45.5)
>>> xoff, yoff = map(int, offsets)
>>> print xoff, yoff
0 1800
>>> subset_ulx = gdal.ApplyGeoTransform(gt, xoff)

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    subset_ulx = gdal.ApplyGeoTransform(gt, xoff)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1712, in ApplyGeoTransform
    return _gdal.ApplyGeoTransform(*args)
TypeError: ApplyGeoTransform() takes exactly 3 arguments (2 given)
>>> subset_ulx, subset_uly = gdal.ApplyGeoTransform(gt, xoff, yoff)
>>> print subset_ulx, subset_uly
24.9998611111 45.5001388889
>>> # ok, now I can alter the new_gt with the upper left coord. of the pixel corner:
>>> new_gt [0] = subset_ulx
>>> new_gt [3] = subset_uly
>>> print new_gt
[24.999861111111112, 0.0002777777777777778, 0.0, 45.50013888888889, 0.0, -0.0002777777777777778]
>>> new_ds.SetGeoTransform(new_gt)
0
>>> new_band = new_ds.GetRasterBand(1)
>>> new_data = band.ReadAsArray(xoff, yoff, 1800, 1800)
>>> new_band.WriteArray(new_data)
0
>>> del new_ds
>>> 

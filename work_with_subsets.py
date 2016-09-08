Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fn = 'blue.tif'
>>> from osgeo import gdal
>>> ds = gdal.Open(fn)
>>> ds.RasterXSize
1181
>>> ds.RasterYSize
626
>>> ds.Raster

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ds.Raster
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 785, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> 
>>> ds.RasterCount
1
>>> # so my ds has 1181 columns, 626 rows and 1 raster band
>>> 
>>> band = ds.GetRasterBand(1)
>>> mydata= band.ReadAsArray(8, 2, 4, 11)
>>> import numpy as np
>>> data = np.empty(4, 11)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data = np.empty(4, 11)
TypeError: data type not understood
>>> data = np.empty((4, 11), dtype=foat)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data = np.empty((4, 11), dtype=foat)
NameError: name 'foat' is not defined
>>> data = np.empty((4, 11), dtype=float)
>>> band.ReadAsArray(8,2,4,11, buf_obj=data)
array([[ 113.,  113.,  113.,  109.,  109.,  109.,  119.,  119.,  140.,
         140.,  140.],
       [   0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    4.,
           4.,    4.],
       [   0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
           0.,    0.],
       [ 127.,  127.,  127.,  112.,  112.,  112.,   98.,   98.,   95.,
          95.,   95.]])
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> new_ds= gtiff_driver.Create('blue2.tif', band.XSize, band.YSize, bands=1)
>>> blue_data=band.ReadAsArray()
>>> new_ds.SetProjection(ds.GetProjection())
0
>>> new_ds.SetGeoTransform(ds.GetGeoTransform())
0
>>> new_blue_band= new_ds.GetRasterBand(1)
>>> new_blue_band.WriteArray(blue_data)
0
>>> # so indeed without the SetMetadata() the tif remains blank.
>>> gtiff_driver.Delete('blue2.tif')
0
>>> new_blue_band.WriteArray(data, 1400, 1600)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    new_blue_band.WriteArray(data, 1400, 1600)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> new_ds= gtiff_driver.Create('blue2.tif', band.XSize, band.YSize, bands=1)
>>> new_ds.SetProjection(ds.GetProjection())
0
>>> new_ds.SetGeoTransform(ds.GetGeoTransform())
0
>>> new_blue_band= new_ds.GetRasterBand(1)
>>> new_blue_band.WriteArray(data, 1400, 1600)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    new_blue_band.WriteArray(data, 1400, 1600)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> new_blue_band.WriteArray(data, 8, 2)
0
>>> 
>>> new_ds.FlushCache()
>>> new_ds.RasterXSize
1181
>>> new_ds= gtiff_driver.Create('blue3.tif', 4, 11, bands=1)
>>> new_ds.SetProjection(ds.GetProjection())
0
>>> new_ds.SetGeoTransform(ds.GetGeoTransform())
0
>>> new_blue_band= new_ds.GetRasterBand(1)
>>> new_blue_band.WriteArray(data, 1400, 1600)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    new_blue_band.WriteArray(data, 1400, 1600)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> gtiff_driver.Delete('blue2.tif')
0
>>> gtiff_driver.Delete('blue3.tif')
3
>>> new_ds.FlushCache()
>>> gtiff_driver.Delete('blue3.tif')
0
>>> new_ds= gtiff_driver.Create('blue3.tif', 4, 11, bands=1)
>>> gtiff_driver.Delete('blue3.tif')
3
>>> new_ds.FlushCache()
>>> gtiff_driver.Delete('blue3.tif')
0
>>> new_ds= gtiff_driver.Create('blue3.tif', 3, 10, bands=1)
>>> new_blue_band.WriteArray(data, 1400, 1600)

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    new_blue_band.WriteArray(data, 1400, 1600)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> new_blue_band.WriteArray(data)

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    new_blue_band.WriteArray(data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> new_blue_band.WriteArray(mydata)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    new_blue_band.WriteArray(mydata)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> new_ds.FlushCache()
>>> gtiff_driver.Delete('blue3.tif')
0
>>> new_ds= gtiff_driver.Create('blue3.tif', 4, 11, bands=1)
>>> new_blue_band= new_ds.GetRasterBand(1)
>>> new_blue_band.WriteArray(mydata)
0
>>> 
>>> new_ds.FlushCache()
>>> new_ds.RasterXSize
4
>>> new_ds.RasterYSize
11
>>> new_ds.SetProjection(ds.GetProjection())
0
>>> new_ds.SetGeoTransform(ds.SetGeoTransform())

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    new_ds.SetGeoTransform(ds.SetGeoTransform())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 834, in SetGeoTransform
    return _gdal.Dataset_SetGeoTransform(self, *args)
TypeError: Dataset_SetGeoTransform() takes exactly 2 arguments (1 given)
>>> new_ds.SetGeoTransform(ds.GetGeoTransform())
0
>>> new_ds.FlushCache()
>>> # ok, so I've saved the small subset into a newly created ds (blue3.tif)
>>> 
new_ds2= gtiff_driver.Create('blue2.tif', band.XSize, band.YSize , bands=1)
>>> new_blue_band2= new_ds2.GetRasterBand(1)
>>> new_blue_band.WriteArray(blue_data)

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    new_blue_band.WriteArray(blue_data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1360, in WriteArray
    return gdalnumeric.BandWriteArray( self, array, xoff, yoff )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 321, in BandWriteArray
    raise ValueError("array larger than output file, or offset off edge")
ValueError: array larger than output file, or offset off edge
>>> new_blue_band2.WriteArray(blue_data)
0
>>> new_ds2.FlushCache()
>>> 
gtiff_driver.Delete('blue2.tif')
0
>>> new_ds2= gtiff_driver.Create('blue2.tif', band.XSize, band.YSize , bands=1)
>>> new_blue_band2= new_ds2.GetRasterBand(1)
>>> blue_data = band.ReadAsArray(0,0, 1181, 626)
>>> new_blue_band2.WriteArray(blue_data)
0
>>> new_ds2.FlushCache()
>>> new_ds2.SetGeoTransform(ds.GetGeoTransform())
0
>>> 
>>> new_ds2.SetProjection(ds.GetProjection())
0
>>> new_ds2.FlushCache()
>>> new_ds4= gtiff_driver.Create('blue4.tif', band.XSize, band.YSize , bands=1)
>>> new_blue_band4=new_ds4.GetRasterBand(1)
>>> blue_data = band.ReadAsArray()
>>> new_blue_band4.WriteArray(blue_data)
0
>>> new_ds4.FlushCache()
>>> new_ds4.SetGeoTransform(ds.GetGeoTransform())
0
>>> new_ds4.SetProjection(ds.GetProjection())
0
>>> new_ds4.FlushCache()
>>> # WriteArray on whole bands seems to work well now...So Chris's method works for my image too.
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> 
>>> old_tif = '_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif'
>>> old_ds= gdal.Open(old_tif)
>>> blue_band= old_ds.GetRasterBand(1)
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.Ysize, 1, blue_band.DataType)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.Ysize, 1, blue_band.DataType)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.Ysize, 1, blue_band.DataType)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.Ysize, 1, blue_band.DataType)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.Ysize,1, blue_band.DataType)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.Ysize,1, blue_band.DataType)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> new_ds = gtiff_driver.Create('blue.tif', blue_band.XSize, blue_band.YSize, bands=1)
>>> new_ds.SetProjection(old_ds.GetProjection())
0
>>> new_ds.SetGeoTransform(old_ds.GetGeoTransform)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    new_ds.SetGeoTransform(old_ds.GetGeoTransform)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 834, in SetGeoTransform
    return _gdal.Dataset_SetGeoTransform(self, *args)
TypeError: not a sequence
>>> new_ds.SetGeoTransform(old_ds.GetGeoTransform())
0
>>> blue_data = blue_band.ReadAsArray()
>>> if blue_data is None : print 'none'

>>> if blue_data is None : print 'none'
else : print 'not none'

not none
>>> new_band = new_ds.GetRasterBand()

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    new_band = new_ds.GetRasterBand()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 809, in GetRasterBand
    return _gdal.Dataset_GetRasterBand(self, *args)
TypeError: Dataset_GetRasterBand() takes exactly 2 arguments (1 given)
>>> new_band = new_ds.GetRasterBand(1)
>>> new_band.WriteArray(blue_data)
0
>>> new_ds.FlushCache()
>>> blue_data = blue_band.ReadBlock()

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    blue_data = blue_band.ReadBlock()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1332, in ReadBlock
    return _gdal.Band_ReadBlock(self, *args, **kwargs)
TypeError: Required argument 'xoff' (pos 2) not found
>>> blue_data = blue_band.ReadBlock(1)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    blue_data = blue_band.ReadBlock(1)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1332, in ReadBlock
    return _gdal.Band_ReadBlock(self, *args, **kwargs)
TypeError: Required argument 'yoff' (pos 3) not found
>>> blue_data = blue_band.ReadRaster()
>>> new_band.WriteRaster(blue_data)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    new_band.WriteRaster(blue_data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1227, in WriteRaster
    return _gdal.Band_WriteRaster(self, *args, **kwargs)
TypeError: Required argument 'yoff' (pos 3) not found
>>> new_band.SetMetadata(blue_data)
0
>>> new_ds.FlushCache()
>>> 

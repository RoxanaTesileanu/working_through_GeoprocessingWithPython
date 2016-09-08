Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> 
>>> old_tif = '_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif'
>>> old_ds= gdal.Open(old_tif)
>>> green_band = old_ds.GetRasterBand(2)
>>> if green_band is None : print 'green band is none'
else : print 'green band open'

green band open
>>> gtiff_driver= gdal.GetDriverByName('GTiff')
>>> green_ds = gtiff_driver.Create('green.tif', green_band.XSize, green_band.YSize, bands=1_
			       
SyntaxError: invalid syntax
>>> green_ds = gtiff_driver.Create('green.tif', green_band.XSize, green_band.YSize, bands=1)
>>> green_ds.SetProjection(old_ds.GetProjection())
0
>>> green_ds.SetGeoTransform(old_ds.GetGeoTransform())
0
>>> new_band = green_ds.GetRasterBand(2)
>>> new_band = green_ds.GetRasterBand(1)
>>> green_data = green_band.ReadRaster()
>>> new_band.SetMetadata(green_data)
0
>>> 
>>> green_ds.FlushCache()
>>> green_data_ar= green_band.ReadAsArray()
>>> new_band.WriteArray(green_data_ar)
0
>>> 
>>> green_data = green_band.ReadRaster()
>>> new_band.SetMetadata(green_data)
0
>>> green_ds.FlushCache()
>>> # so it seems that I have to go through two steps: get the data as array and then as metadata...
>>> # let's do it for red too:
>>> 
>>> red_band = old_ds.GetRasterBand(3)
>>> red_ds = gtiff_driver.Create('red.tif', red_band.XSize, red_band.Ysize, bands=1_
			     
SyntaxError: invalid syntax
>>> red_ds = gtiff_driver.Create('red.tif', red_band.XSize, red_band.Ysize, bands=1)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    red_ds = gtiff_driver.Create('red.tif', red_band.XSize, red_band.Ysize, bands=1)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> red_ds = gtiff_driver.Create('red.tif', red_band.XSize, red_band.Ysize, bands=1)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    red_ds = gtiff_driver.Create('red.tif', red_band.XSize, red_band.Ysize, bands=1)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> red_ds=gtiff_driver.Create('red.tif', red_band.XSize, red_band.YSize, bands=1)
>>> new_band_red= red_ds.GetRasterBand(1)
>>> red_data_ar = red_band.ReadAsArray()
>>> new_band_red.WriteArray(red_data_ar)
0
>>> red_ds.FlushCache()
>>> red_data_m = red_band.ReadRaster()
>>> new_band_red.SetMetadata(red_data_m)
0
>>> red_ds.FlushCache()
>>> ### ok! so it is really like that: you have to use ReadAsArray() and then ReadRaster() to obtain all the data necessary for the new band!
>>> 

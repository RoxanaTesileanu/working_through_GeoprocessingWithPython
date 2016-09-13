Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> mytif = 'blue3.tif'
>>> ds = gdal.Open(mytif)
>>> print ds.GetXSize

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print ds.GetXSize
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 785, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> print ds.RasterXSize
4
>>> print ds.RasterYSize
11
>>> band = ds.GetRasterBand(1)
>>> out_rows = band.YSize*2
>>> out_columns = band.XSize*2
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> out_ds = gtiff_driver.Create('resampledblue.tif', out_columns, out_rows, bands=1)
>>> out_ds.SetProjection(ds.GetProjection())
0
>>> geotransform = list(ds.GetGeoTransform())
>>> print geotransform
[2842586.9770944533, 30.01496347773325, 0.0, 5727820.656936204, 0.0, -30.014963477733918]
>>> geotransform [1] /=2
>>> geotransform [5] /=2
>>> out_ds.SetGeoTransform(geotransform)
0
>>> data = band.ReadAsArray(buf_xsize=out_columns, buf_ysize=out_rows)
>>> out_band = out_ds.GetRasterBand(1)
>>> out_band.WriteArray(data)
0
>>> 
>>> out_band.FlushCache()
>>> del out_ds
>>> 

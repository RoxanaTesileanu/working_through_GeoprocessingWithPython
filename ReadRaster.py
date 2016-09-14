Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> import numpy as np
>>> in_ds = gdal.Open('nat_colour.tif')
>>> out_rows = int(in_ds.RasterYSize/2)
>>> out_columns = int(in_ds.RasterXSize/2)
>>> num_bands=in_ds.RasterCount
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> out_ds = gtiff_driver.Create('nat_colour_resampled.tif')

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    out_ds = gtiff_driver.Create('nat_colour_resampled.tif')
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 453, in Create
    return _gdal.Driver_Create(self, *args, **kwargs)
TypeError: Required argument 'xsize' (pos 3) not found
>>> out_ds = gtiff_driver.Create('nat_colour_resampled.tif', out_columns, out_rows, num_bands)
>>> out_ds.SetProjection(in_ds.GetProjection())
0
>>> geotransform = list(in_ds.GetGeoTransform())
>>> geotransform
[2842586.9770944533, 30.01496347773325, 0.0, 5727820.656936204, 0.0, -30.014963477733918]
>>> geotransform [1] *=2
>>> geotransform [5] *=2
>>> out_ds.SetGeotransform(geotransform)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    out_ds.SetGeotransform(geotransform)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 785, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> out_ds.SetGeoTransform(geotransform)
0
>>> data = in_ds.ReadRaster(buf_xsize=out_columns, buf_ysize=out_rows)
>>> out_ds.WriteRaster(0, 0, out_columns, out_rows, data)
0
>>> out_ds.FlushCache()
>>> for i range (num_bands) :
	
SyntaxError: invalid syntax
>>> out_ds.FlushCache()
>>> for i in range (num_bands) :
	out_ds.GetRasterBand(i +1).ComputeStatistics(False)

	
[0.0, 255.0, 114.72168191909893, 46.51511237481718]
[0.0, 255.0, 129.53270699084854, 34.76495241850529]
[0.0, 255.0, 89.38699301456653, 48.387798676899195]
>>> out_ds.BuildOverviews('average', [2,4,8,16])
0
>>> del out_ds
>>> 

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
>>> 
>>> # resampling to larger pixels
>>> print ds.RasterXSize
4
>>> print ds.RasterYSize
11
>>> import numpy as np
>>> data = np.empty(6, 2), np.int)
SyntaxError: invalid syntax
>>> data = np.empty((6, 2), np.int)
>>> band.ReadAsArray(buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    band.ReadAsArray(buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> band.ReadAsArray(0,0, 4,11, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    band.ReadAsArray(0,0, 4,11, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> band = ds.GetRasterBand(1)
>>> band.ReadAsArray(0,0, 4,11, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    band.ReadAsArray(0,0, 4,11, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> data = np.empty((11, 2), np.int)
>>> band.ReadAsArray(0,0, 4,11, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    band.ReadAsArray(0,0, 4,11, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> band.ReadAsArray( buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    band.ReadAsArray( buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> data = np.empty((5, 2), np.int)
>>> band.ReadAsArray(0,1, 4,10, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    band.ReadAsArray(0,1, 4,10, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> 
>>> band.ReadAsArray(0,1, 4,10, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    band.ReadAsArray(0,1, 4,10, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> data = np.empty((5, 2), np.int)
>>> band = ds.GetRasterBand(1)
>>> band.ReadAsArray(0,1, 4,10, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    band.ReadAsArray(0,1, 4,10, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> print data
[[140633014885320        46489664]
 [140632935341160 140632511960632]
 [140632511959840 140632511961640]
 [140632511962576 140632511981544]
 [140632511982768 140632511981184]]
>>> band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_yysize=5, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_yysize=5, buf_obj=data)
TypeError: ReadAsArray() got an unexpected keyword argument 'win_yysize'
>>> band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> data = np.empty((2, 5), np.int)
>>> band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> print data
[[0 0 0 0 0]
 [0 0 0 0 0]]
>>> data = np.empty((5, 2), np.int)
>>> band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> band.ReadAsArray(xoff=0, yoff=0, win_xsize=4, win_ysize=10, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    band.ReadAsArray(xoff=0, yoff=0, win_xsize=4, win_ysize=10, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> band.ReadAsArray(win_xsize=4, win_ysize=10, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    band.ReadAsArray(win_xsize=4, win_ysize=10, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> data = np.empty(5, 2)

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    data = np.empty(5, 2)
TypeError: data type not understood
>>> print ds.GetXSize

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print ds.GetXSize
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 785, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> mytif = 'blue3.tif'
>>> ds = gdal.Open(mytif)
>>> print ds.RasterXSize
4
>>> print ds.RasterYSize
11
>>> band = ds.GetRasterBand(1)
>>> data = np.empty((5, 2), np.int)
>>> band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    band.ReadAsArray(xoff=0, yoff=0, win_xsize=2, win_ysize=5, buf_obj=data)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1355, in ReadAsArray
    buf_xsize, buf_ysize, buf_obj )
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal_array.py", line 302, in BandReadAsArray
    raise ValueError("array does not have corresponding GDAL data type")
ValueError: array does not have corresponding GDAL data type
>>> 

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
>>> new_band.ComputeBandStats()
(114.59106919191782, 46.996522069645444)
>>> new_band.ComputeRasterMinMax()
(0.0, 255.0)
>>> new_band.ComputeStatistics()

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    new_band.ComputeStatistics()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1187, in ComputeStatistics
    return _gdal.Band_ComputeStatistics(self, *args)
TypeError: Band_ComputeStatistics() takes at least 2 arguments (1 given)
>>> new_band.ComputeStatistics(False)
[0.0, 255.0, 114.59106919191782, 46.996522069645444]
>>> new_band.GetBlockSize()
[1181, 6]
>>> new_band.GetColorInterpretation()
1
>>> new_band.GetCategoryNames()
>>> new_band.GetCategoryNames()
>>> new_band.GetColorTable()
>>> new_band.GetDefaultHistogram()
(-0.5, 255.5, 256, [11076, 291, 372, 0, 465, 729, 0, 979, 987, 0, 1251, 1379, 0, 1678, 1784, 0, 1991, 2183, 0, 2307, 2514, 0, 2694, 2922, 0, 2929, 3018, 0, 3045, 2947, 0, 2949, 3047, 0, 3062, 2833, 0, 2652, 2556, 0, 2335, 2330, 0, 2235, 2057, 0, 2168, 1982, 0, 2025, 2045, 0, 2087, 2196, 0, 2320, 2418, 0, 2514, 2614, 0, 2697, 2855, 0, 3057, 2950, 0, 3095, 3221, 0, 3376, 3558, 0, 3638, 3851, 0, 3949, 4007, 0, 4093, 4279, 0, 4359, 4479, 0, 4532, 4780, 0, 4798, 5108, 0, 5359, 5548, 0, 5767, 6063, 0, 6337, 6614, 0, 7063, 7532, 0, 8136, 8628, 0, 9244, 9884, 0, 10128, 10736, 0, 11132, 11364, 0, 11690, 12273, 0, 12706, 13304, 0, 14133, 15456, 0, 16256, 17789, 0, 19595, 20631, 0, 21486, 21630, 0, 21705, 20373, 0, 18813, 17277, 0, 15713, 13960, 0, 12011, 10345, 0, 8715, 7473, 0, 6055, 5194, 0, 4163, 3464, 0, 2978, 2441, 0, 2188, 1825, 0, 1667, 1536, 0, 1384, 1310, 0, 1164, 1137, 0, 1104, 1088, 0, 961, 964, 0, 1029, 980, 0, 950, 933, 0, 889, 963, 0, 939, 877, 0, 913, 928, 0, 944, 901, 0, 916, 905, 0, 890, 913, 0, 894, 926, 0, 880, 919, 0, 886, 885, 0, 935, 903, 0, 901, 872, 0, 880, 909, 0, 912, 891, 0, 874, 880, 0, 897, 862, 0, 908, 857, 0, 822, 851, 0, 860, 849, 0, 827, 857, 0, 912, 823, 0, 891, 865, 0, 882, 922, 0, 981, 1115, 0, 1261, 1136, 0, 1150, 1059, 3362])
>>> new_band.GetHistogram()
[1183, 40, 47, 0, 43, 51, 0, 94, 92, 0, 145, 163, 0, 188, 181, 0, 170, 164, 0, 202, 276, 0, 312, 341, 0, 292, 295, 0, 281, 302, 0, 376, 377, 0, 456, 369, 0, 280, 250, 0, 278, 309, 0, 255, 252, 0, 265, 239, 0, 199, 221, 0, 242, 245, 0, 321, 269, 0, 292, 298, 0, 292, 308, 0, 289, 321, 0, 293, 294, 0, 336, 307, 0, 369, 360, 0, 389, 372, 0, 392, 399, 0, 414, 434, 0, 405, 482, 0, 457, 498, 0, 534, 522, 0, 529, 554, 0, 585, 670, 0, 688, 793, 0, 816, 860, 0, 987, 1028, 0, 998, 1053, 0, 1083, 1170, 0, 1188, 1300, 0, 1279, 1332, 0, 1533, 1700, 0, 1730, 1871, 0, 2011, 2265, 0, 2368, 2272, 0, 2355, 2150, 0, 2108, 1899, 0, 1830, 1595, 0, 1253, 1072, 0, 946, 840, 0, 664, 575, 0, 532, 420, 0, 344, 273, 0, 245, 228, 0, 186, 144, 0, 145, 117, 0, 103, 132, 0, 108, 104, 0, 75, 105, 0, 119, 95, 0, 94, 91, 0, 93, 103, 0, 105, 102, 0, 80, 103, 0, 103, 108, 0, 106, 121, 0, 94, 112, 0, 102, 96, 0, 95, 112, 0, 103, 89, 0, 103, 103, 0, 99, 98, 0, 92, 105, 0, 98, 108, 0, 99, 94, 0, 96, 90, 0, 87, 87, 0, 88, 88, 0, 101, 91, 0, 78, 75, 0, 95, 73, 0, 73, 71, 0, 77, 81, 0, 89, 81, 0, 102, 106, 0, 106, 118, 435]
>>> new_band.GetDescription()
''
>>> new_band.GetOverview()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    new_band.GetOverview()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1202, in GetOverview
    return _gdal.Band_GetOverview(self, *args)
TypeError: Band_GetOverview() takes exactly 2 arguments (1 given)
>>> new_band.GetRasterCategoryNames()
>>> new_band.GetRasterColorInterpretation()
1
>>> new_band.GetScale()
>>> #### ok, I've tried out some options to see what they return..
>>> 
>>> #### now, I will create a red.tif and a green.tif and afterwards I will unite the blue.tif, red.tif and green.tif into a natural_colour.tif
>>> 
>>> print new_ds.GetMetadata()
{}
>>> print old_ds.GetMetadata()
{'DataType': 'Generic', 'AREA_OR_POINT': 'Area'}
>>> print old_ds.RasterCount
3
>>> ctable=blue_band.GetColorTable()
>>> ctable.GetCount()

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ctable.GetCount()
AttributeError: 'NoneType' object has no attribute 'GetCount'
>>> if ctable is None : print 'ctable none'

ctable none
>>> ctable=new_band.GetColorTable()
>>> if ctable is None : print 'ctable none'

ctable none
>>> if new_band is None : print 'new_band none'

>>> ctable=new_band.GetColorTable()
>>> if ctable is None : print 'ctable none'

ctable none
>>> # maybe it doesn't have a colour table
>>> 
>>> 
>>> green_band = old_ds.GetRasterBand(2)
>>> if green_band is None : print 'green band is none'

>>> new_ds2 = gtiff_driver.Create('green.tif', green_band.XSize, green_band.YSize, bands=1)
>>> if new_ds2 is None : print 'new_ds2 is none'
else : print 'new_ds2 is created'

new_ds2 is created
>>> new_ds2.SetProjection(old_ds.GetProjection())
0
>>> new_ds2.SetGeoTransform(old_ds.GetGeoTransform())
0
>>> new_band2 = new_ds2.GetRasterBand(1)
>>> if new_band2 is None : print 'new_band2 is none'
else : print 'new_band2 is open'

new_band2 is open
>>> green_data = green_band.ReadRaster()
>>> new_band2.SetMetadata(green_data)
0
>>> new_ds2.FlushCache()
>>> new_ds2.FlushCache()
>>> green_band = old_ds.GetRasterBand(2)
>>> new_band2 = new_ds2.GetRasterBand(1)
>>> green_data = green_band.ReadRaster()
>>> new_band2.SetMetadata(green_data)
0
>>> new_ds2.FlushCache()
>>> gtiff_driver.Delete('green.tif')
0
>>> new_ds2 = gtiff_driver.Create('green.tif', green_band.XSize, green_band.YSize, bands=1)
>>> new_band2 = new_ds2.GetRasterBand(1)
>>> green_band = old_ds.GetRasterBand(2)
>>> green_data = green_band.ReadRaster()
>>> new_band2 = new_ds2.GetRasterBand(1)
>>> new_band2.SetMetadata(green_data)
0
>>> new_ds2.FlushCache()
>>> gtiff_driver.Delete('green.tif')
0
>>> old_ds= None
>>> 

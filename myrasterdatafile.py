Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> band_fn= '_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif'
>>> in_ds = gdal.Open(band_fn)
>>> in_band = in_ds.GetRasterBand()

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    in_band = in_ds.GetRasterBand()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 809, in GetRasterBand
    return _gdal.Dataset_GetRasterBand(self, *args)
TypeError: Dataset_GetRasterBand() takes exactly 2 arguments (1 given)
>>> in_band = in_ds.GetRasterBand(1)
>>> # I don't have 3 bands, I will just make a copy of the data to see how the GTiff driver works and how a raster data file is created.
>>> 
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> new_ds = gtiff_driver.Create('sacele.tif', in_band.XSize, in_band.YSize, 1, in_band.DataType)
>>> new_ds.SetProjection(in_ds.GetProjection())
0
>>> new_ds.SetGeoTransform(in_ds.GetGeoTransform())
0
>>> in_data = in_band.ReadAsArray()
>>> new_band = new_ds.GetRasterBand(1)
>>> new_band.WriteArray(in_data)
0
>>> new_ds.FlushCache()
>>> in_ds.GetDescription()
'_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif'
>>> in_ds.GetRasterBand(2)
<osgeo.gdal.Band; proxy of <Swig Object of type 'GDALRasterBandShadow *' at 0x7f165c0370f0> >
>>> band2 =in_ds.GetRasterBand(2)
>>> band2.ComputeStatistics()

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    band2.ComputeStatistics()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1187, in ComputeStatistics
    return _gdal.Band_ComputeStatistics(self, *args)
TypeError: Band_ComputeStatistics() takes at least 2 arguments (1 given)
>>> band2.ComputeStatistics(False)
[0.0, 255.0, 129.4003254403454, 35.16296213678928]
>>> # ok, so I do have more bands!!!!
>>> in_ds.RasterCount()

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    in_ds.RasterCount()
TypeError: 'int' object is not callable
>>> in_ds.GetDescription()
'_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif'
>>> print in_ds.GetDescription()
_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif
>>> print in_ds.GetFileList()
['_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif']
>>> in_ds.GetGCPCount()
0
>>> in_ds.GetMetadata_List()
['AREA_OR_POINT=Area', 'DataType=Generic']
>>> in_ds.GetMetadata()
{'DataType': 'Generic', 'AREA_OR_POINT': 'Area'}
>>> in_ds.GetGCPs()
()
>>> # given the fact that it is an ETM tif it should probably have 8 bands,so...let me check the brochoure of USGS on the Landsat project:
>>> # for L7 ETM+ band 1 is blue, band 2 is green, band 3 is red, band 4 is near-infrared, band 5 is shortwawe infrared-1, band 6 T2 is thermal, band 7 is shortwave infrared-2 and band 8 is panchromatic.
>>> gtiff_driver.Delete('sacele.tif')
0
>>> # I try to make a 'natural_sacele.tif' with the first 3 bands of the in_ds:
>>> in_ds.GetRasterBand(1)
<osgeo.gdal.Band; proxy of <Swig Object of type 'GDALRasterBandShadow *' at 0x7f165c04ac90> >
>>> blue_band = in_ds.GetRasterBand(1)
>>> green_band = in_ds.GetRasterBand(2)
>>> red_band = in_ds.GetRasterBand(3)
>>> gtiff_driver.Create('natural_sacele.tif')

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    gtiff_driver.Create('natural_sacele.tif')
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 453, in Create
    return _gdal.Driver_Create(self, *args, **kwargs)
TypeError: Required argument 'xsize' (pos 3) not found
>>> gtiff_driver.Create('natural_sacele.tif', blue_band.XSize, blue_band.YSize, 3, blue_band.DataType)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f1644657bd0> >
>>> new_ds=gtiff_driver.Create('natural_sacele.tif', blue_band.XSize, blue_band.YSize, 3, blue_band.DataType)
>>> new_ds.SetProjection(blue_band.GetProjection)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    new_ds.SetProjection(blue_band.GetProjection)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> new_ds.SetProjection(blue_band.GetProjection())

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    new_ds.SetProjection(blue_band.GetProjection())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1075, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Band, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> new_ds.SetProjection(in_ds.GetProjection())
0
>>> new_ds.SetGeoTransform(in_ds.GetGeoTransform())
0
>>> blue_data = blue_band.ReadAsArray()
>>> red_data = red_band.ReadAsArray()
>>> green_data = green_band.ReadAsArray()
>>> new_ds.GetRasterBand(1).WriteArray(blue_data)
0
>>> new_ds.GetRasterBand(2).WriteArray(green_data)
0
>>> new_ds.GetRasterBand(3).WriteArray(red_data)
0
>>> 

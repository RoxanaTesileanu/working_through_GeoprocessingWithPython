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
>>> new_ds

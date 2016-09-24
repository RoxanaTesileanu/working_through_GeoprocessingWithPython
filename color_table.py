Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # color tables are used in thematic rasters to show how pixels are classified
>>> mytif = 'DEM_Sacele/ASTGTM2_N45E025_dem.tif'
>>> from osgeo import gdal
>>> ds = gdal.Open(mytif)
>>> ds.GetDescription
<bound method Dataset.GetDescription of <osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f539e72c3f0> >>
>>> ds.GetDescription()
'DEM_Sacele/ASTGTM2_N45E025_dem.tif'
>>> ds.RasterCount()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ds.RasterCount()
TypeError: 'int' object is not callable
>>> ds.RasterCount
1
>>> ds.RasterXSize
3601
>>> ds.RasterYSize
3601
>>> band = ds.GetRasterBand(1)
>>> colors = gdal.ColorTable()
>>> #### or I'd better make a copy of the ds as Chris.
>>> driver = gdal.GetDriverByName('gtiff')
>>> new_ds = driver.CreateCopy(ds, 'dem_copy.tif')

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    new_ds = driver.CreateCopy(ds, 'dem_copy.tif')
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 458, in CreateCopy
    return _gdal.Driver_CreateCopy(self, *args, **kwargs)
RuntimeError: not a string
>>> new_ds = driver.CreateCopy('dem_copy.tif', ds)
>>> new_band = new_ds.GetRasterBand(1)
>>> colors = gdal.ColorTable()
>>> # add colors to the color table:
>>> colors.SetColorEntry(1, (112, 153, 89))
>>> colors.SetColorEntry(2, (242, 238, 162))
>>> colors.SetColorEntry(3, (242, 206, 133))
>>> colors.SetColorEntry(4, (194, 140, 124))
>>> colors.SetColorEntry(5, (214, 193, 156))
>>> band.SetRasterColorTable(colors)
3
>>> band.SetColorTable(colors)
3
>>> # ok, so the ds has to have a data_type = GDT_Byte parameter
>>> 
new_ds = driver.CreateCopy('dem_copy.tif', ds, data_type=GDT_Byte)

Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    new_ds = driver.CreateCopy('dem_copy.tif', ds, data_type=GDT_Byte)
NameError: name 'GDT_Byte' is not defined
>>> new_ds = driver.Create('dem_copy2.tif', bands=1, data_type=GDT_Byte)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', bands=1, data_type=GDT_Byte)
NameError: name 'GDT_Byte' is not defined
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, data_type=GDT_Byte)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, data_type=GDT_Byte)
NameError: name 'GDT_Byte' is not defined
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, data_type=1)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, data_type=1)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 453, in Create
    return _gdal.Driver_Create(self, *args, **kwargs)
TypeError: 'data_type' is an invalid keyword argument for this function
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, eType=GDT_Byte)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, eType=GDT_Byte)
NameError: name 'GDT_Byte' is not defined
>>> 
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, eType='GDT_Byte')

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, eType='GDT_Byte')
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 453, in Create
    return _gdal.Driver_Create(self, *args, **kwargs)
TypeError: in method 'Driver_Create', argument 6 of type 'GDALDataType'
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDALDataType='GDT_Byte')

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDALDataType='GDT_Byte')
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 453, in Create
    return _gdal.Driver_Create(self, *args, **kwargs)
TypeError: 'GDALDataType' is an invalid keyword argument for this function
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDALDataType='GDT_Byte')band.SetColorTable(colors)
SyntaxError: invalid syntax
>>> new_band.SetColorTable(colors)
3
>>> new_band = new_ds.GetRasterBand(1)
>>> new_band.SetColorTable(colors)
3
>>> new_band.GetColorTable()
>>> ct = new_band.GetColorTable()
>>> print ct
None
>>> new_band.GetUnitType()
''
>>> print new_band.GetUnitType()

>>> 
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDALDataType='GDT_Byte')

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, GDALDataType='GDT_Byte')
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 453, in Create
    return _gdal.Driver_Create(self, *args, **kwargs)
TypeError: 'GDALDataType' is an invalid keyword argument for this function
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1,'GDT_Byte')
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, gdal.GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', ds.RasterXSize, ds.RasterYSize, bands=1, gdal.GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', 3601, 3601, bands=1, gdal.GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', 3601, 3601, bands=1, gdal.GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy2.tif', 3601, 3601, bands=1)
>>> new_ds = driver.Create('dem_copy3.tif', 3601, 3601, bands=1, gdal.GDT_Byte)
SyntaxError: non-keyword arg after keyword arg
>>> new_ds = driver.Create('dem_copy3.tif', 3601, 3601, bands=1, eType = gdal.GDT_Byte)
>>> new_band = new_ds.GetRasterBand(1)
>>> data = band.ReadAsArray()
>>> new_band.WriteArray(data)
0
>>> new_ds.FlushCache()
>>> new_ds.FlushCache()
>>> data_m = band.ReadRaster()
>>> new_band.SetMetadata(data_m)
0
>>> new_ds.FlushCache()
>>> new_ds.FlushCache()
>>> new_band.SetColorTable(colors)
0
>>> new_band.SetRasterColorTable(colors)
0
>>> new_band.SetRasterColorInterpretation(gdal.GCI_PaletteIndex)
0
>>> new_ds.FlushCache()
>>> new_ds.FlushCache()
>>> del new_band, new_ds
>>> # ok, I've forgotten to add the projection and the geotransform and I only have a black rectangle...I will do this now:
>>> mytif = 'color_table.py'
>>> mytif2 = 'DEM_Sacele/ASTGTM2_N45E025_dem.tif'
>>> ds2 = gdal.Open(mytif2)
>>> ds1 = gdal.Open(mytif1, 1)

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    ds1 = gdal.Open(mytif1, 1)
NameError: name 'mytif1' is not defined
>>> ds1 = gdal.Open(mytif, 1)
>>> proj = ds2.GetProjection()
>>> ds1 = gdal.Open(mytif, 1)
>>> ds1 = gdal.Open(mytif, 2)
>>> ds1 = gdal.Open(mytif)
>>> ds1 = gdal.Open(mytif)
>>> mytif = 'dem_copy3.tif'
>>> ds1 = gdal.Open(mytif, 1)
>>> ds1.SetProjection(proj)
0
>>> gt= ds2.GetGeoTransform()
>>> ds1.SetGeoTransform(gt)
0
>>> ds1.FlushCache()
>>> ds1.FlushCache()
>>> # ok, so it still is black, but is probably because I have't catched the most prevalent pixel values. The color table contains zeros(black) for the values that I didn't change (p.217).
>>> 
ds2 = gdal.Open(mytif2, gdal.GA_Update)
>>> ds1 = gdal.Open(mytif, gdal.GA_Update)
>>> ds1.SetProjection(proj)
0
>>> ds1.SetGeoTransform(gt)
0
>>> ds1.FlushCache()
>>> ds1.FlushCache()
>>> myband = ds1.GetRasterBand(1)
>>> myband.ComputeStatistics(False)
[171.0, 255.0, 254.88373342867132, 1.9586783857436165]
>>> colors = myband.GetRasterColorTable()
>>> colors.SetColorEntry(255, (250, 250, 250))
>>> ds1.FlushCache()
>>> ds1.FlushCache()
>>> del ds1
>>> ds1 = gdal.Open(mytif, gdal.GA_Update)
>>> myband = ds1.GetRasterBand(1)
>>> print myband.GetHistogram()
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 2, 5, 8, 3, 5, 0, 1, 4, 0, 2, 6, 2, 6, 11, 11, 14, 9, 9, 11, 8, 2, 1, 1, 2, 12, 5, 7, 5, 2, 10, 16, 7, 8, 10, 12, 10, 13, 14, 18, 9, 12, 13, 10, 14, 7, 7, 9, 5, 18, 18, 19, 13, 20, 44, 37, 54, 58, 64, 58, 43, 47, 55, 57, 41, 49, 49, 34, 29, 30, 32, 26, 308428]
>>> colors = myband.GetRasterColorTable()
>>> colors.SetColorEntry(255, (250, 250, 250))
>>> ds1.FlushCache()
>>> ds1.FlushCache()
>>> colors.SetColorEntry(254, (250, 250, 250))
>>> 
>>> ds1.FlushCache()
>>> if colors is None : print 'ct none'

>>> del ds1
>>> ds1 = gdal.Open(mytif, gdal.GA_Update)
>>> myband = ds1.GetRasterBand(1)
>>> colors.SetColorEntry(76, (250, 250, 250))
>>> ds1.FlushCache()
>>> ds1.FlushCache()
>>> # the problem is I don't have a classified elevation raster
>>> import numpy as np
>>> ds1 = gdal.Open(mytif, gdal.GA_Update)
>>> myband = ds1.GetRasterBand(1)
>>> data1= np.where(data==range(0, 800), 1)

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    data1= np.where(data==range(0, 800), 1)
ValueError: either both or neither of x and y should be given
>>> data1= np.where(data==range(0, 800), 1, data)
>>> data2= np.where(data==range(800,1300), 2, data)
>>> data3 = np.where(data==range(1300, 2000), 3, data)
>>> data4 = np.where(data==range(2000, 2600), 4, data)
>>> data4 = np.where(data==range(2000, 2600), 4, data)
>>> data= myband.ReadAsArray()
>>> ds_class= driver.CreateCopy('class_rast.tif', mytif)

Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    ds_class= driver.CreateCopy('class_rast.tif', mytif)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 458, in CreateCopy
    return _gdal.Driver_CreateCopy(self, *args, **kwargs)
TypeError: in method 'Driver_CreateCopy', argument 3 of type 'GDALDatasetShadow *'
>>> ds_class= driver.CreateCopy('class_rast.tif', ds)
>>> band = ds.GetRasterBand(1)
>>> data= myband.ReadAsArray()
>>> data1= np.where(data==range(0, 800), 1, data)
>>> data2= np.where(data==range(800,1300), 2, data)
>>> data3 = np.where(data==range(1300, 2000), 3, data)
>>> data4 = np.where(data==range(2000, 2600), 4, data)
>>> band_class = ds_class.GetRasterBand(1)
>>> band_class.WriteArray(data1)
0
>>> band_class.WriteArray(data2)
0
>>> band_class.WriteArray(data3)
0
>>> band_class.WriteArray(data4)
0
>>> ds_class.FlushCache()
>>> colors = gdal.ColorTable()
>>> colors.SetColorEntry(1, (112, 153, 89))
>>> colors.SetColorEntry(2, (242, 238, 162))
>>> colors.SetColorEntry(3, (242, 206, 133))
>>> colors.SetColorEntry(4, (194, 140, 124))
>>> band_class.SetRasterColorTable(colors)
3
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> # blue => band 1
>>> # green => band 2
>>> # red => band 3
>>> 
>>> blue_tif= 'blue.tif'
>>> green_tif ='green.tif'
>>> red_tif = 'red_tif'
>>> red_tif = 'red.tif'
>>> blue_ds = gdal.Open(blue_tif)
>>> green_ds = gdal.Open(green_tif)
>>> red_ds = gdal.Open(red_tif)
>>> blue_band = blue_ds.GetRasterBand(1)
>>> green_band = green_ds.GetRasterBand(1)
>>> red_band = red_ds.GetRasterBand(1)
>>> 
>>> gtiff_driver = gdal.GetDriverByName('GTiff')
>>> nat_colour_ds = gtiff_driver.Create('nat_colour.tif', blue_band.XSize, blue_band.YSize, bands=3)
>>> nat_colour_ds.SetProjection(blue_ds.GetProjection())
0
>>> nat_colour_ds.SetGeoTransform(blue_ds.GetGeoTransform())
0
>>> new_blue_band= nat_colour_ds.GetRasterBand(1)
>>> new_green_band = nat_colour_ds.GetRasterBand(2)
>>> new_red_band = nat_colour_ds.GetRasterBand(3)
>>> blue_data_ar = blue_band.ReadAsArray()
>>> green_data_ar = green_band.ReadAsArray()
>>> red_data_ar = red_band.ReadAsArray()
>>> new_blue_band.WriteArray(blue_data_ar)
0
>>> new_green_band.WriteArray(green_data_ar)
0
>>> new_red_band.WriteArray(red_data_ar)
0
>>> nat_colour_ds.FlushCache()
>>> blue_data_m = blue_band.ReadRaster()
>>> green_data_m = green_band.ReadRaster()
>>> red_data_m = red_band.ReadRaster()
>>> new_blue_band.SetMetadata(blue_data_m)
0
>>> new_green_band.SetMetadata(green_data_m)
0
>>> new_red_band.SetMetadata(red_data_m)
0
>>> nat_colour_ds.FlushCache()
>>> ### did it!!  

>>> 
>>> # for looping through all raster bands:
>>> print '[Raster Band Count]:', nat_colour_ds.RasterCount
[Raster Band Count]: 3
>>> for i in range (nat_colour_ds.RasterCount) :
	nat_colour_ds.GetRasterBand(i).ComputeStatistics(False)

	

Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    nat_colour_ds.GetRasterBand(i).ComputeStatistics(False)
AttributeError: 'NoneType' object has no attribute 'ComputeStatistics'
>>> for i in range (1,4) :
	nat_colour_ds.GetRasterBand(i).ComputeStatistics(False)

	
[0.0, 255.0, 114.59106919191782, 46.996522069645444]
[0.0, 255.0, 129.4003254403454, 35.16296213678928]
[0.0, 255.0, 89.25016434331657, 48.85975802449811]
>>> 

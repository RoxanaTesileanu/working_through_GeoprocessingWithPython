Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # create an array from scratch
>>> import numpy as nm
>>> import numpy as np
>>> np.zeros((3,2))
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])
>>> np.ones((2,3), np.int)
array([[1, 1, 1],
       [1, 1, 1]])
>>> # you have floating-point by default, but you can specify the type if you need to (np.int - if you need integers
>>> np.ones((2,3), np.int)*5
array([[5, 5, 5],
       [5, 5, 5]])
>>> # you can also create an empty array with the empty() function, but you have to fill all cells with real data afterwards!
>>> np.empty((2,2))
array([[  6.94671686e-310,   6.94671686e-310],
       [  9.15535262e-317,   9.15530519e-317]])
>>> # MAP ALGEBRA
>>> # is about adding and subtracting two or more rasters
>>> # there are four types of map algebra:
>>> # LOCAL ANALYSIS - 	works on individual pixels
>>> # FOCAL ANALYSIS - works on a few surrounding pixels
>>> # ZONAL ANALYSIS - works on pixels with the same value
>>> # GLOBAL ANALYSIS - works on entire array
>>> 
>>> # definition of a function to save a new raster
>>> 
>>> def make_raster(in_ds, fn, data, data_type, nodata=None)
SyntaxError: invalid syntax
>>> def make_raster(in_ds, fn, data, data_type, nodata=None) :
	"""Create a one-band GeoTIFF.
	in_ds = datasource to copy projection and geotransform from
	fn = path to the file to create
	data = NumPy array containing data to write
	data_type = output data type
	nodata = optional NoData value
	"""
	driver = gdal.GetDriverbyName('GTiff')
	out_ds = driver.Create(
		fn, in_ds.RasterXSize, in_ds.RasterYSize, bands=1, data_type)
	
SyntaxError: non-keyword arg after keyword arg
>>> from osgeo import gdal
>>> def make_raster(in_ds, fn, data, data_type, nodata=None) :
	"""Create a one-band GeoTIFF.
	in_ds = datasource to copy projection and geotransform from
	fn = path to the file to create
	data = NumPy array containing data to write
	data_type = output data type
	nodata = optional NoData value
	"""
	driver = gdal.GetDriverbyName('GTiff')
	out_ds = driver.Create(
		fn, in_ds.RasterXSize, in_ds.RasterYSize, bands=1, data_type)
	
SyntaxError: non-keyword arg after keyword arg
>>> def make_raster(in_ds, fn, data, data_type, nodata=None) :
	"""Create a one-band GeoTIFF.
	in_ds = datasource to copy projection and geotransform from
	fn = path to the file to create
	data = NumPy array containing data to write
	data_type = output data type
	nodata = optional NoData value
	"""
	driver = gdal.GetDriverbyName('GTiff')
	out_ds = driver.Create(fn, in_ds.RasterXSize, in_ds.RasterYSize, bands=1, data_type)
	
SyntaxError: non-keyword arg after keyword arg
>>> def make_raster(in_ds, fn, data, data_type, nodata=None) :
	"""Create a one-band GeoTIFF.
	in_ds = datasource to copy projection and geotransform from
	fn = path to the file to create
	data = NumPy array containing data to write
	data_type = output data type
	nodata = optional NoData value
	"""
	driver = gdal.GetDriverbyName('GTiff')
	out_ds = driver.Create(fn, in_ds.RasterXSize, in_ds.RasterYSize, bands=1, data_type)
	
SyntaxError: non-keyword arg after keyword arg
>>> def make_raster(in_ds, fn, data, data_type, nodata=None) :
	"""Create a one-band GeoTIFF.
	in_ds = datasource to copy projection and geotransform from
	fn = path to the file to create
	data = NumPy array containing data to write
	data_type = output data type
	nodata = optional NoData value
	"""
	driver = gdal.GetDriverbyName('GTiff')
	out_ds = driver.Create(fn, in_ds.RasterXSize, in_ds.RasterYSize, bands=1, data_type)
	
SyntaxError: non-keyword arg after keyword arg
>>> def make_raster(in_ds, fn, data, data_type, nodata=None) :
	"""Create a one-band GeoTIFF.
	in_ds = datasource to copy projection and geotransform from
	fn = path to the file to create
	data = NumPy array containing data to write
	data_type = output data type
	nodata = optional NoData value
	"""
	driver = gdal.GetDriverbyName('GTiff')
	
	out_ds = driver.Create(fn, in_ds.RasterXSize, in_ds.RasterYSize, 1, data_type)
	out_ds.SetProjection(in_ds.GetProjection())
	out_ds.SetGeoTransform(in_ds.GetGeoTransform())
	out_band = out_ds.GetRasterBand(1)
	if nodata is not None :
		out_band.SetNoDataValue(nodata)
	out_band.WriteArray(data)
	out_band.FlushCache()
	out_band.ComputeStatistics(False)
	return out_ds

>>> # LOCAL ANALYSES
>>> # They work on two or more arrays that are the same size, and an algebraic equation is applied to each set of pixel locations.
>>> # Local map algebra calculations work on pixel-by-pixel basis, so the equation applies to pixels that fall in the same spatial location.
>>> 

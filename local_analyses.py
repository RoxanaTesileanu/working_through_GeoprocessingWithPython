Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # LOCAL ANALYSES
>>> # example using the NDVI - normalized difference vegetation index
>>> # NDVI = (NIR-RED)/(NIR+RED)
>>> # if both denominator and numerator are 0 => np.nan value (not a nomber)
>>> # if only the denominator is 0 => np.inf value (infinity)
>>> # These invalid numbers for pixels that couldn't be calculated affect your statistics.
>>> # => SET INVALID PIXELS TO NoData!
>>> # => REPLACE INVALID NUMBERS WITH ANOTHER NUMBER
>>> # => SET THE NoData VALUE TO THAT NUMBER
>>> from osgeo import gdal
>>> import numpy as np
>>> fn ='DEM_Sacele/zizin/LE71830282016249NSG00.tif'
>>> ds = gdal.Open(fn)
>>> ds.RasterCount()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ds.RasterCount()
TypeError: 'int' object is not callable
>>> ds.RasterCount
3
>>> fn ='_ags_20eac0a2_f4d8_47f4_83d3_b9c7ffd3c15a.tif'
>>> ds = gdal.Open(fn)
>>> ds.RasterCount
3
>>> fn ='_ags_629d8283_ac94_404c_94de_31704b68f0ab.tif'
>>> ds = gdal.Open(fn)
>>> ds.RasterCount
3
>>> fn = 'LE71960262003128EDC00.jpg'
>>> ds = gdal.Open(fn)
>>> ds.RasterCount
3
>>> fn = 'm_4307057_nw_19_1_20120710_20121004.jp2'
>>> ds = gdal.Open(fn)
>>> ds.RasterCount
4
>>> # ok, so I've found a NAIP image on EarthExplorer
>>> red = ds.GetRasterBand(1).ReadAsArray().astype(np.float)
>>> red = ds.GetRasterBand(1).ReadAsArray().astype(np.float)
>>> # because the output is floating point, you convert the red band from byte to floating-point
>>> nir= ds.GetRasterBand(4).ReadAsArray
>>> red = np.ma.masked_where(nir + red == 0, red)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    red = np.ma.masked_where(nir + red == 0, red)
TypeError: unsupported operand type(s) for +: 'instancemethod' and 'float'
>>> red = nm.ma.masked_where((nir + red) == 0, red)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    red = nm.ma.masked_where((nir + red) == 0, red)
NameError: name 'nm' is not defined
>>> red = np.ma.masked_where((nir + red) == 0, red)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    red = np.ma.masked_where((nir + red) == 0, red)
TypeError: unsupported operand type(s) for +: 'instancemethod' and 'float'
>>> mask = np.ma.equal(nir + red, 0)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    mask = np.ma.equal(nir + red, 0)
TypeError: unsupported operand type(s) for +: 'instancemethod' and 'float'
>>> mask = np.ma.equal((nir+red), 0)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    mask = np.ma.equal((nir+red), 0)
TypeError: unsupported operand type(s) for +: 'instancemethod' and 'float'
>>> data = nir + red

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data = nir + red
TypeError: unsupported operand type(s) for +: 'instancemethod' and 'float'
>>> nir= ds.GetRasterBand(4).ReadAsArray.astype(np.float)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    nir= ds.GetRasterBand(4).ReadAsArray.astype(np.float)
AttributeError: 'function' object has no attribute 'astype'
>>> nir= ds.GetRasterBand(4).ReadAsArray().astype(np.float)
>>> red = np.ma.masked_where((nir + red) == 0, red)
>>> # ok, so both bands need to be transformed to floating point.
>>> ndvi = (nir-red)/(nir+red)
>>> ndvi = ndvi.filled(-99)
>>> # this fills the masked pixels with the value -99
>>> # you then set the NoData value to be -99
>>> out_fn='ndvi.tif'
>>> driver = gdal.GetDriverByName('gtiff')
>>> driver.Create(out_fn, ds.RasterXSize, ds.RasterYSize, bands=1, eType=gdal.GDT_Float32)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7ffb80321c30> >
>>> driver.Delete(out_fn)
3
>>> out_ds = driver.Create(out_fn, ds.RasterXSize, ds.RasterYSize, bands=1, eType=gdal.GDT_Float32)
>>> out_ds.SetProjection(ds.GetProjection())
0
>>> out_ds.SetGeoTransform(ds.GetGeotransform())

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    out_ds.SetGeoTransform(ds.GetGeotransform())
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 785, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> out_ds.SetGeoTransform(ds.GetGeoTransform())
0
>>> out_ds.FlushCache()
>>> out_ds.FlushCache()
>>> out_ds.FlushCache()
>>> out_band = out_ds.GetRasterBand(1)
>>> out_band.SetNoDataValue(-99)
0
>>> nodata = out_band.GetNoDataValue()
>>> if nodata is not None :
	out_band.SetNoDataValue(-99)

	
0
>>> out_band.WriteArray(ndvi)
0
>>> out_ds.FlushCache()
>>> out_ds.FlushCache()
>>> out_ds.FlushCache()
>>> del ds, out_ds
>>> 

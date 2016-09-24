Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> ds=gdal.Open('subset.vrt')
>>> gdal.GetDriverByName('jpeg').CreateCopy('subset.vrt', ds)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f7d58794cf0> >
>>> 

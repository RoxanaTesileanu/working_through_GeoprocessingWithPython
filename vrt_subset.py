Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> temp_ds= gdal.Open('nat_colour.tif')
>>> temp_gt= temp_ds.GetGeotransform()

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    temp_gt= temp_ds.GetGeotransform()
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 785, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Dataset, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> temp_gt = temp_ds.GetGeoTransform()
>>> inv_gt = gdal.InvGeoTransform(temp_gt)
>>> if inv_gt is None : print 'inv_gt none'
else : print 'inv_gt is not none'

inv_gt is not none
>>> # or you can use raise RuntimeError()
>>> if inv_gt is None: raise RuntimeError('Inverse geotransform failed')

>>> temp_ds.RasterXSize
1181
>>> temp_ds.RasterYSize
626
>>> subset_uloff=gdal.ApplyGeoTransform(gt, 0, 0)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    subset_uloff=gdal.ApplyGeoTransform(gt, 0, 0)
NameError: name 'gt' is not defined
>>> subset_uloff=gdal.ApplyGeoTransform(temp_gt, 0, 0)
>>> print subset_uloff
[2842586.9770944533, 5727820.656936204]
>>> subset_lroff=gdal.ApplyGeoTransform(temp_gt, 1180, 625)
>>> print subset_lroff
[2878004.6339981784, 5709061.3047626205]
>>> # actually they are not offsets, are real-world coordinates.
>>> # so, I redefine those variables:
>>> subset_ul=gdal.ApplyGeoTransform(temp_gt, 0, 0)
>>> subset_lr=gdal.ApplyGeoTransform(temp_gt, 1180, 625)
>>> # I don't want to use the whole image, so I will redefine these two points as being the ul lr coord. of the whole set:
>>> set_ul=gdal.ApplyGeoTransform(temp_gt, 0, 0)
>>> set_lr=gdal.ApplyGeoTransform(temp_gt, 1180, 625)
>>> ##### I will subset the raster using the following ul, lr points:
>>> ul = (0, 400)
>>> lr=(400, 625)
>>> rows = 625 - 400
>>> print rows
225
>>> columns = 400-0
>>> print columns
400
>>> # now define the gt as a list and alter it:
>>> gt= list(temp_gt)
>>> # now alter the item 0 (origin x coordinate) and 3 (origin y coordinate):
>>> gt[0] +=gt[1] * 400
>>> #no, it is :
>>> gt[0] += gt[1] *0
>>> gt[3] += gt[5]*400
>>> print gt
[2854592.9624855467, 30.01496347773325, 0.0, 5715814.671545111, 0.0, -30.014963477733918]
>>> # now, create the .vrt file:
>>> ds= gdal.GetDriverByName('vrt')
>>> # ooups I mean:
>>> driver = gdal.GetDriverByName('vrt')
>>> ds = driver.Create('subset.vrt', 400, 225, bands=3)
>>> ds.SetProjection(temp_ds.GetProjection())
0
>>> ds.SetGeoTransform(gt)
0
>>> xml= '''
<SimpleSource>
	<SourceFilename relativeToVRT="1"> {fn}</SourceFilename>
	<SourceBand>{band}</SourceBand>
	<SrcRect xOff="{xoff}" yOff="{yoff}"
		 xSize = "{cols}" ySize = "{rows}"/>
	<DestRect xOff="0" yOff="0"
		xSize="{cols}" ySize="{rows}" />
</SimpleSource>
'''
>>> data = {'fn': 'nat_color.tif', 'band':1,
	'xoff': 0, 'yoff':400,
	'cols': 400, 'rows': 225}
>>> meta = {'source_0': xml.format(**data)}
>>> ds.GetRasterBand(1).SetMetadata(meta, 'vrt_sources')
3
>>> data = {'fn': 'nat_colour.tif', 'band':1,
	'xoff': 0, 'yoff':400,
	'cols': 400, 'rows': 225}
>>> meta = {'source_0': xml.format(**data)}
>>> ds.GetRasterBand(1).SetMetadata(meta, 'vrt_sources')
0
>>> data['band']=2
>>> meta = {'source_0': xml.format(**data)}
>>> ds.GetRasterBand(2).SetMetadata(meta, 'vrt_sources')
0
>>> data ['band']=3
>>> meta = {'source_0': xml.format(**data)}
>>> ds.GetRasterBand(3).SetMetadata(meta, 'vrt_sources')
0
>>> del ds, temp_ds
>>> 

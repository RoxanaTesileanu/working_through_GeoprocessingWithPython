Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # define a dataset using an XML file
>>> xml = '''
<SimpleSource>
	<SourceFilename>{0}</SourceFilename>
	<SourceBand>1</SourceBand>
</SimpleSource>
'''
>>> from osgeo import gdal
>>> temp_ds = gdal.Open('nat_colour.tif')
>>> driver = gdal.GetDriverByName('vrt')
>>> ds= driver.Create('nat_color.vrt', temp_ds.RasterXSize, temp_ds.RasterYSize, bands=3)
>>> ds.SetProjection(temp_ds.GetProjection())
0
>>> ds.SetGeoTransform(temp_ds.GetGeoTransform())
0
>>> metadata = {'source_0': xml.format ('nat_colour.tif')}
>>> ds.GetRasterBand(1).SetMetadata(metadata, 'vrt_sources')
0
>>> metadata = {'source_0': xml.format('nat_colour.tif')}
>>> ds.GetRasterBand(2).SetMetadata(metadata, 'vrt_sources')
0
>>> metadata = {'source_0': xml.format('nat_colour.tif')}
>>> ds.GetRasterBand(3).SetMetadata(metadata, 'vrt_sources')
0
>>> 
KeyboardInterrupt
>>> 
ds= driver.Create('nat_color.vrt', temp_ds.RasterXSize, temp_ds.RasterYSize, bands=3)
>>> ds= driver.Create('nat_color2.vrt', temp_ds.RasterXSize, temp_ds.RasterYSize, bands=3)
>>> ds.SetProjection(temp_ds.GetProjection())
0
>>> ds.SetGeoTransform(temp_ds.GetGeoTransform())
0
>>> metadata = {'source_0': xml.format ('nat_colour.tif')}
>>> ds.GetRasterBand(1).SetMetadata(metadata, 'vrt_sources')
0
>>> metadata = {'source_0': xml.format('nat_colour.tif')}
>>> ds.GetRasterBand(2).SetMetadata(metadata, 'vrt_sources')
0
>>> metadata = {'source_0': xml.format('nat_colour.tif')}
>>> ds.GetRasterBand(3).SetMetadata(metadata, 'vrt_sources')
0
>>> del ds
>>> 

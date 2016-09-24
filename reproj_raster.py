Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> from osgeo import ost

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from osgeo import ost
ImportError: cannot import name ost
>>> from osgeo import osr
>>> srs = osr.SpatialReference()
>>> srs.SetWellKnownGeogCS('WGS84'))
SyntaxError: invalid syntax
>>> srs.SetWellKnownGeogCS('WGS84'))
SyntaxError: invalid syntax
>>> srs.SetWellKnownGeogCS('WGS84')
0
>>> old_ds = gdal.Open('nat_colour.tif')
>>> old_proj = old_ds.GetProjection()
>>> print old_proj
PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.017453292519943295]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0],EXTENSION["PROJ4","+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"]]
>>> vrt_ds = gdal.AutoCreateWarpedVRT(old_ds, None, srs.ExportToWkt(), gdal.GRA_Bilinear)
>>> gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f1c780d5e10> >
>>> vrt_ds.FlushCache()
>>> gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f1c780d5ea0> >
>>> old_ds = gdal.Open('DEM_Sacele/zizin/LE71830282016249NSG00.tif')
>>> vrt_ds = gdal.AutoCreateWarpedVRT(old_ds, None, srs.ExportToWkt(), gdal.GRA_Bilinear)
>>> gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f1c780d5b10> >
>>> gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f1c780d5cc0> >
>>> gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
<osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x7f1c780d5ea0> >
>>> mytif_ds= gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
>>> mytif_ds.FlushCache()
>>> mytif_ds.FlushCache()
>>> vrt_ds = gdal.AutoCreateWarpedVRT(old_ds, None, srs.ExportToWkt(), gdal.GRA_Bilinear)
>>> mytif_ds= gdal.GetDriverByName('gtiff').CreateCopy('nat_color_wgs84.tif', vrt_ds)
>>> mytif_ds.FlushCache()
>>> # It worked after running the code a few times
>>> 

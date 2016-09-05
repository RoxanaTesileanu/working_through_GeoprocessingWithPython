Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> path1 = 'ne_110m_land/ne_110m_land.shp'
>>> from osgeo import ogr
>>> from osgeo import osr
>>> ds = ogr.Open(path1, 1)
>>> lyr = ds.GetLayer()
>>> lyr.GetFeatureCount()
127
>>> lyr.GetGeomType()
3
>>> union_poly = ogr.Geometry(3)
>>> for feat in lyr :
	geom = feat.GetGeometryRef()
	union_poly = union_poly.Union(geom)

	

>>> tower = ogr.Geometry(wkt= 'POINT (2.294694 46.858093)')
>>> tower.AssignSpatialReference(
	osr.SpatialReference(osr.SRS_WKT_WGS84))
>>> print (lyr.GetSpatialRef())
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.017453292519943295]]
>>> lyr_sr = lyr.GetSpatialRef()
>>> lyr_sr.GetAuthorityCode('Geogcs')
>>> lyr_sr.GetAttrValue('geogcs')
'GCS_WGS_1984'
>>> lyr_sr.AutoIdentifyEPSG()
0
>>> print (lyr_sr.AutoIdentifyEPSG())
0
>>> lyr_sr.GetAuthorityCode('Geogcs')
'4326'
>>> # both geometries (union_poly and tower) are provided with SRS info, so you can use geom.TransformTo(dest_sr) to reproject them.
>>> 

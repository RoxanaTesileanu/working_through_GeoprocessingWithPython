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

	

>>> 

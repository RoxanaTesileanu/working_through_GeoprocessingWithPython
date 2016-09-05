Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> from osgeo import osr
>>> path1 = 'ne_110m_land/ne_110m_land.shp'
>>> ds = ogr.Open(path1, 1)
>>> lyr = ds.GetLayer()
>>> lyr.GetFeatureCount()
127
>>> lyr.GetGeomType()
3
>>> union_poly = ogr.Geometry(3)
>>> for feat in lyr :
	geom = feat.GetGeometryRef()
	union_poly= union_poly.Union(geom)

	

>>> tower = ogr.Geometry(wkt = 'POINT (2.294694 46.858093)')
>>> tower.AssignSpatialReference(osr.SpatialReference(osr.SRS_WKT_WGS84))
>>> print (lyr.GetSpatialRef())
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.017453292519943295]]
>>> lyr_sr = lyr.GetSpatialRef()
>>> lyr_sr.GetAttrValue('geogcs')
'GCS_WGS_1984'
>>> lyr_sr.AutoIdentifyEPSG()
0
>>> lyr_sr.GetAuthorityCode('geogcs')
'4326'
>>> #both geometries are assigned an SRS (the same), so you can use geom.TransformTo(dest_sr) to reproject them.
>>> 
>>> #because some points like North and South Poles can't be reprojected you have to enable the config "PARTIAL-REPROJECTION"
>>> from osgeo import gdal
>>> gdal.SetConfigOption('OGR_ENABLE_PARTIAL_REPROJECTION', 'TRUE')
>>> web_mercator_sr= osr.SpatialReference()
>>> web_mercator_sr.ImportFromEPSG(3857)
0
>>> union_poly.TransformTo(web_mercator_sr)
6
>>> tower.TransformTo(web_mercator_sr)
0
>>> print(tower)
POINT (255444.167606379633071 5918941.92025978025049)
>>> lyr.GetFeatureCount()
127
>>> union_poly = ogr.Geometry(ogr.wkbMultiPolygon)
>>> for feat in lyr :
	geom = feat.GetGeometryRef()
	union_poly= union_poly.Union(geom)

	
>>> lyr.GetFeatureCount()
127
>>> if union_poly.GetGeometryType() == ogr.wkbPolygon
SyntaxError: invalid syntax
>>> if union_poly.GetGeometryType() == ogr.wkbPolygon :
	union_poly = ogr.ForceToPolygon(union_poly)

	
>>> lyr.GetFeatureCount()
127
>>> lyr.GetGeometryCount()

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lyr.GetGeometryCount()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1060, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> union_poly.TransformTo(web_mercator_sr)
6
>>> 
union_poly.AssignSpatialReference(osr.SpatialReference(osr.SRS_WKT_WGS84))
>>> 
>>> union_poly.AssignSpatialReference(osr.SpatialReference(osr.SRS_WKT_WGS84))
>>> union_poly.TransformTo(web_mercator_sr)
0
>>> # so, it is not enough to have a layer which has a SR, the geometry itself needs to have an SRS assigned!! (p.166)
>>> sr = osr.SpatialReference()
>>> sr.SetWellKnownGeogCS('Dealul_Piscului_1930')
6
>>> sr.SetWellKnownGeogCS('Dealul Piscului 1930')
6
>>> sr.SetWellKnownGeogCS('DealulPiscului1930')
6
>>> sr.ImportFromEPSG(1995)
7
>>> sr.ImportFromEPSG(4316)
0
>>> print sr.SpatialRef()

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print sr.SpatialRef()
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 578, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> print sr.ExportToWkt()
GEOGCS["Dealul Piscului 1930",DATUM["Dealul_Piscului_1930",SPHEROID["International 1924",6378388,297,AUTHORITY["EPSG","7022"]],TOWGS84[103.25,-100.4,-307.19,0,0,0,0],AUTHORITY["EPSG","6316"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4316"]]
>>> # The Romanian Datum is Dealul Piscului 1930
>>> # Dealul Piscului has a EPSG code of 4316
>>> 
>>> # now I try to change the Datum Dealul Piscului 1930 to WGS84:
>>> sr.SetTOWGS84(103.25, -100.4, -307.19)
0
>>> # the parameters are taken from the EPSG report on the transformation from Dealul Piscului to WGS84.
>>> 

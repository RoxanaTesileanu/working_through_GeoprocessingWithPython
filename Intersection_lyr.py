Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> from osgeo import osr
>>> path1 = 'ROU_adm.gpkg'
>>> ds1 = ogr.Open(path1, 1)
>>> coutry_lyr = ds1.GetLayer(0)
>>> path2 = '//home//roxana//Desktop//data//Romania1.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> filtered_lyr = ds2.GetLayer(0)
>>> filtered_lyr.GetFeatureCount()
204
>>> country_lyr.GetFeatureCount()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    country_lyr.GetFeatureCount()
NameError: name 'country_lyr' is not defined
>>> country_lyr = ds1.GetLayer(0)
>>> country_lyr.GetFeatureCount()
1
>>> rou_feat = country_lyr.GetFeature(1)
>>> rou_geom = rou_feat.geom
>>> rou_geom = rou_feat.geometry().Clone()
>>> print (country_lyr.GetSpatialRef())
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]
>>> print (filtered_lyr.GetSpatialRef())
PROJCS["ETRS_1989_LAEA",
    GEOGCS["GCS_ETRS_1989",
        DATUM["European_Terrestrial_Reference_System_1989",
            SPHEROID["GRS_1980",6378137.0,298.257222101]],
        PRIMEM["Greenwich",0.0],
        UNIT["Degree",0.017453292519943295]],
    PROJECTION["Lambert_Azimuthal_Equal_Area"],
    PARAMETER["False_Easting",4321000.0],
    PARAMETER["False_Northing",3210000.0],
    PARAMETER["longitude_of_center",10.0],
    PARAMETER["latitude_of_center",52.0],
    UNIT["Meter",1.0]]
>>> rou_geom.TransformTo(filtered_lyr.GetSpatialRef())
0
>>> filtered_lyr.GetGeometryType()

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    filtered_lyr.GetGeometryType()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1060, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> filtered_lyr.GetGeomType()
3
>>> union_filtered = ogr.Geometry(3)
>>> for feat in filtered_lyr :
	geom = feat.GetGeometryRef()
	union_filtered = union_filtered.Union(geom)

	





>>> intersection = union_filtered.Intersection(rou_geom)
>>> intersection.GetArea()
44735706152.163994
>>> # create spatial reference for the destlyr in which I will save the intersection
>>> sr = osr.SpatialReference()
>>> sr.ImportFromEPSG(3035)
0
>>> driver = ogr.GetDriverByName('ESRI Shapefile')
>>> ds=driver.CreateDataSource('Intersection_lyr.shp')
>>> destlyr = ds.CreateLayer('IntersectionWithSR', sr, ogr.wkbMultiPolygon)
>>> intersection_feat = ogr.Geometry(3)
>>> intersection_feat = ogr.Feature(destlyr.GetLayerDefn())
>>> intersection_feat.SetGeometry(intersection)
0
>>> destlyr.GetFeatureCount()
0
>>> destlyr.CreateFeature(intersection_feat)
0
>>> destlyr.GetFeatureCount()
1
>>> del ds
>>> 

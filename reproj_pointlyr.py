Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path1= 'ne_10m_airports/ne_10m_airports.shp'
>>> ds = ogr.Open(path1, 1)
>>> lyr = ds.GetLayer()
>>> print (lyr.GetName())
ne_10m_airports
>>> print lyr.GetGeomType()
1
>>> print (lyr.GetGeomType() == ogr.wkbPoint)
True
>>> print lyr.GetSpatialRef()
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.017453292519943295]]
>>> # I want to reproject the point layer to another SRS
>>> 

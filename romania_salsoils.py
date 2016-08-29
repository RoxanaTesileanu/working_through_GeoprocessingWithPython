Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path1 = '//home//roxana//working_through_GeoprocessingWithPython//ROU_adm.gpkg'
>>> ds1 = ogr.Open(path1, 1)
>>> 
>>> if ds1 is None : print 'no'
else : print 'yes'

yes
>>> country_lyr = ds1.GetLayer(0)
>>> rou_feat = country_lyr.GetFeature(0)
>>> rou_geom = rou_feat.geometry().Clone()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    rou_geom = rou_feat.geometry().Clone()
AttributeError: 'NoneType' object has no attribute 'geometry'
>>> rou_feat=country_lyr.GetFeature(1)
>>> rou_geom = rou_feat.geometry().Clone()
>>> del ds1
>>> 
>>> # open the second ds with EU soils
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//saline_and_sodic_soils_in_EU//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//saline_and_sodic_soils_in_EU//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//saline_and_sodic_soils_in_EU//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//saline_and_sodic_soils_in_EU//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '\\home\\roxana\\working_through_GeoprocessingWithPython\\saline_and_sodic_soils_in_EU\\datasal_alk_eu27_laea1052.shp'
>>> 
>>> path2 = '\\home\\roxana\\working_through_GeoprocessingWithPython\\saline_and_sodic_soils_in_EU\\data\\sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//saline_and_sodic_soils_in_EU//data//sal_alk_eu27_laea1052.shp'
>>> 
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//saline_and_sodic_soils_in_EU//data//sal_alk_eu27_laea1052.shp'
>>> path2 = '\\home\\roxana\\working_through_GeoprocessingWithPython\\saline_and_sodic_soils_in_EU\\data\\sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = '//home//roxana//working_through_GeoprocessingWithPython//salsoils//data//salsoils.shp'
>>> ds2 = ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> path2 = 'salsoils//data'
>>> ds2 = ogr.Open(path2, 1)
>>> if ds2 is None : print 'no'
else : print 'no'

no
>>> '//home//roxana//Desktop//data//sal_alk_eu27_laea1052.shp'
'//home//roxana//Desktop//data//sal_alk_eu27_laea1052.shp'
>>> path2='//home//roxana//Desktop//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> eu_lyr = ds2.GetLayer(0)
>>> rou_geom.TransformTo(eu_lyr.GetSpatialRef())
0
>>> eu_lyr.SetSpatialFilter(rou_geom)
>>> rou_lyr = ds2.CopyLayer(eu_lyr, 'Romania')
>>> del ds

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    del ds
NameError: name 'ds' is not defined
>>> del ds2
>>> # get the area of saline soils in Romania
>>> path3 = '//home//roxana//Desktop//data//Romania.shp'
>>> ds3 = ogr.Open(path3, 1)
>>> ds3.GetLayer(0)
<osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fbdf3878420> >
>>> soil_lyr = ds3.GetLayer(0)
>>> print(soil_lyr.GetName)
<bound method Layer.GetName of <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fbdf38786f0> >>
>>> print(soil_lyr.GetName())
Romania
>>> totalarea = soil_lyr.schema()

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    totalarea = soil_lyr.schema()
TypeError: 'list' object is not callable
>>> totalarea = soil_lyr.schema
>>> print totalarea
[<osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7fbdf3878390> >]
>>> soil_lyr.schema.count()

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    soil_lyr.schema.count()
TypeError: count() takes exactly one argument (0 given)
>>> for row in soil_lyr :
	soil = row.GetField('Sal_AlkCL')

	
>>> 
>>> 
>>> soil.GetArea()

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    soil.GetArea()
AttributeError: 'int' object has no attribute 'GetArea'
>>> soil_lyr.GetFIDColumn(1)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    soil_lyr.GetFIDColumn(1)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1349, in GetFIDColumn
    return _ogr.Layer_GetFIDColumn(self, *args)
TypeError: Layer_GetFIDColumn() takes exactly 1 argument (2 given)
>>> soil_lyr.GetFeatureCount()
204
>>> for feat in range (soil_lyr.GetFeatureCount()) :
	area = feat.GetArea()

	

Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    area = feat.GetArea()
AttributeError: 'int' object has no attribute 'GetArea'
>>> for feat in range (soil_lyr.GetFeatureCount()) :
	area =feat.geometry().GetArea()

	

Traceback (most recent call last):
  File "<pyshell#89>", line 2, in <module>
    area =feat.geometry().GetArea()
AttributeError: 'int' object has no attribute 'geometry'
>>> 
for feat in range (soil_lyr.GetFeatureCount()) :
	feat_geom =feat.geometry()
	feat_geom.GetArea()

	

Traceback (most recent call last):
  File "<pyshell#93>", line 3, in <module>
    feat_geom =feat.geometry()
AttributeError: 'int' object has no attribute 'geometry'
>>> for i in range (soil_lyr.GetFeatureCount()) :
	feat_geom = feat.geometry()
	feat_geom.GetArea(i)

	

Traceback (most recent call last):
  File "<pyshell#97>", line 2, in <module>
    feat_geom = feat.geometry()
AttributeError: 'int' object has no attribute 'geometry'
>>> feat0 = soil_lyr.GetFeature(0)
>>> feat0.geometry().GetArea()
265661320.594234
>>> soil_lyr.GetSpatialRef()
<osgeo.osr.SpatialReference; proxy of <Swig Object of type 'OSRSpatialReferenceShadow *' at 0x7fbdf3878270> >
>>> print (soil_lyr.GetSpatialRef())
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
>>> feat0.geometry().GetArea() / 1000000
265.661320594234
>>> sql = 'SELECT SUM (OGR_GEOM_AREA) AS area FROM Romania'
>>> lyr = ds3.ExecuteSQL(sql)
>>> print lyr
<osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fbdf3878870> >
>>> print (lyr.GetFeature(0).GetField('area'))
57391779523.9
>>> print (lyr.GetFeature(0).GetField('area') / 1000000)
57391.7795239
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> pathdb = '//home//roxana//Desktop//ROU_adm.gpkg'
>>> datasource = ogr.Open(pathdb, 1)
>>> if datasource None :
	
SyntaxError: invalid syntax
>>> if datasource is None :
	print 'not open'
else :
	print 'all right'

	
all right
>>> lyr1 = datasource.GetLayer(01)
>>> 
>>> print lyr1.GetFeatureCount
<bound method Layer.GetFeatureCount of <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f85950faf30> >>
>>> for field in lyr1.schema :
	print (field.name, field.GetTypeName())

	
('ID_0', 'Integer')
('ISO', 'String')
('NAME_0', 'String')
('ID_1', 'Integer')
('NAME_1', 'String')
('HASC_1', 'String')
('CCN_1', 'Integer')
('CCA_1', 'String')
('TYPE_1', 'String')
('ENGTYPE_1', 'String')
('NL_NAME_1', 'String')
('VARNAME_1', 'String')
('Shape_Length', 'Real')
('Shape_Area', 'Real')
>>> print (lyr1.GetSpatialRef())
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
>>> lyr1def = lyr1.GetLayerDefn()
>>> 

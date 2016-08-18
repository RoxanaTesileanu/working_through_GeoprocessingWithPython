Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> shapefile = '//home//roxana//private//grassdata//saline//data//saline.shp'
>>> datasource = ogr.Open(shapefile, 0)
>>> if datasource is None :
	print ('could not open ')
else :
	print ('all right')

	
all right
>>> lyr = datasource.GetLayer(0)
>>> num_features = lyr.GetFeatureCount()
>>> num_features
927
>>> myfifthfeature = lyr.GetFeature(4)
>>> myfifthfeature.Sal_AlkCL
3
>>> 
>>> lyr.ResetReading
<bound method Layer.ResetReading of <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7fc0c5894780> >>
>>> lyr.GetExtent()
(2650413.3628196027, 6484929.078754643, 1459503.1224782402, 3545890.035717098)
>>> 
>>> print(lyr.GetGeomType ())
3
>>> print(lyr.GetGeomType() == ogr.wkbLineString)
False
>>> print (lyr.GetGeomType() == ogr.wkbPolygon)
True
>>> print (myfifthfeature.geometry().GetGeometryName())
POLYGON
>>> 
>>> print(lyr.GetSpatialRef())
PROJCS["ETRS_1989_LAEA",
    GEOGCS["GCS_ETRS_1989",
        DATUM["European_Terrestrial_Reference_System_1989",
            SPHEROID["GRS_1980",6378137.0,298.257222101]],
        PRIMEM["Greenwich",0.0],
        UNIT["Degree",0.0174532925199433]],
    PROJECTION["Lambert_Azimuthal_Equal_Area"],
    PARAMETER["False_Easting",4321000.0],
    PARAMETER["False_Northing",3210000.0],
    PARAMETER["longitude_of_center",10.0],
    PARAMETER["latitude_of_center",52.0],
    UNIT["Meter",1.0]]
>>> 
>>> for field in lyr.schema :
	print(field.name, field.GetTypeName())

	
('Sal_AlkCL', 'Integer')
>>> #creating a layer and its own shapefile
>>> datafolder = ogr.Open('//home//roxana//private//grassdata//saline//data')
>>> datafolder = ogr.Open('//home//roxana//private//grassdata//saline//data', 1)
>>> if datafolder is None :
	print ('not there')
else :
	print ('all right')

	
all right
>>> newlayer = datafolder.CreateLayer('salinesoils', lyr.GetSpatialRef(), \
				  ogr.wkbPolygon)
>>> newlayer.CreateFields(lyr.schema)
>>> # the schema property allows you to use the list of attributes of the
>>> # initial old layer
>>> 
>>> # to add a feature to a layer you have to create a new blank feature first
>>> # and then to fill it in with information
>>> 
>>> newfeatdefn = newlayer.GetLayerDefn ()
>>> newfeat = ogr.Feature(newfeatdefn)
>>> geom = myfifthfeature.geometry()
>>> geom
<osgeo.ogr.Geometry; proxy of <Swig Object of type 'OGRGeometryShadow *' at 0x7fc0adf70e40> >
>>> newfeat.SetGeometry (geom)
0
>>> print(newfeat.geometry ().GetGeometryName())
POLYGON
>>> 
>>> for i in range(myfifthfeature.GetFieldCount()) :
	value = myfifthfeature.GetField(i)
	newfeat.SetField (i, value)

	
>>> newlayer.CreateFeature(newfeat)
0
>>> numfeatnew = newlayer.GetFeatureCount()
>>> numfeatnew
1
>>> del ds

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del ds
NameError: name 'ds' is not defined
>>> del datasource
>>> 
>>> vp = VectorPlotter (True)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    vp = VectorPlotter (True)
NameError: name 'VectorPlotter' is not defined
>>> 
>>> #get a driver
>>> datasource1 = ogr.Open('//home//roxana//private//grassdata//saline//data//saline.shp')
>>> mydriver = datasource1.GetDriver()
>>> mydriver
<osgeo.ogr.Driver; proxy of <Swig Object of type 'OGRDriverShadow *' at 0x7fc0adf70f00> >
>>> print (mydriver)
<osgeo.ogr.Driver; proxy of <Swig Object of type 'OGRDriverShadow *' at 0x7fc0adf70f00> >
>>> json_driver = ogr.GetDriverByName ('GeoJSON')
>>> json_datasource = json_driver.CreateDataSource(json_datasource)

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    json_datasource = json_driver.CreateDataSource(json_datasource)
NameError: name 'json_datasource' is not defined
>>> json_datasource = json_driver.CreateDataSource()

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    json_datasource = json_driver.CreateDataSource()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 398, in CreateDataSource
    return _ogr.Driver_CreateDataSource(self, *args, **kwargs)
TypeError: Required argument 'utf8_path' (pos 2) not found
>>> json_datasource = json_driver.CreateDataSource(json_file)

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    json_datasource = json_driver.CreateDataSource(json_file)
NameError: name 'json_file' is not defined
>>> json_ds = json_driver.CreateDataSource ('json_file')
>>> if json_ds is None :
	print ('not created')
else :
	print ('created!')

	
created!
>>> mydriver_sqlite = ogr.GetDriverByName('SQLite')
>>> ds_sqlite = mydriver_sqlite.CreateDataSource('//home//roxana//mysqlitefile.sqlite', ['SPATIALITE=yes'])
>>> if os.path.exists(json_file) :
	json_driver.DeleteDataSource (json_file)


Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    if os.path.exists(json_file) :
NameError: name 'os' is not defined
>>> if os.path.exists('//home//roxana//json_file ')
SyntaxError: invalid syntax
>>> if os.path.exits('//home//roxana//json_file') :
	print ('it does exist')

	

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    if os.path.exits('//home//roxana//json_file') :
NameError: name 'os' is not defined
>>> if os.path.exists ('//home//roxana//Sacele.gif ') :
	print ('it already exists')

	

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    if os.path.exists ('//home//roxana//Sacele.gif ') :
NameError: name 'os' is not defined
>>> os.path.exists(/home/roxana/Sacele.gif)
SyntaxError: invalid syntax
>>> os.path.exists(//home//roxana//Sacele.gif)
SyntaxError: invalid syntax
>>> os.path.exists(\home\roxana\Sacele.gif)
SyntaxError: unexpected character after line continuation character
>>> import os
>>> os.path.exists(//home//roxana//Sacele.gif)
SyntaxError: invalid syntax
>>> os.path.exists('//home//roxana//Sacele.gif')
True
>>> os.path.exists('json_file')
True
>>> if os.path.exists('json_file') :
	json_driver.DeleteDataSource ('json_file')

	
0
>>> os.path.exists('json_file')
False
>>> 
>>> 
>>> coord_fld = ogr.FieldDefn ('X', ogr.OFTReal )
>>> coodr_fld.SetWidth(8)

Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    coodr_fld.SetWidth(8)
NameError: name 'coodr_fld' is not defined
>>> coord_fld.SetWidth(8)
>>> coord_fld.SetPrecision(3)
>>> 
>>> newlayer.CreateField(coord_fld)
0
>>> coord_fld.SetName('Y')
>>> 
>>> newlayer.CreateField(coord_fld)
0
>>> >>> i = lyr.GetLayerDefn().GetFieldIndex('Sal_AlkCL')
>>> i
0
>>> changedfld = ogr.FieldDefn ('saltype', OFTInteger)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    changedfld = ogr.FieldDefn ('saltype', OFTInteger)
NameError: name 'OFTInteger' is not defined
>>> changedfld = ogr.FieldDefn ('saltype', ogr.OFTInteger)
>>> lyr.AlterFieldDefn (i, chanfedfld, ogr.ALTER_NAME_FLAG)

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    lyr.AlterFieldDefn (i, chanfedfld, ogr.ALTER_NAME_FLAG)
NameError: name 'chanfedfld' is not defined
>>> lyr.AlterFieldDefn (i, changedfld, ogr.ALTER_FIELD_NAME)

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    lyr.AlterFieldDefn (i, changedfld, ogr.ALTER_FIELD_NAME)
AttributeError: 'module' object has no attribute 'ALTER_FIELD_NAME'
>>> lyr.AlterFieldDefn(i, changedfld, ogr.ALTER_FIELD_FLAG)

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    lyr.AlterFieldDefn(i, changedfld, ogr.ALTER_FIELD_FLAG)
AttributeError: 'module' object has no attribute 'ALTER_FIELD_FLAG'
>>> lyr.AlterFieldDefn (i, changedfld, ogr.ALTER_NAME_FLAG )
6
>>> for field in lyr.schema :
	print (field.name)

	
Sal_AlkCL
>>> print (lyr.GetLayerDefn())
<osgeo.ogr.FeatureDefn; proxy of <Swig Object of type 'OGRFeatureDefnShadow *' at 0x7f7bb41a3810> >
>>> print (lyr.GetLayerDefn().GetFieldIndex('Sal_AlkCL'))
0
>>> changedfld = ogr.FieldDefn ('saltype', ogr.OFTInteger)
>>> lyr.AlterFieldDefn(0, changedfld, ogr.ALTER_NAME_FLAG )
0
>>> for field in lyr.schema :
	print (field.name)

	
saltype
>>> lyr.CreateField(ogr.FieldDefn ('ID', ogr.OFTInteger )
		)
0
>>> for field in lyr.schema :
	print (field.name)

	
saltype
ID
>>> n=1
>>> for feat in lyr :
	feat.SetField('ID', n)
	lyr.SetFeature(feat)
	n += 1

	
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
>>> datasource.ExecuteSQL('REPACK saltype')
>>> datasource.ExecuteSQL('REPACK saline ')
>>> datasource.ExecuteSQL('REPACK' + lyr.GetName())
>>> datasource.ExecuteSQL ('REPACK saline')
>>> # pay attention to blank spaces!! 'saline' is not 'saline '
>>> 
>>> def print_layers (fn) :
	ds=org.Open(fn, 0)
	if ds is None :
		print 'not there'
	else :
		print 'ds open'

		
>>> def print_layers (fn) :
	ds = org.Open(fn, 0)
	if ds is None :
		print 'not open'
	else :
		print 'ds open'
	for i in range (ds.GetLayerCount()) :
		alyrs = ds.GetLayer(i)
		print ('{0};{1}'.format (i, alyrs.GetName())






		       )

		
>>> print_layers (shapefile)

Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print_layers (shapefile)
  File "<pyshell#131>", line 2, in print_layers
    ds = org.Open(fn, 0)
NameError: global name 'org' is not defined
>>> def print_layers (fn) :
	ds = ogr.Open(fn, 0)
	if ds None :
		
SyntaxError: invalid syntax
>>> def print_layers (fn) ;
SyntaxError: invalid syntax
>>> def print_layers (fn) :
	ds = ogr.Open(fn, 0)
	if ds is None :
		print ('ds not open')
	else :
		print ('ds open!')
	for i in range (ds.GetLayerCount()) :
		alyrs=ds.GetLayer(i)
		print ('{0}:{1}'.format(i, alyrs.GetName()))

		
>>> print_layers (shapefile)
ds open!
0:saline
>>> orginfo datasource
SyntaxError: invalid syntax
>>> ogrinfo datasource
SyntaxError: invalid syntax
>>> ogrinfo "datasource"
SyntaxError: invalid syntax
>>> ogrinfo 'datasource'
SyntaxError: invalid syntax
>>> ogrinfo

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    ogrinfo
NameError: name 'ogrinfo' is not defined
>>> url= 'WFS:http://gis.srh.noaa.gov/arcgis/services/watchWarn/' +\
     'MapServer/WFSServer'
>>> print_layers(url)
ds not open

Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    print_layers(url)
  File "<pyshell#146>", line 7, in print_layers
    for i in range (ds.GetLayerCount()) :
AttributeError: 'NoneType' object has no attribute 'GetLayerCount'
>>> # no web mapping for now ! It 's on the TO DO list!
>>> 

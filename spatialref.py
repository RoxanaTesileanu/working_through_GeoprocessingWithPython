Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> path1 = 'ROU_adm.gpkg'
>>> from osgeo import ogr
>>> ds1 = ogr.Open(path1, 1)
>>> lyr= ds1.GetLayer(0)
>>> print (lyr.GetSpatialRef())
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
>>> path2 = '//home//roxana//Desktop//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> lyr2 = ds2.GetLayer(0)
>>> print (lyr2.GetSpatialRef())
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
>>> lyr2.GetSpatialRef().ExportToXML()
'<gml:ProjectedCRS gml:id="ogrcrs1">\n  <gml:srsName>ETRS_1989_LAEA</gml:srsName>\n  <gml:baseCRS>\n    <gml:GeographicCRS gml:id="ogrcrs2">\n      <gml:srsName>GCS_ETRS_1989</gml:srsName>\n      <gml:usesEllipsoidalCS>\n        <gml:EllipsoidalCS gml:id="ogrcrs3">\n          <gml:csName>ellipsoidal</gml:csName>\n          <gml:csID>\n            <gml:name gml:codeSpace="urn:ogc:def:cs:EPSG::">6402</gml:name>\n          </gml:csID>\n          <gml:usesAxis>\n            <gml:CoordinateSystemAxis gml:id="ogrcrs4" gml:uom="urn:ogc:def:uom:EPSG::9102">\n              <gml:name>Geodetic latitude</gml:name>\n              <gml:axisID>\n                <gml:name gml:codeSpace="urn:ogc:def:axis:EPSG::">9901</gml:name>\n              </gml:axisID>\n              <gml:axisAbbrev>Lat</gml:axisAbbrev>\n              <gml:axisDirection>north</gml:axisDirection>\n            </gml:CoordinateSystemAxis>\n          </gml:usesAxis>\n          <gml:usesAxis>\n            <gml:CoordinateSystemAxis gml:id="ogrcrs5" gml:uom="urn:ogc:def:uom:EPSG::9102">\n              <gml:name>Geodetic longitude</gml:name>\n              <gml:axisID>\n                <gml:name gml:codeSpace="urn:ogc:def:axis:EPSG::">9902</gml:name>\n              </gml:axisID>\n              <gml:axisAbbrev>Lon</gml:axisAbbrev>\n              <gml:axisDirection>east</gml:axisDirection>\n            </gml:CoordinateSystemAxis>\n          </gml:usesAxis>\n        </gml:EllipsoidalCS>\n      </gml:usesEllipsoidalCS>\n      <gml:usesGeodeticDatum>\n        <gml:GeodeticDatum gml:id="ogrcrs6">\n          <gml:datumName>European_Terrestrial_Reference_System_1989</gml:datumName>\n          <gml:usesPrimeMeridian>\n            <gml:PrimeMeridian gml:id="ogrcrs7">\n              <gml:meridianName>Greenwich</gml:meridianName>\n              <gml:greenwichLongitude>\n                <gml:angle gml:uom="urn:ogc:def:uom:EPSG::9102">0</gml:angle>\n              </gml:greenwichLongitude>\n            </gml:PrimeMeridian>\n          </gml:usesPrimeMeridian>\n          <gml:usesEllipsoid>\n            <gml:Ellipsoid gml:id="ogrcrs8">\n              <gml:ellipsoidName>GRS_1980</gml:ellipsoidName>\n              <gml:semiMajorAxis gml:uom="urn:ogc:def:uom:EPSG::9001">6378137.0</gml:semiMajorAxis>\n              <gml:secondDefiningParameter>\n                <gml:inverseFlattening gml:uom="urn:ogc:def:uom:EPSG::9201">298.257222101</gml:inverseFlattening>\n              </gml:secondDefiningParameter>\n            </gml:Ellipsoid>\n          </gml:usesEllipsoid>\n        </gml:GeodeticDatum>\n      </gml:usesGeodeticDatum>\n    </gml:GeographicCRS>\n  </gml:baseCRS>\n  <gml:definedByConversion>\n    <gml:Conversion gml:id="ogrcrs9" />\n  </gml:definedByConversion>\n  <gml:usesCartesianCS>\n    <gml:CartesianCS gml:id="ogrcrs10">\n      <gml:csName>Cartesian</gml:csName>\n      <gml:csID>\n        <gml:name gml:codeSpace="urn:ogc:def:cs:EPSG::">4400</gml:name>\n      </gml:csID>\n      <gml:usesAxis>\n        <gml:CoordinateSystemAxis gml:id="ogrcrs11" gml:uom="urn:ogc:def:uom:EPSG::9001">\n          <gml:name>Easting</gml:name>\n          <gml:axisID>\n            <gml:name gml:codeSpace="urn:ogc:def:axis:EPSG::">9906</gml:name>\n          </gml:axisID>\n          <gml:axisAbbrev>E</gml:axisAbbrev>\n          <gml:axisDirection>east</gml:axisDirection>\n        </gml:CoordinateSystemAxis>\n      </gml:usesAxis>\n      <gml:usesAxis>\n        <gml:CoordinateSystemAxis gml:id="ogrcrs12" gml:uom="urn:ogc:def:uom:EPSG::9001">\n          <gml:name>Northing</gml:name>\n          <gml:axisID>\n            <gml:name gml:codeSpace="urn:ogc:def:axis:EPSG::">9907</gml:name>\n          </gml:axisID>\n          <gml:axisAbbrev>N</gml:axisAbbrev>\n          <gml:axisDirection>north</gml:axisDirection>\n        </gml:CoordinateSystemAxis>\n      </gml:usesAxis>\n    </gml:CartesianCS>\n  </gml:usesCartesianCS>\n</gml:ProjectedCRS>\n'
>>> lyr2.GetSpatialRef().IsGeographic()
0
>>> lyr2.GetSpatialRef().IsProjected()
1
>>> if lyr2.GetSpatialRef().IsProjected() is True :
	print 'projected'
else : print 'not projected'

not projected
>>> if lyr2.GetSpatialRef().IsGeographic() : print 'geographic'
else : print 'not geographic'

not geographic
>>> if lyr2.GetSpatialRef().IsGeographic() is True: print 'geographic'
else : print 'not geographic'

not geographic
>>> print (lyr2.GetSpatialRef())
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
>>> laea_sr = lyr2.GetSpatialRef()
>>> laea_sr.GetAttrValue('PROJCS')
'ETRS_1989_LAEA'
>>> laea_sr.GetAttrValue('Authority')
>>> laea_sr.GetAttrValue('AUTHORITY')
>>> # no authority (ESPG)
>>> if lyr.GetSpatialRef().IsGeographic() is True : print 'SRS is geographic'
else : 'SRS not geographic'

'SRS not geographic'
>>> if lyr.GetSpatialRef().IsProjected() is True : print 'SRS is projected'
else : 'SRS not projected'

'SRS not projected'
>>> wgs84_sr = lyr.GetSpatialRef()
>>> wgs84_sr.GetAttrValue ('Authority')
'EPSG'
>>> wgs84_sr.GetAttrValues ('Authority', 1)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    wgs84_sr.GetAttrValues ('Authority', 1)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 578, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> wgs84_sr.GetAttrValue ('Authority', 1)
'4326'
>>> # the ESPG code
>>> wgs84_sr.GetAuthorityCode('datum')
'6326'
>>> wgs84_sr.GetAuthorityCode('unit')
'9122'
>>> wgs84_sr.GetAuthorityCode('geogcs')
'4326'
>>> wgs84_sr.GetAuthorityCode ('spheroid')
'7030'
>>> laea_sr.GetProjParm(osr.SRS_PP_FALSE_EASTING)

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    laea_sr.GetProjParm(osr.SRS_PP_FALSE_EASTING)
NameError: name 'osr' is not defined
>>> from osgeo import osr
>>> laea_sr.GetProjParm(osr.SRS_PP_FALSE_EASTING)
4321000.0
>>> # create a spatial reference objects
>>> # you create a blank SpatialReference object with SpatialReference()
>>> mysr= osr.SpatialReference()
>>> mysr.ImportFromESPG(26912) # you look up the ESPG code

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    mysr.ImportFromESPG(26912) # you look up the ESPG code
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 578, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> mysr.ImportFromESPG(26912) # you look up the ESPG code

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    mysr.ImportFromESPG(26912) # you look up the ESPG code
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 578, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> mysr.ImportFromESPG(26912)

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    mysr.ImportFromESPG(26912)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 578, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> mysr.ImportFromESPG('26912')

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    mysr.ImportFromESPG('26912')
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 578, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> mysr.ImportFromEPSG(26912)
0
>>> # you look up the EPSG code (European Petroleum Survey Group)
>>> mylaea_sr = osr.SpatialReference()
>>> mylaea_sr.ImportFromEPSG(3035)
0
>>> mylaea_sr.GetAttrValue('projcs')
'ETRS89 / LAEA Europe'
>>> mylaea2_sr = osr.SpatialReference()
>>> mylaea_sr.ImportFromProj4('''+proj=laea +lat_0=52 +lon_0=10 +x_0=4321000 +y_0=3210000 +ellps=GRS80 +units=m +no_defs'''
			  )
0
>>> mylaea2_sr.GetAttrValue('projcs')
>>> 
>>> mylaea2_sr.GetAttrValue('geogcs')
>>> mylaea_sr.ImportFromProj4('''+proj=laea +lat_0=52 +lon_0=10 +x_0=4321000 +y_0=3210000 +ellps=GRS80 +units=m +datum=wgs84 +no_defs''')
0
>>> mylaea2_sr.GetAttrValue('projcs')
>>> print mylaea2_sr

>>> print mylaea2_sr.AutoIdentifyEPSG()
7
>>> mylaea2_sr.AutoIdentifyEPSG()
7
>>> mylaea2_sr.GetAttrValue('projcs')
>>> # I guess I prefer the EPSG codes..
>>> mylaea2_sr.ImportFromUrl(http://spatialreference.org/ref/epsg/3035/proj4js/)
SyntaxError: invalid syntax
>>> mylaea2_sr.ImportFromUrl('http://spatialreference.org/ref/epsg/3035/proj4js/')
6
>>> mylaea2_sr.ImportFromUrl('http://spatialreference.org/ref/epsg/3035/proj4/')
0
>>> mylaea2_sr.GetAttrValue('projcs')
'unnamed'
>>> mylaea2_sr.GetAttrValue('datum')
'unknown'
>>> mylaea2_sr.GetAttrValue('sheroid')
>>> mylaea2_sr.GetAttrValue('spheroid')
'GRS80'
>>> mylaea2_sr.GetAttrValue('projection')
'Lambert_Azimuthal_Equal_Area'
>>> mylaea_sr.GetAttrValue('projection')
'Lambert_Azimuthal_Equal_Area'
>>> mylaea_sr.GetAttrValue('authority')
'EPSG'
>>> mylaea2_sr.GetAttrValue('authority')
>>> 
>>> wkt = '''PROJCS["ETRS_1989_LAEA",
		GEOGCS["GCS_ETRS_1989,
			DATUM["European_Terrestrial_Reference_System_1989",
				SPHEROID["GRS_1980", 6378137.0, 298.257222101]],
			PERIMEM["Greenwich",0.0],
			UNIT["Degree",0.0174532925199433]],
		PROJECTION["Lambert_Azimuthal_Equal_Area"],
		PARAMETER["False_Easting",4321000.0],
		PARAMETER["False_Northing",3210000.0],
		PARAMETER["longitude_of_center",10.0],
		PARAMETER["latitude_of_center", 52.0],
		UNIT["Meter",1.0]]'''
>>> mylaea_wkt=osr.SpatialReference(wkt)
>>> mylaea_wkt.GetAttrValue('projcs')

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    mylaea_wkt.GetAttrValue('projcs')
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 658, in GetAttrValue
    return _osr.SpatialReference_GetAttrValue(self, *args)
TypeError: in method 'SpatialReference_GetAttrValue', argument 1 of type 'OSRSpatialReferenceShadow *'
>>> wkt = '''PROJCS["ETRS_1989_LAEA",
		GEOGCS["GCS_ETRS_1989,
			DATUM["European_Terrestrial_Reference_System_1989",
				SPHEROID["GRS_1980",6378137.0,298.257222101]],
			PERIMEM["Greenwich",0.0],
			UNIT["Degree",0.0174532925199433]],
		PROJECTION["Lambert_Azimuthal_Equal_Area"],
		PARAMETER["False_Easting",4321000.0],
		PARAMETER["False_Northing",3210000.0],
		PARAMETER["longitude_of_center",10.0],
		PARAMETER["latitude_of_center",52.0],
		UNIT["Meter",1.0]]'''
>>> mylaea_wkt=osr.SpatialReference(wkt)
>>> mylaea_wkt.GetAttrValue('projcs')

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    mylaea_wkt.GetAttrValue('projcs')
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 658, in GetAttrValue
    return _osr.SpatialReference_GetAttrValue(self, *args)
TypeError: in method 'SpatialReference_GetAttrValue', argument 1 of type 'OSRSpatialReferenceShadow *'
>>> wkt = '''PROJCS["ETRS_1989_LAEA",
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
    UNIT["Meter",1.0]]'''
>>> mylaea_wkt=osr.SpatialReference(wkt)
>>> mylaea_wkt.GetAttrValue('projcs')
'ETRS_1989_LAEA'
>>> # so you can use a WKT string to import the information in a spatial reference object!
>>> 

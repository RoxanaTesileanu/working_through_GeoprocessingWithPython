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
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> form osgeo import ogr
SyntaxError: invalid syntax
>>> from osgeo import ogr
>>> from osgeo import osr
>>> sr1 = osr.SpatialReference()
>>> sr1.ImportFromEPSG(4316)
0
>>> print sr1.ExportToWkt()
GEOGCS["Dealul Piscului 1930",DATUM["Dealul_Piscului_1930",SPHEROID["International 1924",6378388,297,AUTHORITY["EPSG","7022"]],TOWGS84[103.25,-100.4,-307.19,0,0,0,0],AUTHORITY["EPSG","6316"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4316"]]
>>> 
>>> sr2 = osr.SpatialReference()
>>> sr2.ImportFromEPSG(19926)
7
>>> sr2.ImportFromEPSG(3844)
0
>>> print sr2.ExportToWkt()
PROJCS["Pulkovo 1942(58) / Stereo70",GEOGCS["Pulkovo 1942(58)",DATUM["Pulkovo_1942_58",SPHEROID["Krassowsky 1940",6378245,298.3,AUTHORITY["EPSG","7024"]],TOWGS84[33.4,-146.6,-76.3,-0.359,-0.053,0.844,-0.84],AUTHORITY["EPSG","6179"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4179"]],PROJECTION["Oblique_Stereographic"],PARAMETER["latitude_of_origin",46],PARAMETER["central_meridian",25],PARAMETER["scale_factor",0.99975],PARAMETER["false_easting",500000],PARAMETER["false_northing",500000],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AUTHORITY["EPSG","3844"]]
>>> 
>>> sr4.ImportFromEPSG(4179)
0
>>> print sr4.ExportToWkt()
GEOGCS["Pulkovo 1942(58)",DATUM["Pulkovo_1942_58",SPHEROID["Krassowsky 1940",6378245,298.3,AUTHORITY["EPSG","7024"]],TOWGS84[33.4,-146.6,-76.3,-0.359,-0.053,0.844,-0.84],AUTHORITY["EPSG","6179"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4179"]]
>>> sr4.GetAttrValue('proj')
>>> sr4.GetAttrValue('projcs')
>>> sr4.GetAuthorityCode('projcs')
>>> 
>>> ### In conclusion I've only found Dealul Piscului 1930 (code 4316), Pulkovo 1942(58)/Stereo 70 (code 3844) and Pulkovo 1942 (58) (code 4179). The last one seams to be more accurate from what I see in the EPSG report.  

#### THE PROJ4 STRING FOR PULKOVO 1942(58)/STEREO 70 (CODE 3844) IS:
EPSG:3844 : +title=Stereo 70 +proj=sterea +lat_0=46 +lon_0=25 +k=0.99975 +x_0=500000 +y_0=500000 +ellps=krass +towgs84=33.4,-146.6,-76.3,-0.359,-0.053,0.844,-0.84 +units=m +no_defs

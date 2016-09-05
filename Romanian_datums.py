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
>>> sr3 = osr.SpatialReference()
>>> sr3.ImportFromEPSG(1197)
7
>>> sr3.ImportFromEPSG(3845)
0
>>> print sr3.ExportToWkt()
PROJCS["SWEREF99 / RT90 7.5 gon V emulation",GEOGCS["SWEREF99",DATUM["SWEREF99",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6619"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4619"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",11.30625],PARAMETER["scale_factor",1.000006],PARAMETER["false_easting",1500025.141],PARAMETER["false_northing",-667.282],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AUTHORITY["EPSG","3845"]]
>>> sr4 = osr.SpatialReference()
>>> sr4.ImportFromEPSG(3846)
0
>>> print sr4.ExportToWkt()
PROJCS["SWEREF99 / RT90 5 gon V emulation",GEOGCS["SWEREF99",DATUM["SWEREF99",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6619"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4619"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",13.55626666666667],PARAMETER["scale_factor",1.0000058],PARAMETER["false_easting",1500044.695],PARAMETER["false_northing",-667.13],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AUTHORITY["EPSG","3846"]]
>>> sr4 = osr.SpatialReference()
>>> sr4.ImportFromEPSG(9926)
7
>>> sr4 = osr.SpatialReference()
>>> print sr4.ExportToWkt(4179)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print sr4.ExportToWkt(4179)
  File "/usr/lib/python2.7/dist-packages/osgeo/osr.py", line 1088, in ExportToWkt
    return _osr.SpatialReference_ExportToWkt(self, *args)
TypeError: SpatialReference_ExportToWkt() takes exactly 1 argument (2 given)
>>> sr4.ImportFromEPSG(4179)
0
>>> print sr4.ExportToWkt()
GEOGCS["Pulkovo 1942(58)",DATUM["Pulkovo_1942_58",SPHEROID["Krassowsky 1940",6378245,298.3,AUTHORITY["EPSG","7024"]],TOWGS84[33.4,-146.6,-76.3,-0.359,-0.053,0.844,-0.84],AUTHORITY["EPSG","6179"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4179"]]
>>> sr4.GetAttrValue('proj')
>>> sr4.GetAttrValue('projcs')
>>> sr4.GetAuthorityCode('projcs')
>>> 
>>> ### In conclusion I've only found Dealul Piscului 1930 (code 4316), Pulkovo 1942(58)/Stereo 70 (code 3844) and Pulkovo 1942 (58) (code 4179). The last one seams to be more accurate from what I see in the EPSG report.  

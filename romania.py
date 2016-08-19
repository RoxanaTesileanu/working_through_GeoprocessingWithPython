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
>>> #using attribute filters
>>> lyr2 = datasource.GetLayer(1)
>>> lyr2.SetAttributeFilter('NAME_1 = "RO.BV"')
0
>>> lyr2.GetFeatureCount
<bound method Layer.GetFeatureCount of <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f85acdd7ab0> >>
>>> lyr2.GetFeatureCount()
0
>>> lyr2.SetAttributeFilter('HASC_1 = "RO.BV"')
0
>>> lyr2.GetFeatureCount()
1
>>> lyr3 = datasource.GetLayer(2)
>>> lyr3.SetAttributeFilter('ID_1 = 8')
0
>>> lyr3.GetFeatureCount()
52
>>> lyr3.GetFeature(2).GetField('HASC_1')

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    lyr3.GetFeature(2).GetField('HASC_1')
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 3271, in GetField
    raise ValueError("Illegal field requested in GetField()")
ValueError: Illegal field requested in GetField()
>>> ly3.GetFeature(2).GetField(HASC_1)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ly3.GetFeature(2).GetField(HASC_1)
NameError: name 'ly3' is not defined
>>> lyr3.GetFeature(2).GetField(HASC_1)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lyr3.GetFeature(2).GetField(HASC_1)
NameError: name 'HASC_1' is not defined
>>> lyr3.GetFeature(2).GetField(8)
>>> 
>>> 
>>> lyr3.GetFeature(2).GetField(7)
>>> 
>>> print (lyr3.GetFeature(2).GetField(7))
None
>>> print(lyr3.GetFeature(2).GetField(8))
None
>>> print(lyr3.GetFeature(2).GetField(8))
None
>>> print((lyr3.GetFeature(2).GetField(1))








      )
ROU
>>> print((lyr3.GetFeature(2).GetField(5))

      )
2
>>> print((lyr3.GetFeature(2).GetField(5)))
2
>>> 
>>> print((lyr3.GetFeature(2).GetField(6))

      )
Aiud
>>> print(lyr3.GetFeature(2).GetField('NAME_2'))
Aiud
>>> # the error was because HASC_1 doesn't exist in lyr3!
>>> 
>>> # clear out the attribute filter and get all features
# back pass NONE to SetAttributeFilter
>>> lyr3.SetAttributeFilter(None)
0
>>> lyr3.GetFeatureCount()
2939
>>> # using spatial filters
>>> rogeom = lyr1.GetGeometryColumn()
>>> rogeom = lyr1.GetGeometryColumn().Clone()

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    rogeom = lyr1.GetGeometryColumn().Clone()
AttributeError: 'str' object has no attribute 'Clone'
>>> rogeom = lyr1.geometry().Clone()

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    rogeom = lyr1.geometry().Clone()
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 1060, in <lambda>
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 74, in _swig_getattr
    return _swig_getattr_nondynamic(self, class_type, name, 0)
  File "/usr/lib/python2.7/dist-packages/osgeo/ogr.py", line 69, in _swig_getattr_nondynamic
    return object.__getattr__(self, name)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> 

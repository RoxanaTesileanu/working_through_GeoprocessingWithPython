Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> sw = ogr.Geometry(ogr.wkbLineString)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sw = ogr.Geometry(ogr.wkbLineString)
NameError: name 'ogr' is not defined
>>> from osgeo import ogr
>>> sw = ogr.Geometry(ogr.wkbLineString)
>>> 

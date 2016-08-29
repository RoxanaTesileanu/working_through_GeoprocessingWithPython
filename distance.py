Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> pt1_2d = ogr.Geometry(ogr.wkbPoint)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pt1_2d = ogr.Geometry(ogr.wkbPoint)
NameError: name 'ogr' is not defined
>>> from osgeo import ogr
>>> pt1_2d = ogr.Geometry(ogr.wkbPoint)
>>> pt1_2d.AddPoint(15,15)
>>> pt2_2d = ogr.Geometry(ogr.wkbPoint)
>>> pt2_2d.AddPoint(15, 19)
>>> print(pt1_2d.Distance(pt2_2d)


      )
4.0
>>> # returns a distance of 4 units
>>> pt1_25d=ogr.Geometry(ogr.wkbPoint25D)
>>> pt1_25d.AddPoint(15, 15, 0)
>>> pt2_25d= ogr.Geometry(ogr.wkbPoint25D)
>>> pt2_25d.AddPoint(15,19,3)
>>> print(pt1_25d.Distance(pt2_25d)

      )
4.0
>>> # but the real distance is 5!
>>> 
>>> # OGR DOESN'T TAKE Z VALUES INTO ACCOUNT WHEN PERFORMING SPATIAL OPERATIONS!
>>> 

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

>>> sw
<osgeo.ogr.Geometry; proxy of <Swig Object of type 'OGRGeometryShadow *' at 0x7fd5271b1cc0> >
>>> sw.AddPoint(54, 37)
>>> sw.AddPoint(62, 35.5)
>>> sw.AddPoint(70.5, 38)
>>> sw.AddPoint(74.5, 41.5)
>>> print(sw)
LINESTRING (54 37 0,62.0 35.5 0,70.5 38.0 0,74.5 41.5 0)
>>> sw.SetPoint(3, 76, 41.5)
>>> print(sw)
LINESTRING (54 37 0,62.0 35.5 0,70.5 38.0 0,76.0 41.5 0)
>>> for i in range (sw.GetPointCount()) :
	sw.SetPoint(i, sw.GetX(i), (sw.GetY(i) +1))

	
>>> print(sw.GetPoints())
[(54.0, 38.0, 0.0), (62.0, 36.5, 0.0), (70.5, 39.0, 0.0), (76.0, 42.5, 0.0)]
>>> vertices = sw.GetPoints()
>>> vertices[2:2] = [(66.5, 35)]
>>> print(vertices)
[(54.0, 38.0, 0.0), (62.0, 36.5, 0.0), (66.5, 35), (70.5, 39.0, 0.0), (76.0, 42.5, 0.0)]
>>> new_sw = ogr.Geometry(ogr.wkbLineString)
>>> for vertex in vertices :
	new_sw.AddPoint(*vertex)

	
>>> vertices = line.GetPoints()

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    vertices = line.GetPoints()
NameError: name 'line' is not defined
>>> vertices = sw.GetPoints()
>>> print (vertices)
[(54.0, 38.0, 0.0), (62.0, 36.5, 0.0), (70.5, 39.0, 0.0), (76.0, 42.5, 0.0)]
>>> print(new_sw)
LINESTRING (54 38 0,62.0 36.5 0,66.5 35.0 0,70.5 39.0 0,76.0 42.5 0)
>>> vertices2 = new_sw.GetPoints()
>>> vertices2[4:4] = [(75, 42)]
>>> vertices2[2:2]= [(61, 36)]
>>> new_line = ogr.Geometry(ogr.wkbLineString)
>>> for vertex in vertices2 :
	new_line.AddPoint(*vertex)

	
>>> myline = ogr.Geometry(ogr.wkbLineString)
>>> myline.AddPoint(54, 38)
>>> myline.AddPoint(62, 36)
>>> myvertices = myline.GetPoints()
>>> myvertices[1:1] = [(55, 37)]
>>> for i in range (len(myvertices) :
		
SyntaxError: invalid syntax
>>> for i in range (len(myvertices)) :
	myline.SetPoint(i, for vertex in vertices2 :
		new_line.AddPoint(*vertex)
			
SyntaxError: invalid syntax
>>> 
>>> for i in range (len(myvertices)) :
	myline.SetPoint(i, *myvertices[i])

	
>>> path1 = ogr.Geometry(ogr.wkbLineString)
>>> path1.AddPoint(61.5, 29)
>>> path1.AddPoint(63, 20)
>>> path1.AddPoint(62.5, 16)
>>> path1.AddPoint(60, 13)
>>> 
>>> path2 = ogr.Geometry(ogr.wkbLineString)
>>> path2.AddPoint(60.5, 12)
>>> path2.AddPoint(68.5, 13.5)
>>> 
>>> path3 = ogr.Geometry(ogr.LineString)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    path3 = ogr.Geometry(ogr.LineString)
AttributeError: 'module' object has no attribute 'LineString'
>>> path3 = ogr.Geometry(ogr.wkbLineString)
>>> path3.AddPoint(69.5, 33)
>>> path3.AddPoint(80, 33)
>>> path3.AddPoint(86.5, 22.5)
>>> 
>>> paths = ogr.Geometry(ogr.wkbMultiLineString)
>>> paths.AddGeometry(path1)
0
>>> paths.AddGeometry(path2)
0
>>> paths.AddGeometry(path3)
0
>>> print(paths)
MULTILINESTRING ((61.5 29.0 0,63 20 0,62.5 16.0 0,60 13 0),(60.5 12.0 0,68.5 13.5 0),(69.5 33.0 0,80 33 0,86.5 22.5 0))
>>> paths.GetGeometryRef(0).SetPoint(1, 63, 22)
>>> print(paths)
MULTILINESTRING ((61.5 29.0 0,63 22 0,62.5 16.0 0,60 13 0),(60.5 12.0 0,68.5 13.5 0),(69.5 33.0 0,80 33 0,86.5 22.5 0))
>>> for i in range(paths.GetGeometryCount)) :
	
SyntaxError: invalid syntax
>>> for i in range (paths.GetGeometryCount()) :
	path= paths.GetGeometryRef(i)
	for j in range (path.GetPointCount()) :
		path.SetPoint(j, (path.GetX(j) +2) , (path.GetY(j) -3))

		
>>> IsValid(paths)

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    IsValid(paths)
NameError: name 'IsValid' is not defined
>>> paths.IsValid()
True
>>> 

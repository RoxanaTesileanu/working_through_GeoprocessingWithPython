Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> file_list = ['green.tif', 'blue.tiff', 'red.tif']
>>> # handle errors with a try/except block:
>>> # you have to enable the gdal.UseExceptions()
>>> gdal.UseExceptions()
>>> for fn in file_list :
	try :
		ds= gdal.Open(fn)
		ds.GetRasterBand(1).ComputeStatistics(False)
	except :
		print ('could not compute stats for'+fn)
		print (gdal.GetLastErrorMsg())

		
[0.0, 255.0, 129.4003254403454, 35.16296213678928]
could not compute stats forblue.tiff
`blue.tiff' does not exist in the file system,
and is not recognised as a supported dataset name.

[0.0, 255.0, 89.25016434331657, 48.85975802449811]
>>> # so, the code doesn't stopps at an error. it continues with the next task but throws an exception..
>>> # also, if you need the error message, you can get access to the error message using the GetLastErrorMsg() function!
>>> 
>>> # 2nd trick is using the error handlers!
>>> # GDAL calls error handlers whenever a GDAL function runs into an error.
>>> 
>>> # you can set up a personalized error handler for your needs with the Error() function:
>>> from osgeo import osr
>>> def comp_srs(ds1, ds2):
	if ds1.GetProjection() != ds2.GetProjection() :
		gdal.Error(gdal.CE_Failure, gdal.CPLE_AppDefined,
			   'Datasets must have the same srs!')
		return False

	
>>> ds1, ds2, ds3 = gdal.Open(file_list)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    ds1, ds2, ds3 = gdal.Open(file_list)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1800, in Open
    return _gdal.Open(*args)
RuntimeError: not a string
>>> file_list2= ['green.tif', 'red.tif']
>>> for fn in file_list2 :
	try :
		ds = gdal.Open(file_list2)
		comp_srs(gdal.Open(file_list2))
	except:
		print (gdal.GetLastErrorMsg())

		


>>> 
>>> ds1, ds2 = gdal.Open(file_list2)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ds1, ds2 = gdal.Open(file_list2)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1800, in Open
    return _gdal.Open(*args)
RuntimeError: not a string
>>> for fn in file_list2 :
	ds1, ds2 = gdal.Open(file_list2)

	

Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    ds1, ds2 = gdal.Open(file_list2)
  File "/usr/lib/python2.7/dist-packages/osgeo/gdal.py", line 1800, in Open
    return _gdal.Open(*args)
RuntimeError: not a string
>>> 

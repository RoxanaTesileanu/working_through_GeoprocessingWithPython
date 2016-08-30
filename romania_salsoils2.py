Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path1= 'ROU_adm.gpkg'
>>> ds1 = ogr.Open(path1, 1)
>>> country_lyr = ds1.GetLayer(0)
>>> print (country_lyr.GetName())
ROU_adm0
>>> path2 = '//home//roxana//Desktop//data//sal_alk_eu27_laea1052.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> eu_lyr = ds2.GetLayer(0)
>>> print (eu_lyr.GetName())
sal_alk_eu27_laea1052
>>> rou_feat = coutry_lyr.GetFeature(1)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    rou_feat = coutry_lyr.GetFeature(1)
NameError: name 'coutry_lyr' is not defined
>>> rou_feat = country_lyr.GetFeature(1)
>>> rou_geom = rou_feat.geometry().Clone()
>>> rou_geom.TransformTo(eu_lyr.GetSpatialRef())
0
>>> eu_lyr.SetSpatialFilter(rou_geom)
>>> sql = 'SELECT SUM (OGR_GEOM_AREA) AS area FROM eu_lyr'
>>> lyr = ds2.ExecuteSQL(sql)
>>> print (lyr.GetFeature(0).GetField('area')/ 1000000)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (lyr.GetFeature(0).GetField('area')/ 1000000)
AttributeError: 'NoneType' object has no attribute 'GetFeature'
>>> lyr = ds2.ExecuteSQL(sql)
>>> if lyr is None : print 'none'

none
>>> feat0 = eu_lyr.GetFeature(0)
>>> feat0.geometry().GetArea()
119103155.27905321
>>> feat0.geometry().GetArea() / 1000000
119.10315527905321
>>> eu_lyr.GetFeatureCount()
204
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (area)

	
119.103155279
139.566250414
40.3062743012
55.2446822469
172.418069882
89.7804470029
221.585513566
1538.76934671
220.845547815
1347.05546315
233.984313121
127.179418446
873.229780324
309.223350938
322.517125074
236.484595405
2046.9291116
880.142152526
326.274898516
337.367963371
112.891919155
351.195898157
416.083819349
278.530061427
214.088715947
99.8564202581
137.849147644
331.39904151
277.560958853
74.1615935004
653.390873345
86.7738892004
711.078891267
537.661698626
258.493155371
236.453624689
207.875796544
5078.51550017
175.300576722
166.9331564
136.138507374
250.066354848
174.463830196
836.748572214
130.023363398
166.329238644
798.31676708
320.067055767
267.407319347
123.812396896
166.814793633
235.540296152
206.296612329
234.054500023
506.314415782
251.111554061
127.764911144
221.684615252
119.53802246
101.731459656
71.896233617
107.36872297
400.928668895
289.169352528
150.255111693
168.60055753
447.527172328
49.0197052067
119.842490838
63.1252070713
79.0608132583
125.025692952
141.055082278
694.357190993
198.690550139
186.635492092
148.497902774
141.568761246
38.8171812707
347.645633095
232.335586767
192.158410335
930.159025198
199.119332356
207.611464014
203.118886544
209.975332972
667.132100045
817.675840573
1974.51524114
357.077246376
352.40408923
174.873369701
294.236717954
142.467506597
120.790110284
51.4447972326
131.982825934
85.4719969779
42.1398662632
455.304207195
509.67101199
81.6107788524
465.462109834
239.777392826
321.326574868
157.364127728
98.3703399024
209.583558477
381.063395049
43.7622092173
284.228790407
237.73784297
223.583712417
138.300982352
277.955488028
99.9120950057
347.196666274
142.834824772
200.542965138
324.992064483
341.179984137
241.624759694
449.133939976
263.772332316
4047.06362639
39.539031561
14.8954961554
547.933507719
21.8788928945
57.9167498915
66.4734324044
326.588751162
35.7127139103
65.4063816626
87.2602463449
73.6469347617
38.4296917227
50.6556115457
261.032919264
1223.63771287
169.040217364
887.073677203
58.0701991808
67.0193288574
12.2807737016
41.3197437671
33.535448491
36.9655251277
35.3013681903
76.3645754657
35.9663674325
56.0272747761
43.3000279706
20.3916231398
43.7530263844
18.727774635
534.084567584
220.999515261
441.669781529
206.369557981
326.665453552
505.756372419
39.0059568127
22.8610718301
37.6066805492
41.5870918319
46.8650882145
70.1279315405
126.773410748
58.5143788187
96.8108731108
64.8900529406
86.8576189691
41.0733191909
39.1217438847
36.6709314696
40.0808583534
94.3982255923
17.4069441814
43.8385860951
101.938820352
93.2535628038
55.6362654689
53.7062051575
23.1391634624
50.1258998723
216.383210014
234.626079064
83.0368650881
87.2710580101
95.6050598506
35.6061845353
112.855661388
265.661320594
213.152600451
87.3633812218
114.233005745
70.5028109825
51.8469427839
137.290005986
95.8583093768
56.7244487782
1825.83877114
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(area))

	

Traceback (most recent call last):
  File "<pyshell#30>", line 4, in <module>
    print (sum(area))
TypeError: 'float' object is not iterable
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(*area))

	

Traceback (most recent call last):
  File "<pyshell#32>", line 4, in <module>
    print (sum(*area))
TypeError: sum() argument after * must be an iterable, not float
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(sequence[*are]))
	
SyntaxError: invalid syntax
>>> 
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(sequence[*area]))
	
SyntaxError: invalid syntax
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(sequence[*area]))
	
SyntaxError: invalid syntax
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(sequence[area]))

	

Traceback (most recent call last):
  File "<pyshell#38>", line 4, in <module>
    print (sum(sequence[area]))
NameError: name 'sequence' is not defined
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(*area))

	

Traceback (most recent call last):
  File "<pyshell#40>", line 4, in <module>
    print (sum(*area))
TypeError: sum() argument after * must be an iterable, not float
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(area))

	

Traceback (most recent call last):
  File "<pyshell#42>", line 4, in <module>
    print (sum(area))
TypeError: 'float' object is not iterable
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(eatures.geometry().GetArea() / 1000000))

	

Traceback (most recent call last):
  File "<pyshell#44>", line 4, in <module>
    print (sum(eatures.geometry().GetArea() / 1000000))
NameError: name 'eatures' is not defined
>>> for i in range (eu_lyr.GetFeatureCount()) :
	features = eu_lyr.GetFeature(i)
	area = features.geometry().GetArea() / 1000000
	print (sum(features.geometry().GetArea() / 1000000))

	

Traceback (most recent call last):
  File "<pyshell#46>", line 4, in <module>
    print (sum(features.geometry().GetArea() / 1000000))
TypeError: 'float' object is not iterable
>>> rou_lyr = ds2.CopyLayer(eu_lyr, 'Romania1')
>>> del ds2
>>> 

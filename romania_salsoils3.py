Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import ogr
>>> path1 = 'ROU_adm.gpkg'
>>> ds1 = ogr.Open(path1, 1)
>>> country_lyr = ds1.GetLayer(0)
>>> print (country_lyr.GetName())
ROU_adm0
>>> path2 = '//home//roxana//Desktop//data//Romania1.shp'
>>> ds2 = ogr.Open(path2, 1)
>>> filtered_lyr = ds2.GetLayer(0)
>>> print (filtered_lyr.GetName())
Romania1
>>> rou_feat = country_lyr.GetFeature(1)
>>> rou_geom = rou_feat.geometry().Clone()
>>> rou_geom.TransformTo(filtered_lyr.GetSpatialRef())
0
>>> for i in range (filtered_lyr.GetFeatureCount()) :
	features = filtered_lyr.GetFeature(i)
	filtered_geom = features.geometry()
	intersection = filtered_geom.Intersection(rou_geom)
	print intersection.GetArea()

	
11320542.5203
30285456.9529
21591849.9913
62271445.963
51846942.7839
137290005.986
95858309.3768
56724448.7782
1825838771.14
108855209.461
48898958.1831
37107673.0034
100854635.12
266627602.386
24770669.6033
117104331.539
53856020.1644
183303482.38
1190728582.57
37979303.1402
60139015.0398
39070.2152261
1827266667.06
1471976.27611
231924821.628
71029979.6875
160146186.692
70858255.534
195279370.302
11670345.5021
167461.199464
13889.3237129
50228146.5201
47036615.1324
75208630.8875
21368909.5731
47236569.1063
47514404.5999
57921892.9523
31112149.1679
55640308.9337
48315616.1848
40693124.915
50063996.6195
49580900.3952
48909046.4247
52212362.4543
51216775.5061
30890286.4373
42210637.4671
40354902.9191
46102152.6033
47580545.3821
53667745.0639
266158026.198
37353078.3
2673119.64334
1433451.63114
3746677.41602
46106807.9101
28489066.5284
34096672.6336
111423131.748
54689510.6002
26003204.1172
11871394.5371
8509397.9476
121373325.363
11580305.6103
68272882.2433
66401904.5508
33119570.0609
466950994.825
61777842.2384
82093549.6484
118838367.916
16929072.3376
29383521.9402
14897548.2292
4437294.91331
101135159.908
74239322.2652
60607929.608
146627551.451
6443449.98228
25436871.7389
6282040854.06
33772501.5848
44062866.4324
31262810.2423
49638954.2211
24639528.9452
1048990.40037
14610888695.7
91755097.7739
5963151593.64
534827490.415
4635343.33143
236685412.708
131708031.614
7892593.21122
590613870.149
69771847.1517
32697740.1146
23849619.3065
3169786.09234
14476030.6592
20721055.9951
2203098.1439
1570364.24553
87128727.7401
9772362.68979
54732028.4301
77535310.8179
31351232.446
10995501.6308
69451057.2991
143783714.866
30485542.2681
105159781.355
23194565.5726
35786150.3246
27332711.5639
134094442.218
14340119.8409
17507193.6843
27022010.6953
12854147.1172
392961548.455
54528054.9744
29197392.0591
57257365.2485
331582415.653
93377760.2707
450328203.673
1006505.56492
712168.909473
197311357.767
100031204.345
80662713.1363
5631669.86867
32560363.7544
7726593.96689
12928480.7806
95766387.1054
225353683.24
216249692.899
146415209.395
159994583.193
130863439.257
222807394.487
113859689.649
72220753.9479
138024833.392
271488874.942
80668391.853
57411375.2249
193147096.461
30030106.7106
49297208.3687
21911427.4376
194926183.147
118904809.965
74236291.6408
82031177.6522
52775325.4771
77538219.188
63610388.7613
111881.481978
111881.481978
54817.7187362
54817.7187362
191162.757371
191162.757371
2469.23608091
2469.23608091
30292.3762527
30292.3762527
84236.4453762
84236.4453762
399338.956044
399338.956044
2407149.56127
2407149.56127
403265.859271
403265.859271
162701.302628
162701.302628
53206.4928879
53206.4928879
48802.9405773
48802.9405773
38103.2697531
38103.2697531
125494.29116
125494.29116
26139.2112268
26139.2112268
244089.189505
244089.189505
1480341.58929
1480341.58929
1608538.21103
1608538.21103
>>> newlayer = ds2.CreateLayer('Romania2', filtered_lyr.GetSpatialRef(), filtered_lyr.GetGeomType())
>>> newlayer.CreateFields(filtered_lyr.schema)
>>> new_defn = filtered_lyr.GetLayerDefn()
>>> 

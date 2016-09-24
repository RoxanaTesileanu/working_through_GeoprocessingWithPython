Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from osgeo import gdal
>>> import numpy as np
>>> a= np.arange(12)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> a[1]
1
>>> a[1:5]
array([1, 2, 3, 4])
>>> a = np.reshape(a, (3,4))
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> a[2, 4]

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[2, 4]
IndexError: index 4 is out of bounds for axis 1 with size 4
>>> a[2,1]
9
>>> a[0,0]
0
>>> # ok, so it starts counting at 0,0. To access an element in 2nd row you have to type 3.
>>> a[3,3]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[3,3]
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> a[3,1]

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[3,1]
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> # no I mean to access an element in 2nd row you have to type 1.
>>> a[1, 2]
6
>>> a[2]
array([ 8,  9, 10, 11])
>>> a[:0]
array([], shape=(0, 4), dtype=int64)
>>> a[:1]
array([[0, 1, 2, 3]])
>>> a[:2]
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
>>> a[:,2]
array([ 2,  6, 10])
>>> a[:,0]
array([0, 4, 8])
>>> # so you need to type the comma to get the desired column!
>>> # if you leave out the comma, you get a two-dimensional slice.
>>> a[1:,1:3]
array([[ 5,  6],
       [ 9, 10]])
>>> a[2,:-1]
array([ 8,  9, 10])
>>> a = np.array([1,3,4], [2,7,6])

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a = np.array([1,3,4], [2,7,6])
TypeError: data type not understood
>>> a= np.array([[1,3,4], [2,7,6]])
>>> b= np.array([[5,2,9], [3,6,4]])
>>> a
array([[1, 3, 4],
       [2, 7, 6]])
>>> b
array([[5, 2, 9],
       [3, 6, 4]])
>>> a+b
array([[ 6,  5, 13],
       [ 5, 13, 10]])
>>> a>b
array([[False,  True, False],
       [False,  True,  True]], dtype=bool)
>>> # write a sort of if-else statement with the np.where() function.
>>> np.where(a>b, 10, 5)
array([[ 5, 10,  5],
       [ 5, 10, 10]])
>>> np.where(a>b, a, b)
array([[5, 3, 9],
       [3, 7, 6]])
>>> a= np.random.randint(0,20,12)
>>> a
array([ 7,  7,  2,  9, 19, 10, 17,  5, 18,  1, 14, 13])
>>> a[(8,0,3)]

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a[(8,0,3)]
IndexError: too many indices for array
>>> a[[8,0,4]]
array([18,  7, 19])
>>> # notice the double brackets
>>> a=np.reshape(a, (3,4))
>>> a
array([[ 7,  7,  2,  9],
       [19, 10, 17,  5],
       [18,  1, 14, 13]])
>>> a[[2,0,0], [0,0,3]]
array([18,  7,  9])
>>> b
array([[5, 2, 9],
       [3, 6, 4]])
>>> c=np.where(a>7, True, False)
>>> c
array([[False, False, False,  True],
       [ True,  True,  True, False],
       [ True, False,  True,  True]], dtype=bool)
>>> a[c]
array([ 9, 19, 10, 17, 18, 14, 13])
>>> # select elements of a that correspond to TRUE in c definition
>>> np.mean(a[c])
14.285714285714286
>>> 
KeyboardInterrupt
>>> 

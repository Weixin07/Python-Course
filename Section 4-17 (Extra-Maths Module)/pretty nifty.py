Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> round(1.5)
2
>>> round(2.1)
2
>>> import math
>>> round.floor(1.5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    round.floor(1.5)
AttributeError: 'builtin_function_or_method' object has no attribute 'floor'
>>> 
>>> math.floor(1.5)
1
>>> math.cell(2.1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    math.cell(2.1)
AttributeError: module 'math' has no attribute 'cell'
>>> math.ceil(2.1)
3
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.pi/math.e
1.1557273497909217
>>> math.sin(math.pi/2)
1.0
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> math.floor(math.sin(math.pi))
0
>>> math.cos(0)
1.0
>>> math.asin(0)
0.0
>>> math.acos(0)
1.5707963267948966
>>> math.hypot(3,4)
5.0
>>> math.hypot(5,12)
13.0
>>> math.hypot(12,13)
17.69180601295413
>>> math.isfinite(math.hypot(3,4))
True
>>> math.pow(2,3)
8.0
>>> 2**3
8
>>> math.pow(9,2)
81.0
>>> math.exp(2)
7.38905609893065
>>> math.log(math.e)
1.0
>>> math.log10(1000)
3.0
>>> 

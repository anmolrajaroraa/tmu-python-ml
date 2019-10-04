Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print
<built-in function print>
>>> print('hello')
hello
>>> a = 'hello'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'hello'
>>> bool('hello')
True
>>> bool('')
False
>>> int(True)
1
>>> int(False)
0
>>> str(True)
'True'
>>> str(False)
'False'
>>> str('10a')
'10a'
>>> str(10)
'10'
>>> int('hello')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
>>> int('10')
10
>>> True = 10
SyntaxError: can't assign to keyword
>>> 
>>> 
>>> a = 10
>>> b = 20
>>> c = a + b
>>> 
>>> 1290/35
36.857142857142854
>>> 1290//35
36
>>> #1290/35  ->   classic division
>>> #1290//35  - > floor division
>>> 
>>> 12 * 2
24
>>> 12 ** 2
144
>>> 12 ** 12
8916100448256
>>> 
>>> 
>>> 
>>> print("Sum of" + a "and" + b + "is" + c)
SyntaxError: invalid syntax
>>> print("Sum of" + str(a) "and" + str(b) + "is" + str(c))
SyntaxError: invalid syntax
>>> print("Sum of" + a + "and" + b + "is" + c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print("Sum of" + a + "and" + b + "is" + c)
TypeError: can only concatenate str (not "int") to str
>>> print("Sum of" + str(a) + "and" + str(b) + "is" + str(c))
Sum of10and20is30
>>> print("Sum of " + str(a) + " and " + str(b) + " is " + str(c))
Sum of 10 and 20 is 30
>>> 
>>> print("Sum of a and b is c")
Sum of a and b is c
>>> print("Sum of" + a + "and" + b + "is" + c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print("Sum of" + a + "and" + b + "is" + c)
TypeError: can only concatenate str (not "int") to str
>>> print("Sum of" , a , "and" , b , "is" , c)
Sum of 10 and 20 is 30
>>> print("Sum of %d and %d is %d")
Sum of %d and %d is %d
>>> print("Sum of %d and %d is %d"%(a,b,c))
Sum of 10 and 20 is 30
>>> 
>>> a = input("Enter first number: ")
Enter first number: 23
>>> a
'23'
>>> b = input("Enter second number: ")
Enter second number: 20
>>> b
'20'
>>> c = a + b
>>> print("Sum of %d and %d is %d"%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print("Sum of %d and %d is %d"%(a,b,c))
TypeError: %d format: a number is required, not str
>>> c
'2320'
>>> print("Sum of %s and %s is %s"%(a,b,c))
Sum of 23 and 20 is 2320
>>> c = int(a) + int(b)
>>> c
43
>>> a = int(input("Enter first number: "))
Enter first number: 1O
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a = int(input("Enter first number: "))
ValueError: invalid literal for int() with base 10: '1O'
>>> a = int(input("Enter first number: "))
Enter first number: 10
>>> type(a)
<class 'int'>
>>> print("Sum of {} and {} is {}")
Sum of {} and {} is {}
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 10 and 20 is 43
>>> 
>>> print("Sum of {a} and {b} is {c}")
Sum of {a} and {b} is {c}
>>> print(f"Sum of {a} and {b} is {c}")
Sum of 10 and 20 is 43
>>> #logical operators -> and (&&), or(||), not(!)
>>> 
>>> a = 10
>>> a + 1
11
>>> a
10
>>> a = a + 1
>>> a
11
>>> a += 1
>>> a
12
>>> a -= 1
>>> a
11
>>> a *= 10
>>> a
110
>>> a /= 10
>>> a
11.0
>>> a //= 10
>>> a
1.0
>>> a = 110
>>> a /= 10
>>> a
11.0
>>> a //=2
>>> a
5.0
>>> a /= 2
>>> a
2.5
>>> a **= 3
>>> a
15.625
>>> 
>>> 
>>> a = 10
>>> b = a
>>> b
10
>>> a == b
True
>>> a is b
True
>>> 
>>> 
>>> 
>>> a = 10
>>> b = 10
>>> a == b
True
>>> a is b
True
>>> 
>>> a = 1000000
>>> b = 1000000
>>> a is b
False
>>> a is not b
True
>>> 
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/python-basics.py ===
Enter first number: 12
Enter second number: 23
Sum of 12 and 23 is 35
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/python-basics.py ===
Enter first number: 12
Enter second number: 23
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/tmu-python-ml/python-basics.py", line 4, in <module>
    c = a + bb
NameError: name 'bb' is not defined
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/python-basics.py ===
Enter first number: 34
Enter second number: 32
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/tmu-python-ml/python-basics.py", line 6, in <module>
    print(f"Sum of {a} and {b} is {d}")
NameError: name 'd' is not defined
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/python-basics.py ===
Enter first number: 55
Enter second number: 77
Sum of 55 and 77 is 132
>>> 

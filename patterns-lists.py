Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
*
**
***
****
*****
'''
'\n*\n**\n***\n****\n*****\n'
>>> for i in range(10):
	for j in range(i + 1):
		print('*')

		
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> a = 10
>>> b = 20
>>> c = a + b
>>> print('Sum of', a, 'and', b, 'is', c)
Sum of 10 and 20 is 30
>>> print('Sum of', a, 'and', b, 'is', c,sep='$')
Sum of$10$and$20$is$30
>>> if True:
	print('Sum of', a,sep='$')
	print('and', b, 'is', c, sep='$')

	
Sum of$10
and$20$is$30
>>> if True:
	print('Sum of', a,sep='$',end='')
	print('and', b, 'is', c, sep='$')

	
Sum of$10and$20$is$30
>>> for i in range(10):
	for j in range(i + 1):
		print('*',end='')

		
*******************************************************
>>> for i in range(10):
	for j in range(i + 1):
		print('*',end='')
	print()

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> '''
    *
   **
  ***
 ****
*****
'''
'\n    *\n   **\n  ***\n ****\n*****\n'
>>> '''
    *
   ***
  *****
 *******
*********
'''
'\n    *\n   ***\n  *****\n *******\n*********\n'
>>> 
>>> 
>>> '''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    '''
'\n    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n    '
>>> '*' * 10
'**********'
>>> for i in range(10):
	print('*' * (i+1) )

*
**
***

****
*****
******
*******
********
*********
**********
>>> for i in range(10):
	print('*' * (i+1) )

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> for i in range(10):
	print(' ' * (9-i))
	print('*' * (i+1))

	
         
*
        
**
       
***
      
****
     
*****
    
******
   
*******
  
********
 
*********

**********
>>> for i in range(10):
	print(' ' * (9-i),end='')
	print('*' * (i+1))

	
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not35
Number is prime
Number is prime
Number is prime
Number is not prime
Number is prime
Number is not prime
Number is prime
Number is prime
Number is prime
Number is prime
Number is prime
Number is prime
Number is prime
Number is prime
Number is prime
Number is prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not35
Number is prime
Number is prime
Number is prime
Number is not prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not37
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not37
Number is prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not35
Number is not prime
Number is prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not35
Number is not prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not37
Number is prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not37
Number is prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not35
Number is not prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not35
Number is not prime
>>> 
=== RESTART: /Users/anmolrajarora/Documents/tmu-python-ml/prime-number.py ===
Enter a number to check if it's prime or not37
Number is prime
>>> 
>>> list1 = [1,2,3,4,5, 'hello', 'ram', True, False, [11,22,33,44,55], [77,88,99] ]
>>> len(list1)
11
>>> list1[0]
1
>>> list1[6]
'ram'
>>> list1[8]
False
>>> list1[10]
[77, 88, 99]
>>> 
>>> list1[0:]
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99]]
>>> list1[0:10]
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55]]
>>> 
>>> list1[10:0]
[]
>>> list1[10:0:-1]
[[77, 88, 99], [11, 22, 33, 44, 55], False, True, 'ram', 'hello', 5, 4, 3, 2]
>>> list1[10::-1]
[[77, 88, 99], [11, 22, 33, 44, 55], False, True, 'ram', 'hello', 5, 4, 3, 2, 1]
>>> 
>>> 
>>> 
>>> list1[9]
[11, 22, 33, 44, 55]
>>> list1[9][0:3]
[11, 22, 33]
>>> 
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> 
>>> 
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99]]
>>> list1.append(100)
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100]
>>> list1.append('shyam')
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam']
>>> list1.append(True,False)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    list1.append(True,False)
TypeError: append() takes exactly one argument (2 given)
>>> 
>>> 
>>> 
>>> for i in range(4):
	element = input("Enter the element to insert into list: ")
	list1.append(element)

	
Enter the element to insert into list: 
Enter the element to insert into list: 123
Enter the element to insert into list: 234
Enter the element to insert into list: 345
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345']
>>> 
>>> 
>>> list1.extend(['a', 'b', 'c', 'd'])
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd']
>>> 
>>> 
>>> list1.append(['a', 'b', 'c', 'd'])
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd']]
>>> 
>>> 
>>> 
>>> list1.append('python')
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 'python']
>>> list1.extend('python')
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> 
>>> list1.count(11)
0
>>> list1.count(1)
2
>>> list1.count(0)
1
>>> 
>>> list1.index(1)
0
>>> list1.rindex(1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    list1.rindex(1)
AttributeError: 'list' object has no attribute 'rindex'
>>> list1.index(1, 1)
7
>>> list1.insert(10, [1,2,3])
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [1, 2, 3], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> list1[10] = 'abcd'
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], 'abcd', [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> list1.insert(10, [1,2,3])
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [1, 2, 3], 'abcd', [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> 
>>> 
>>> list1.pop()
'n'
>>> list1.pop()
'o'
>>> list1.pop()
'h'
>>> list1.pop()
't'
>>> list1.pop()
'y'
>>> list1.pop()
'p'
>>> list1.pop()
'python'
>>> 
>>> list1.pop(10)
[1, 2, 3]
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], 'abcd', [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd']]
>>> list1.remove('abcd')
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd']]
>>> 
>>> list1.append(100)
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 100, 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 100]
>>> list1.remove(100)
>>> list1
[1, 2, 3, 4, 5, 'hello', 'ram', True, False, [11, 22, 33, 44, 55], [77, 88, 99], 'shyam', '', '123', '234', '345', 'a', 'b', 'c', 'd', ['a', 'b', 'c', 'd'], 100]
>>> list1.reverse()
>>> list1
[100, ['a', 'b', 'c', 'd'], 'd', 'c', 'b', 'a', '345', '234', '123', '', 'shyam', [77, 88, 99], [11, 22, 33, 44, 55], False, True, 'ram', 'hello', 5, 4, 3, 2, 1]
>>> 
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> 
>>> list2 = [62376,238823,238783,3838,93783]
>>> list2.sort()
>>> list2
[3838, 62376, 93783, 238783, 238823]
>>> list2.sort(reverse=True)
>>> list2
[238823, 238783, 93783, 62376, 3838]
>>> 
>>> list3 = [ [101,'Ram'], [103, 'Shyam'], [102, 'Mohan'] ]
>>> list3.sort()
>>> list3
[[101, 'Ram'], [102, 'Mohan'], [103, 'Shyam']]
>>> list3 = [ [101,'Ram'], [102, 'Shyam'], [102, 'Mohan'] ]
>>> list3.sort()
>>> list3
[[101, 'Ram'], [102, 'Mohan'], [102, 'Shyam']]
>>> list3 = [ [101,'Ram'], [102, 'Shyam'], [102, 'Mohan', 'Kumar'], [102, 'Mohan', 'Lal' ]]
>>> 
>>> list3
[[101, 'Ram'], [102, 'Shyam'], [102, 'Mohan', 'Kumar'], [102, 'Mohan', 'Lal']]
>>> list3.sort()
>>> list3
[[101, 'Ram'], [102, 'Mohan', 'Kumar'], [102, 'Mohan', 'Lal'], [102, 'Shyam']]
>>> 
>>> 
>>> 

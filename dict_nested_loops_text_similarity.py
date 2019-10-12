Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tic tac toe
>>> #fb replica
>>> #snake
>>> #pacman
>>> #ball game
>>> #chatbot
>>> a = 10
>>> b = 20
\
>>> diff = b - a
>>> a = 100
>>> b = 20
>>> diff = b - a
>>> diff
-80
>>> if a > b:
	diff = a - b
else:
	diff = b - a

	
>>> diff
80
>>> a = 10
>>> b = 20
>>> if a > b:
	diff = a - b
else:
	diff = b - a

	
>>> diff
10
>>> 
>>> diff = b - a if b > a
SyntaxError: invalid syntax
>>> diff = (b - a) if (b > a) else (a - b)
>>> diff
10
>>> a = 100
>>> b = 20
>>> diff = (b - a) if (b > a) else (a - b)
>>> diff
80
>>> diff = (b - a) if (b > a) else ((a - b) if a > b else 0)
>>> a = 10
>>> b = 10
>>> diff
80
>>> diff = (b - a) if (b > a) else ((a - b) if a > b else 0)
>>> diff
0
>>> diff = print('b is greater') if (b > a) else (print('a is greater') if a > b else print('Numbers equal'))
Numbers equal
>>> a = 100
>>> b = 20
>>> print('b is greater') if (b > a) else (print('a is greater') if a > b else print('Numbers equal'))
a is greater
>>> a = 10
>>> print('b is greater') if (b > a) else (print('a is greater') if a > b else print('Numbers equal'))
b is greater
>>> evenNumbers = []
>>> for i in range(101,2):
	if i % 2 == 0:
		evenNumbers.append(i)

		
>>> evenNumbers = []
>>> evenNumbers
[]
>>> for i in range(101,2):
	if i % 2 == 0:
		evenNumbers.append(i)

		
>>> evenNumbers
[]
>>> for i in range(101,2):
	evenNumbers.append(i)

	
>>> evenNumbers
[]
>>> list(range(101))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> list(range(101,2))
[]
>>> list(range(0,101,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

>>> for i in range(101):
	if i % 2 ==0 or i % 3 == 0:
		evenNumbers.append(i)

		
>>> evenNumbers
[0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 44, 45, 46, 48, 50, 51, 52, 54, 56, 57, 58, 60, 62, 63, 64, 66, 68, 69, 70, 72, 74, 75, 76, 78, 80, 81, 82, 84, 86, 87, 88, 90, 92, 93, 94, 96, 98, 99, 100]
>>> 
>>> #list comprehension
>>> newList = [i for i in range(101) if i % 2 ==0 or i % 3 == 0]
>>> newList
[0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 44, 45, 46, 48, 50, 51, 52, 54, 56, 57, 58, 60, 62, 63, 64, 66, 68, 69, 70, 72, 74, 75, 76, 78, 80, 81, 82, 84, 86, 87, 88, 90, 92, 93, 94, 96, 98, 99, 100]
>>> 
>>> # expression to append in list    for loop     if condition (optional)
>>> 
>>> newList = [i ** 2 for i in range(101) if i % 2 ==0 or i % 3 == 0]
>>> newList
[0, 4, 9, 16, 36, 64, 81, 100, 144, 196, 225, 256, 324, 400, 441, 484, 576, 676, 729, 784, 900, 1024, 1089, 1156, 1296, 1444, 1521, 1600, 1764, 1936, 2025, 2116, 2304, 2500, 2601, 2704, 2916, 3136, 3249, 3364, 3600, 3844, 3969, 4096, 4356, 4624, 4761, 4900, 5184, 5476, 5625, 5776, 6084, 6400, 6561, 6724, 7056, 7396, 7569, 7744, 8100, 8464, 8649, 8836, 9216, 9604, 9801, 10000]
>>> newList = [i ** 2 for i in range(101) if i % 2 ==0 or i % 3 == 0 else 0]
SyntaxError: invalid syntax
>>> newList = [  (i ** 2 if i % 2 == 0 or i% 3 ==0 else 0 ) for i in range(101)]
>>> 
>>> 
>>> for i in range(101)
SyntaxError: invalid syntax
>>> for i in range(101):
	if i % 2 == 0 or i% 3 ==0:
		list.append(i ** 2)
	else:
		list.append(0)

		
Traceback (most recent call last):

  File "<pyshell#84>", line 3, in <module>
    list.append(i ** 2)
TypeError: descriptor 'append' requires a 'list' object but received a 'int'
>>> 
>>> 
>>> 
>>> keys = ['id', 'name', 'contact', 'address']
>>> student = [None, 'Ram', ['1234', '4567'], {'temp' : 'a', 'perm' : 'b'}]
>>> list(zip(keys,student))
[('id', None), ('name', 'Ram'), ('contact', ['1234', '4567']), ('address', {'temp': 'a', 'perm': 'b'})]
>>> dict(zip(keys,student))
{'id': None, 'name': 'Ram', 'contact': ['1234', '4567'], 'address': {'temp': 'a', 'perm': 'b'}}
>>> 
>>> dict1 = {}
>>> for key,value in zip(keys,student):
	dict1[key] = value

	
>>> dict1
{'id': None, 'name': 'Ram', 'contact': ['1234', '4567'], 'address': {'temp': 'a', 'perm': 'b'}}
>>> 
>>> a = 10
>>> b = 20
>>> c = a + b
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 10 and 20 is 30
>>> 
>>> dict1
{'id': None, 'name': 'Ram', 'contact': ['1234', '4567'], 'address': {'temp': 'a', 'perm': 'b'}}
>>> print('Id : {}, Name : {}, Contact : {}, Address : {}'.format(dict1['id'], dict1['name'], dict1['contact'], dict1['address']))
Id : None, Name : Ram, Contact : ['1234', '4567'], Address : {'temp': 'a', 'perm': 'b'}
>>> print('Id : {}, Name : {}, Contact : {}, Address : {}'.format_map(dict1))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print('Id : {}, Name : {}, Contact : {}, Address : {}'.format_map(dict1))
ValueError: Format string contains positional fields
>>> 
>>> print('Id : {id}, Name : {name}, Contact : {contact}, Address : {address}'.format_map(dict1))
Id : None, Name : Ram, Contact : ['1234', '4567'], Address : {'temp': 'a', 'perm': 'b'}
>>> 
>>> list1 = [ 11,22,33, [99,88,77], ['Python', 'Java', 'JavaScript']]
>>> for item in list1:
	print(item)

	
11
22
33
[99, 88, 77]
['Python', 'Java', 'JavaScript']
>>> for item in list1:
	for inner_item in item:
		print(inner_item)

		
Traceback (most recent call last):
  File "<pyshell#118>", line 2, in <module>
    for inner_item in item:
TypeError: 'int' object is not iterable

>>> for item in list1:
	if type(item) == int:
		print(item)
		continue
	for inner_item in item:
		print(inner_item)

		
11
22
33
99
88
77
Python
Java
JavaScript
>>> for index in range(len(list1)):
	if type(index) == int:
		print(index)

		
0
1
2
3
4
>>> list1[0]
11
>>> for index in range(len(list1)):
	if type(list1[index]) == int:
		print(list1[index])

		
11
22
33
>>> for index in range(len(list1)):
	if type(list1[index]) == int:
		print(list1[index])
		continue
	for inner_index in range(len(list1[index])):
		print(list1[index][inner_index])

		
11
22
33
99
88
77
Python
Java
JavaScript
>>> 
>>> str1 = "Python is a general-purpose langauge. It has got many applications"
>>> str2 = "python is a programming language. It has got very easy syntax and can be used to develop many applications"
>>> 
>>> 
>>> #Text similarity using jaccard's distance
>>> 
>>> stopwords = ['is', 'a', 'it', 'has', 'got', 'and', 'can' , 'be', 'to']
>>> 
>>> #tokenization
>>> tokens_1 = str1.split()
>>> tokens_2 = str2.split()
>>> tokens_1
['Python', 'is', 'a', 'general-purpose', 'langauge.', 'It', 'has', 'got', 'many', 'applications']
>>> tokens_2
['python', 'is', 'a', 'programming', 'language.', 'It', 'has', 'got', 'very', 'easy', 'syntax', 'and', 'can', 'be', 'used', 'to', 'develop', 'many', 'applications']
>>> words_1 = [token.lowercase() for token in tokens_1  if token.lowercase() not in stopwords]
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    words_1 = [token.lowercase() for token in tokens_1  if token.lowercase() not in stopwords]
  File "<pyshell#148>", line 1, in <listcomp>
    words_1 = [token.lowercase() for token in tokens_1  if token.lowercase() not in stopwords]
AttributeError: 'str' object has no attribute 'lowercase'
>>> words_1 = [token.lower() for token in tokens_1  if token.lower() not in stopwords]
>>> 
>>> words_1
['python', 'general-purpose', 'langauge.', 'many', 'applications']
>>> words_1 = [token for token.lower() in tokens_1  if token not in stopwords]
SyntaxError: can't assign to function call
>>> words_2 = [token.lower() for token in tokens_2  if token.lower() not in stopwords]
>>> 
>>> words_2
['python', 'programming', 'language.', 'very', 'easy', 'syntax', 'used', 'develop', 'many', 'applications']
>>> 
>>> intersection = words_1.intersection(words_2)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    intersection = words_1.intersection(words_2)
AttributeError: 'list' object has no attribute 'intersection'
>>> intersection = set(words_1).intersection(set(words_2))
>>> intersection
{'applications', 'python', 'many'}
>>> union = set(words_1).union(set(words_2))
>>> union
{'syntax', 'applications', 'many', 'python', 'langauge.', 'easy', 'general-purpose', 'language.', 'very', 'used', 'develop', 'programming'}
>>> print(f"Text similarity is {len(intersection) / len(union) * 100}")
Text similarity is 25.0
>>> 

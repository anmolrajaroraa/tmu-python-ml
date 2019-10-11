Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1 = {'id' : 101, 'name' : 'Ram'}
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : '1234'
	}
>>> 
>>> student['name']
'Ram'
>>> student['contact']
'1234'

>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : [
		'1234',
		'4567'
		]
	}
>>> 
>>> student['contact']
['1234', '4567']
>>> student['contact'][0]
'1234'
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : [
		'1234',
		'4567'
		],
	'address' : 'new city'
	}
>>> 
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : [
		'1234',
		'4567'
		],
	'address' : [
		'city1',
		'city2'
	}
	
SyntaxError: invalid syntax
>>> 
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : [
		'1234',
		'4567'
		],
	'address' : [
		'city1',
		'city2'
		]
	}
>>> 
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : {
		'student_no' : '1234',
		'father_no' : '4567',
		'landline' : '9876'
		}
	'address' : [
		'city1',
		'city2'
		]
	}
SyntaxError: invalid syntax
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'contact' : {
		'student_no' : '1234',
		'father_no' : '4567',
		'landline' : '9876'
		},
	'address' : [
		'city1',
		'city2'
		]
	}
>>> 
>>> student['contact']
{'student_no': '1234', 'father_no': '4567', 'landline': '9876'}
>>> student['contact']['student_no']
'1234'
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> student.get('name')
'Ram'
>>> student.items()
dict_items([('id', 101), ('name', 'Ram'), ('contact', {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}), ('address', ['city1', 'city2'])])
>>> dict_items([('id', 101), ('name', 'Ram'), ('contact', {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}), ('address', ['city1', 'city2'])])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict_items([('id', 101), ('name', 'Ram'), ('contact', {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}), ('address', ['city1', 'city2'])])
NameError: name 'dict_items' is not defined
>>> 
>>> 
>>> for key,value in student.items():
	print(key + " : " + value)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(key + " : " + value)
TypeError: can only concatenate str (not "int") to str
>>> for key,value in student.items():
	print(key , ":" , value)

	
id : 101
name : Ram
contact : {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}
address : ['city1', 'city2']
>>> 
>>> student.keys()
dict_keys(['id', 'name', 'contact', 'address'])
>>> student.values()
dict_values([101, 'Ram', {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}, ['city1', 'city2']])
>>> 
>>> 
>>> 
>>> for key in student.keys():
	print(student[key])

	
101
Ram
{'student_no': '1234', 'father_no': '4567', 'landline': '9876'}
['city1', 'city2']
>>> student.pop('id')
101
>>> student.popitem()
('address', ['city1', 'city2'])
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
>>> student.setdefault('course', 'abc')
'abc'
>>> student.setdefault('course', 'def')
'abc'
>>> student
{'name': 'Ram', 'contact': {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}, 'course': 'abc'}
>>> marks = {
	'c' : 76,
	'c++' : 56,
	'python' : 100
	}
>>> 
>>> student.update(marks)
>>> student
{'name': 'Ram', 'contact': {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}, 'course': 'abc', 'c': 76, 'c++': 56, 'python': 100}
>>> 
>>> student.setdefault('marks', marks)
{'c': 76, 'c++': 56, 'python': 100}
>>> student
{'name': 'Ram', 'contact': {'student_no': '1234', 'father_no': '4567', 'landline': '9876'}, 'course': 'abc', 'c': 76, 'c++': 56, 'python': 100, 'marks': {'c': 76, 'c++': 56, 'python': 100}}
>>> 
>>> 
>>> dict.fromkeys(['id', 'name', 'city', 'isDisabled'], None)
{'id': None, 'name': None, 'city': None, 'isDisabled': None}
>>> dict.fromkeys(['id', 'name', 'city', 'isDisabled'])
{'id': None, 'name': None, 'city': None, 'isDisabled': None}
>>> newStudentdict.fromkeys(['id', 'name', 'city', 'isDisabled'])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    newStudentdict.fromkeys(['id', 'name', 'city', 'isDisabled'])
NameError: name 'newStudentdict' is not defined
>>> newStudent = dict.fromkeys(['id', 'name', 'city', 'isDisabled'])
>>> newStudent
{'id': None, 'name': None, 'city': None, 'isDisabled': None}
>>> newStudent = dict.fromkeys(['id', 'name', 'city', 'isDisabled'], [1,2,3,4])
>>> newStudent
{'id': [1, 2, 3, 4], 'name': [1, 2, 3, 4], 'city': [1, 2, 3, 4], 'isDisabled': [1, 2, 3, 4]}
>>> 

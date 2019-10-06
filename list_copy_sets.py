Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3,4,5,'hello', [11,22,33,44,55], ['python', 'java', 'javascript']]
>>> list1
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java', 'javascript']]
>>> list2 = list1
>>> list2
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java', 'javascript']]
>>> list1.append('new')
>>> list1
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java', 'javascript'], 'new']
>>> list2
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java', 'javascript'], 'new']
>>> list1 is list2
True
>>> list3 = list1.copy()
>>> list3 is list1
False
>>> 
>>> 
>>> 
>>> list3[6]
[11, 22, 33, 44, 55]
>>> list3[6] is list1[6]
True
>>> 
>>> 
>>> list3.append('old')
>>> list3
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java', 'javascript'], 'new', 'old']
>>> list1
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java', 'javascript'], 'new']
>>> list1[6].append(66)
>>> list1
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55, 66], ['python', 'java', 'javascript'], 'new']
>>> list3
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55, 66], ['python', 'java', 'javascript'], 'new', 'old']
>>> 
>>> 
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> 
>>> list4 is list1
False
>>> list4[6] is list1[6]
False
>>> 
>>> 
>>> list4.pop()
'new'
>>> list4[6].pop()
66
>>> list4[7].pop()
'javascript'
>>> list4
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java']]
>>> list1
[1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55, 66], ['python', 'java', 'javascript'], 'new']
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> tuple1 = (1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55], ['python', 'java'])
>>> tuple1[0]
1
>>> tuple1[-1]
['python', 'java']
>>> tuple1[-1] = 100
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tuple1[-1] = 100
TypeError: 'tuple' object does not support item assignment
>>> tuple1[6]
[11, 22, 33, 44, 55]
>>> tuple1[6].append(66)
>>> tuple1
(1, 2, 3, 4, 5, 'hello', [11, 22, 33, 44, 55, 66], ['python', 'java'])
>>> hex(id(tuple1))
'0x107857128'
>>> tuple1[6].append(77)
>>> hex(id(tuple1))
'0x107857128'
>>> hex(id(tuple1[6]))
'0x104ee5d08'
>>> tuple1[6].append(88)
>>> '0x104ee5d08'
'0x104ee5d08'
>>> hex(id(tuple1[6]))
'0x104ee5d08'
>>> 
>>> 
>>> tuple1 = (1, 2, 3, 4, 5, 'hello', 0x6372828, ['python', 'java'])
>>> tuple1[5]
'hello'
>>> tuple1[5][0] = 'a'
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tuple1[5][0] = 'a'
TypeError: 'str' object does not support item assignment
>>> tuple1[6].clear()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tuple1[6].clear()
AttributeError: 'int' object has no attribute 'clear'
>>> tuple1 = (1, 2, 3, 4, 5, 'hello', [11,22,33,44,55], ['python', 'java'])
>>> tuple1[6].clear()
>>> tuple1
(1, 2, 3, 4, 5, 'hello', [], ['python', 'java'])
>>> 
>>> 
>>> set1 = {1, 2, 3, 4, 5, 'hello', [11,22,33,44,55], ['python', 'java']}
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    set1 = {1, 2, 3, 4, 5, 'hello', [11,22,33,44,55], ['python', 'java']}
TypeError: unhashable type: 'list'
>>> set1 = {1, 2, 3, 4, 5, 'hello', 11,22,33,44,55, 'python', 'java', True}
>>> set1
{1, 2, 3, 4, 5, 33, 'hello', 11, 44, 'java', 'python', 22, 55}
>>> set1[0]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    set1[0]
TypeError: 'set' object is not subscriptable
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set1.add(100)
>>> set1
{1, 2, 3, 4, 5, 33, 100, 'hello', 11, 44, 'java', 'python', 22, 55}
>>> 
>>> set2 = {1,3,5,100,11,'java',22}
>>> set1.difference(set2)
{33, 2, 4, 'hello', 44, 'python', 55}
>>> set2.difference(set1)
set()
>>> 
>>> set1 - set2
{33, 2, 4, 'hello', 44, 'python', 55}
>>> set2 - set1
set()
>>> 
>>> set1
{1, 2, 3, 4, 5, 33, 100, 'hello', 11, 44, 'java', 'python', 22, 55}
>>> set1.difference_update(set2)
>>> set1
{2, 4, 33, 'hello', 44, 'python', 55}
>>> help(set)
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
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
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
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
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
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

>>> set1
{2, 4, 33, 'hello', 44, 'python', 55}
>>> set1.add(55)
>>> set1
{2, 4, 33, 'hello', 44, 'python', 55}
>>> set3 = {1,2,3,4,5}
>>> set2 = {1,3,5,100,11,'java',22}
>>> set1 = {1, 2, 3, 4, 5, 'hello', 11,22,33,44,55, 'python', 'java', True}
>>> set1.difference(set2,set3)
{33, 'hello', 44, 'python', 55}
>>> set1.discard(55)
>>> set1
{1, 2, 3, 4, 5, 33, 'hello', 11, 44, 'java', 'python', 22}
>>> set1.discard(55)
>>> set1
{1, 2, 3, 4, 5, 33, 'hello', 11, 44, 'java', 'python', 22}
>>> set1.pop()
1
>>> set1.pop()
2
>>> set1.pop()
3
>>> set1.pop()
4
>>> set1.pop()
5
>>> set1.pop()
33
>>> set1.pop()
'hello'
>>> set1.pop()
11
>>> set1.intersection(set2,set3)
set()
>>> set1.intersection(set2)
{'java', 22}
>>> set1.union(set2,set3)
{1, 2, 3, 100, 5, 4, 11, 44, 'java', 'python', 22}
>>> set1.union(set2)
{1, 3, 100, 5, 11, 44, 'java', 'python', 22}
>>> set1 - set2
{'python', 44}
>>> set2 - set1
{1, 3, 100, 5, 11}
>>> set1.symmetric_difference(set2)
{1, 3, 5, 11, 'python', 100, 44}
>>> 

>>> set1.isdisjoint(set2,set3)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    set1.isdisjoint(set2,set3)
TypeError: isdisjoint() takes exactly one argument (2 given)
>>> set1.isdisjoint(set2)
False
>>> set4 = set1
>>> set1.isdisjoint(set4)
False
>>> set5 = {}
>>> set1.isdisjoint(set5)
True
>>> set1.issuperset(set2)
False
>>> set1
{44, 'java', 'python', 22}
>>> set2
{1, 3, 100, 5, 11, 'java', 22}
>>> set9 = {1,3,100}
>>> set2.isusperset(set9)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    set2.isusperset(set9)
AttributeError: 'set' object has no attribute 'isusperset'
>>> set2.isuperset(set9)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    set2.isuperset(set9)
AttributeError: 'set' object has no attribute 'isuperset'
>>> set2.issuperset(set9)
True
>>> set9.issubset(set2)
True
>>> 

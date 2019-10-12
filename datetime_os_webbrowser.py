Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 10, 1, 18, 1, 57, 314887)
>>> print(datetime.datetime.now())
2019-10-01 18:02:12.404945
>>> 
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 10, 1, 18, 2, 52, 156574)
>>> date.today()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    date.today()
NameError: name 'date' is not defined
>>> datetime.date.today()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    datetime.date.today()
AttributeError: 'method_descriptor' object has no attribute 'today'
>>> 
>>> from datetime import *
>>> date.today()
datetime.date(2019, 10, 1)
>>> print(date.today())
2019-10-01
>>> 
>>> today = date.today()
>>> print(f"{today.day}")
1
>>> print(f"{today.day}/{today.month}/{today.year}")
1/10/2019
>>> 
>>> 
>>> now = datetime.now()
>>> type(now)
<class 'datetime.datetime'>
>>> type(today)
<class 'datetime.date'>
>>> now.strftime('%y')
'19'
>>> now.strftime('%Y')
'2019'
>>> now.strftime('%a')
'Tue'
>>> now.strftime('%A')
'Tuesday'
>>> now.strftime('%b')
'Oct'
>>> now.strftime('%B')
'October'
>>> now.strftime('%c')
'Tue Oct  1 18:08:48 2019'
>>> 
>>> now.strftime('%d')
'01'
>>> now.strftime('%D')
'10/01/19'
>>> now.strftime('%p')
'PM'
>>> now.strftime('%a %d %b %Y %H:%M:%S %p')
'Tue 01 Oct 2019 18:08:48 PM'
>>> 'Tue 01 Oct 2019 18:08:48 PM'
'Tue 01 Oct 2019 18:08:48 PM'
>>> 
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()
'/Users/anmolrajarora/Documents'
>>> os.chdir('/Users/anmolrajarora/Documents/python')
>>> os.getcwd()
'/Users/anmolrajarora/Documents/python'
>>> os.listdir()
['01-PythonIntroduction.wmv', 'PythonPygame_2.wmv', '.DS_Store', 'PythonPygame_!.wmv', '01-Python.wmv', 'PythonFunctionsIntro_1.wmv', 'PythonFunctions_2.wmv', 'PythonFilterMapLambda.wmv', 'PythonFunctionsIntro.wmv', 'Crawling_2.wmv', 'PythonIfElse.wmv', 'Crawling_1.wmv', 'Python_IfElse+List.wmv']
>>> 
>>> import random
>>> songs = os.listdir()
>>> song = random.choice(songs)
>>> song
'PythonFunctions_2.wmv'
>>> song = random.choice(songs)
>>> song
'01-Python.wmv'
>>> song = random.choice(songs)
>>> song
'PythonPygame_2.wmv'
>>> #os.startfile(song)   for windows
>>> os.chdir('C:\')
	 
SyntaxError: EOL while scanning string literal
>>> #os.chdir('C:\\Users\\username\\Music')  for windows
>>> 
>>> 
>>> import subprocess
>>> subprocess.call(['open', song])
0

>>> song = random.choice(songs)
>>> subprocess.call(['open', song])
0
>>> os.chdir('/Users/anmolrajarora/Documents/python-reg-sept')
>>> songs = os.listdir()
>>> song = random.choice(songs)
>>> subprocess.call(['open', song])
0
>>> 
>>> import webbrowser
>>> webbrowser.open('google.com')
True
>>> webbrowser.open('https://google.com')
True
>>> webbrowser.open('http://google.com')
True
>>> webbrowser.open('http://flipkart.com')
True
>>> subprocess.call(['open', '/Applications/TextEdit.exe'])
1
>>> subprocess.call(['open', '/Applications/TextEdit'])
1
>>> subprocess.call(['open', 'Applications/TextEdit'])
1
>>> subprocess.call(['open', 'Applications/TextEdit.app'])
1
>>> subprocess.call(['open', 'Applications/Notes.exe'])
1
>>> subprocess.call(['open', '/Applications/TextEdit.app'])
0
>>> subprocess.call(['open', '/Applications/Notes.app'])
0
>>> #os.open('notepad')

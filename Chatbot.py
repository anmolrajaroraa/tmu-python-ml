#   anmolarora1711@gmail.com

from datetime import *
# import datetime
import os, random, subprocess, webbrowser
# datetime.date()
# date.today()
#time.now()

helloIntent = ['hi', 'hello', 'namaste', 'bonjour']
timeIntent = ['what\'s the time', 'time please', 'tell me the current time']
dateIntent = ['what\'s the date today', 'date please', 'tell me today\'s date']
musicIntent = ['play a song', 'play some song for me', 'play a random song']
apps = ['calc', 'notepad', 'python']

while True:

    message = input( "Enter your message: " )

    if message in helloIntent:
        print('hello')

    elif message == 'how are you' or message == 'how you doin?':
        print('i am great, what about you?')

    elif message == 'i am also fine':
        print('sounds good')

    elif message in timeIntent:
        now = datetime.now( )
        print(now.strftime( '%a %d %b %Y %H:%M:%S %p' ))

    elif message in dateIntent:
        today = date.today( )
        print(f"{today.day}/{today.month}/{today.year}" )

    elif message in musicIntent:
        #os.chdir('/Users/anmolrajarora/Documents/python' )
        os.chdir('C:\\Users\\Ram\\Music')   #change directory
        songs = os.listdir( )
        song = random.choice( songs )
        os.startfile(song)
        #subprocess.call( [ 'open' , song ] )

    elif message.startswith("open"):
        websiteName = message.partition(' ')[-1]
        webbrowser.open(f"https://{websiteName}.com")

    elif message.startswith('run'):
        appName = message.partition( ' ' )[-1]
        #subprocess.call( [ 'open' ,'/Applications/' + appName + '.app' ] )  #for mac
        path = input('Please enter complete path till application')
        #path = C:\\users\\username\\Downloads\\vlc.exe
        os.startfile(path)     #for windows

    elif message == 'bye':
        print('Bye!')
        break

    else:
        print('I don\'t understand :( ')
        
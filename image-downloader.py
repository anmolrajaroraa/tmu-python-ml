from urllib.request import *
from bs4 import BeautifulSoup as bs

#urlretrieve('https://a2.espncdn.com/combiner/i?img=%2Fi%2Fcricket%2Fcricinfo%2F1141591_1296x518.jpg&w=628&h=251&scale=crop&cquality=80&location=center&format=jpg', 'img_1.jpg')

response = urlopen('https://www.espncricinfo.com/')

html = bs(response, 'lxml')

images = html.find_all('img')

imageSrcs = []

for image in images:
    if str(image).count(' src') == 1:
        #print(image['src'])
        imageSrcs.append(image['src'])
    elif str(image).count('data-default-src') == 1:
        #print(image['data-default-src'])
        imageSrcs.append(image['data-default-src'])

for i in range(len(imageSrcs)):
    urlretrieve(imageSrcs[i], 'espncric/img_{}.{}'.format(i+1, imageSrcs[i].rpartition('.')[-1][0:3]))

    '''str1 = "https://a3.espncdn.com/combiner/i?img=%2Fredesign%2Fassets%2Fimg%2Ficons%2FESPN-icon-cricket-ball-international-001.png&w=60&h=60&scale=crop&cquality=80&location=origin"
>>> str1.partition('.')
('https://a3', '.', 'espncdn.com/combiner/i?img=%2Fredesign%2Fassets%2Fimg%2Ficons%2FESPN-icon-cricket-ball-international-001.png&w=60&h=60&scale=crop&cquality=80&location=origin')
>>> str1.rpartition('.')
('https://a3.espncdn.com/combiner/i?img=%2Fredesign%2Fassets%2Fimg%2Ficons%2FESPN-icon-cricket-ball-international-001', '.', 'png&w=60&h=60&scale=crop&cquality=80&location=origin')
>>> str1.rpartition('.')[-1]
'png&w=60&h=60&scale=crop&cquality=80&location=origin'
>>> str1.rpartition('.')[-1][0:3]
'png'''
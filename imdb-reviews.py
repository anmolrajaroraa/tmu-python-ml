import urllib.request as req
import bs4

movie = input("Enter the name of the movie: ")

response = req.urlopen('https://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=all')

page = bs4.BeautifulSoup(response, 'lxml')

td = page.find('td', class_='result_text')

a = td.find('a')

print(a['href'])

newUrl = 'https://imdb.com' + a['href']

response = req.urlopen(newUrl)

html = bs4.BeautifulSoup(response, 'lxml')

div = html.find('div', class_='ratingValue')

print(div.find('span').text)

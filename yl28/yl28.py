from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/"

req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, features="html.parser")

i = 1

movieList = soup.findAll('div', attrs={'class': 'row countdown-item'})

print(movieList)
for div_item in movieList:
    div = div_item.find('div', attrs={'class': 'article_movie_title'}).find('h2')

    title = div.find('a').contents[0]
    year = div.find('span', attrs={'class' : 'subtle start-year'}).contents[0]
    print(str(i) + '.', title, year)
    i += 1
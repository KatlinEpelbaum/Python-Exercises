import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

url = "http://www.imdb.com/search/title?release_date="
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)

    
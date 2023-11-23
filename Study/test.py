import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=윤하'
res = requests.get(url).content.decode()
soup = BeautifulSoup(res, 'html.parser')

imgs = soup.findAll('img', class_='_img')
print(imgs)
for img in imgs:
	print(img.get('data-source'))
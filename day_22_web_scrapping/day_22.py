import requests
from bs4 import BeautifulSoup as bf

url = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
status = response.status_code
print(status)

content = response.content # we get all the content from the website
soup = bf(content, 'html.parser') # beautiful soup will give a chance to parse

print(soup.title)
print(soup.title.get_text())
# print(soup.body) # devuelve todo el body

footer = soup.find_all('tables')
print(footer)

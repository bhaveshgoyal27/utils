from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession 
 

url = 'https://www.youtube.com/watch?v=LMgNKkIp2c8&list=RDGMEM916WJxafRUGgOvd6dVJkeQ&start_radio=1'

session = HTMLSession()
# get the html content
response = session.get(url)
# execute Java-script
print("vchj")
response.html.render(sleep=1)
print("2")
soup = BeautifulSoup(response.html.html, "html.parser")
#file1 = open('myfile.html', 'w')
#file1.write(soup.text[:209400])
#file1.close()
domain = 'https://www.youtube.com'
i=0
for link in soup.find_all("a", {"dir": "ltr"}):
    print("b")
    href = link.get('href')
    print(href)
    if href.startswith('/watch?'):
        print(link.string.strip())
        print(domain + href + '\n')
        i+=1
    if i==35:
        break

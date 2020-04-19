from bs4 import BeautifulSoup
import requests
global var1
answer = input('enter selected youtbers homepage url: ')
results = requests.get(answer)
if int(results.status_code) == 200:
    print(results.status_code)
    print('connection made')
else:
    print(results.status_code)
    print('error')
    
soup = BeautifulSoup(results.content, 'html.parser')
soup = str(soup)

a, b =  '''yt-sprite"></span></span></button><span aria-label="''' , '''subscribers"'''
print(soup[soup.find(a)+ len(a):soup.find(b)] , 'subscribers')

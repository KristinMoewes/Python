# import HTMLSession from requests_html
from requests_html import HTMLSession
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
 
# create an HTML Session object
session = HTMLSession()
 
# Use the object above to connect to needed webpage
resp = session.get("https://play.google.com/store/apps/details?id=com.fluffyfairygames.idleminertycoon&gl=DE&showAllReviews=true")
 
# Run JavaScript code on webpage
data=resp.html.render()
time.sleep(5)  
soup = BeautifulSoup(data, "html.parser")

text=soup.find_all('div', attrs={'class':'UD7Dzf'})
print(text)
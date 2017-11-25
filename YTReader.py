#YT Subscription Reader
#Author: Julius Ahenkora
#Version: 0.0.0.1

from bs4 import BeautifulSoup

with open("YouTube.html") as fp:
    soup = BeautifulSoup(fp,"lxml")

#soup = BeautifulSoup("<html>data</html>","lxml")
print(soup.prettify())
print(soup.findall("script"))

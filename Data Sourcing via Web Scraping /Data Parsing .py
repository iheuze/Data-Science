from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
#%%
with urllib.request.urlopen('https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html') as response:
    html = response.read()
#%%
soup = BeautifulSoup(html, 'lxml')
print(type(soup))
#%%
# parsing data
print(soup.prettify()[0:100])
#%%
#getting data from a parse tree
text_only = soup.get_text()
print(text_only)
#%%
# searching and retrieving data from a parse tree
#filter by name
print(soup.find_all("li"))
#%%
# by key word
print(soup.find_all(id="link 7"))
#%%
#string arguments
print(soup.find_all('ol'))
#%%
# list objects
print(soup.find_all(['ol', 'b']))
#%%
# regular expression
t = re.compile("t")
for tag in soup.find_all(t):
    print(tag.name)
#%%
# boolean value
for tag in soup.find_all(True):
    print(tag.name)
#%%
# web links with string objects
for link in soup.find_all('a'):
    print(link.get('href', ))
#%%
# strings with regular expressions
print(soup.find_all(string = re.compile("data")))

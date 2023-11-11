import sys
print(sys.version)
from bs4 import BeautifulSoup
#%%
our_html_document = “   ”
#%%
our_soup_object = BeautifulSoup(our_html_document, 'html.parser')
print(our_soup_object)
#%%
print(our_soup_object.prettify()[0:300])
#%%
soup_object = BeautifulSoup('<h1 attribute_1 = "Heading Level 1" ">Future Trends for IoT in 2018</h1>', "lxml")
tag = soup_object.h1
print(type(tag))
#%%
print(tag)
print(tag.name)
#%%
tag.name = "heading 1"
print(tag)
print(tag.name)
#%%
# tag attributes
soup_object = BeautifulSoup('<h1 attribute_1 = "Heading Level 1" ">Future Trends for IoT in 2018</h1>', "lxml")
tag = soup_object.h1
print(tag)
print(tag['attribute_1'])
#%%
print(tag.attrs)
#%%
tag['attribute_2'] = "Heading Level 1"
print(tag.attrs)
#%%
del tag['attribute_2']
print(tag)
#%%
del tag['attribute_1']
print(tag.attrs)
#%%
print(our_soup_object.head)
#%%
print(our_soup_object.title)
#%%
print(our_soup_object.body.b)

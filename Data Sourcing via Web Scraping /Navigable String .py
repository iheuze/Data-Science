from bs4 import BeautifulSoup
#%%
our_html_document = our_html_document = “ ”
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
print(tag.string)
#%%
our_nav_string = tag.string
print(our_nav_string)
#%%
our_nav_string.replace_with('NaN')
print(tag.string)
#%%
for string in our_soup_object.stripped_strings:
    print(repr(string))
#%%
first_link = our_soup_object.a
print(first_link)
print(first_link.parent)
print(first_link.string)
print(first_link.string.parent)

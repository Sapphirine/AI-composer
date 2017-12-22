
# coding: utf-8

# In[2]:

import mechanize
from time import sleep
#Make a Browser (think of this as chrome or firefox etc)
br = mechanize.Browser()

# Open your site
br.open("https://vgmusic.com/updates/")

f=open("source.html","w")
f.write(br.response().read()) #can be helpful for debugging maybe

filetypes=[".mid"] #you will need to do some kind of pattern matching on your files
myfiles=[]
for l in br.links(): 
    for t in filetypes:
        if t in str(l): 
            myfiles.append(l)
            


# In[24]:


def downloadlink(l):
    if len(l.text)>10:
    l.text=l.text[0:10]
    name = l.text+'.mid'
    br.retrieve(l.url,name)
    #f.write(br.response().read())
    print l.text," has been downloaded"
    #br.back()

from ipywidgets import FloatProgress
from IPython.display import display
f = FloatProgress(min=0, max=len(myfiles))
display(f)
for l in myfiles:
    f.value+=1
    sleep(1) #throttle so you dont hammer the site
    downloadlink(l)


# In[ ]:




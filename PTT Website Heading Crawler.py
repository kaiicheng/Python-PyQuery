#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from pyquery import PyQuery as pq


# In[2]:


cookies = {"over18": "1"}
res = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html",                    cookies = cookies)


# In[3]:


mainPageDoc = pq(res.text)


# In[4]:


for i in range(10):
    #mainPageDoc("#main-container div > div.title > a").text()
    for each in mainPageDoc("#main-container div > div.title > a").items():
        print(each.text(), each.parent().siblings(".meta>.author").text())

    mainPageDoc.make_links_absolute(base_url=res.url)
    res = requests.get(mainPageDoc("#action-bar-container > div > div.btn-group.btn-group-paging \
            > a:nth-child(2)").attr("href"), cookies = cookies)
    #print(res.text)
    mainPageDoc = pq(res.text)


# In[ ]:





# In[ ]:





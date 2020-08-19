#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from pyquery import PyQuery as pq


# In[2]:


homeRes = requests.get("https://tw.buy.yahoo.com/sitemap/category-list")   # request"s"
homeDoc = pq(homeRes.text)   # No need to use ()


# In[3]:


# homeDoc(".level3Wrapper> .level3TitleWrapper > a.level3Title")


# In[4]:


# homeDoc(".level3Wrapper> .level3TitleWrapper > a.level3Title").text()


# In[5]:


print(homeDoc(".level3Wrapper> .level3TitleWrapper > a.level3Title"))


# In[6]:


# 1:08:35
dataList = []
cateList = homeDoc(".level3Wrapper> .level3TitleWrapper > a.level3Title")
for eachCateDoc in cateList.items():   # item"s"
    # part 1
    # Print out all catregory of products.
    print(eachCateDoc.attr("href"))
    cateRes = requests.get(eachCateDoc.attr("href"))   # request"s
    cateDoc = pq(cateRes.text)
    # part 2 
    pg = 1
    nextPgDoc = cateDoc
    while True:    # for i in range(10):
        itemLi = nextPgDoc(".pageFlex>.main>div:nth-child(1)>.gridList>li")
        # print(len(itemLi), cateRes.url + "?pq={}".format(pg))
        
        for eachItemDoc in itemLi.items():
            dataDict={}
            dataDict["title"] = eachItemDoc("a>span>span:nth-child(1)").text()
            if eachItemDoc("a>span>em").text():
                dataDict["price"] = eachItemDoc("a>span>em").text()
            else:
                dataDict["price"] = eachItemDoc("a>span>span:nth-child(2)>em").text()
            dataList.append(dataDict)
        pg+=1
        if len(itemLi)==0:
            break
        nextPgRes = requests.get(cateRes.url + "?pq={}".format(pg))   # request"s"
        nextPgDoc = pq(nextPgRes.text)
    #        print(eachItemDoc("a>span>em").text())
        


# In[ ]:


dataList


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





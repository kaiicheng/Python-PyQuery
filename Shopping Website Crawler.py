#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyquery


# In[2]:


import requests
from pyquery import PyQuery as pq


# In[3]:


response = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
doc = pq(response.text)


# In[4]:


# doc("body > div.wrapper > div.container.test-site > div > div.col-md-9 > div.row > div > div > div.caption > h4:nth-child(2) > a").text()


# In[5]:


# div p =>空格: 子孫選擇器，以下的全選
# div > p =>孩子選擇器，只選下一層的
# div+p = 緊接在div後為p者 => 選擇所有p，他前⼀個是div
# div~p = 在div後為p者 => 選擇所有p，他前⾯有div


# In[6]:


# * 代表任意元素 => 選擇 任意元素
# 例如: body * = 選擇 body 的⼦孫們
# 例如: body>* = 選擇 body 的孩⼦們


# In[7]:


# 老N 選擇器:nth-child(數字)
# 倒著數老N 選擇器:nth-last-child(數字)
# tr: nth-child(3) => 選擇每個標籤裡的第3個孩⼦，⽽且是tr


# In[8]:


# 找奇數 => nth-child(2n)
# 找偶數 => nth-child(2n+1)


# In[9]:


################## history  =>找出之前的所有輸入   #########################


# In[10]:


#side-menu > li:nth-child(2) > a

#side-menu > li:nth-child(3) > a

#side-menu > li:nth-child(???) > a
#side-menu > li:nth-child(n+2) > a


# In[11]:


# doc("#side-menu > li:nth-child(n+2) > a")


# In[12]:


# doc("#side-menu > li:nth-child(n+2) > a").text()


# In[13]:


# <div class="col-sm-4 col-lg-4 col-md-4"> => 空格代表不同的class


# In[14]:


dataList = []
doc.make_links_absolute(base_url = response.url)   # 自動加上開頭domain網址
for eachMainDoc in doc("#side-menu > li:nth-child(n+2) > a").items():  
    # 因為 doc("...")並非Python 8+1種資料型態 => 加上items
    # print("https://webscraper.io/" + eachMainDoc.attr("href"))   # 手動加上
    # print(eachMainDoc.attr("href"))
    mainRes = requests.get(eachMainDoc.attr("href"))   # 原本是首頁網址 => 改成新爬出的網址
    mainDoc = pq(mainRes.text)   # Misspell
    mainDoc.make_links_absolute(base_url = mainRes.url)
    for eachSubDoc in mainDoc("#side-menu > li.active > ul > li > a").items():
        # 儲存到dict
        print(eachSubDoc.attr("href"))
        subRes = requests.get(eachSubDoc.attr("href"))   # eachSubDoc => Not eachMainDoc
        subDoc = pq(subRes.text)
        # lEVEL 2
        for eachItem in subDoc(".test-site .thumbnail").items():   # 找出test-site 底下所有的thumbnail
            dataDict = {}
            dataDict["title"] = eachItem("h4>.title").text()
            dataDict["price"] = eachItem("h4.price").text()
            # dataDict["stars"] = len(eachItem("span.glyphicon-star"))
            dataDict["stars"] = len(eachItem("span.glyphicon-star"))
            dataList.append(dataDict)
            
            """
            # 出發點已經是thumbnail，若開頭是最頂(更上層的)的body則無法用
            print(eachItem("h4>.title").text())
            print(eachItem("h4.price").text())   # 沒有放空白
            # 找星星 => 方法 1. 選取星星，然後數數量
            # print(len(eachItem("span.glyphicon-star")))
            # 找星星 => 方法 2.
            print((eachItem("ratings>p:nth-child(2)").attr("data-rating")))
            """


# In[15]:


dataList


# In[31]:


dataList[2]["title"]


# In[29]:


dataList[2]["price"]


# In[30]:


dataList[2]["stars"]


# In[32]:


dataList[2]


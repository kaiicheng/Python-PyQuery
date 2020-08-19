#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from random import choice 


# In[2]:


driver = webdriver.Chrome("/Users/Paul/Desktop/Python Crawler/chromedriver.exe")


# In[3]:


driver.get("https://play2048.co/")
driver.current_url


# In[4]:


body = driver.find_element_by_css_selector("body")
arrowList = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]


# In[5]:


for i in range(200):
    #body.send_keys(arrowList[2])
    body.send_keys(choice(arrowList))
    sleep(0.01)


# In[ ]:





# In[ ]:


lastHeight = -1
while True:   # for i in range(80):
    wrapper = driver.find_element_by_css_selector(".wrapper").size
    height = wrapper["height"]
    print(height)
    driver.execute_script(" window.scrollTo(0,{})".format(height))
    
    if lastHeight == height:
        break
    lastHeight = height
    sleep(0.5)


# In[ ]:





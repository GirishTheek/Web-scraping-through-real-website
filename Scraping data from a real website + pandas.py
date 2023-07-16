#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[4]:


page=requests.get(url)
page


# In[5]:


soup=BeautifulSoup(page.text,'html')


# In[6]:


soup


# In[7]:


soup.find('table')


# In[9]:


soup.find_all('table')[1]


# In[10]:


soup.find('table', class_ = 'wikitable sortable')


# In[12]:


table = soup.find_all('table')[1]


# In[13]:


table


# In[16]:


world_title = table.find_all('th')


# In[17]:


world_title


# In[24]:


world_table_titles = [title.text.strip() for title in world_title]


# In[25]:


world_table_titles


# In[26]:


import pandas as pd


# In[27]:


df = pd.DataFrame(columns=world_table_titles)


# In[28]:


df


# In[29]:


column_data = table.find_all('tr')


# In[30]:


column_data


# In[36]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_data


# In[37]:


df


# In[43]:


df.to_csv(r"C:\Users\DELL\Desktop\New folder (2)\Company.csv",index=False)


# In[ ]:





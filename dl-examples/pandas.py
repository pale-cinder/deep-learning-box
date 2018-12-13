
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


pwd


# In[8]:


df = pd.read_csv('salaries.csv')


# In[18]:


df.as_matrix()


# In[12]:


df['Salary']


# In[13]:


df['Salary'].max()


# In[14]:


df.describe()


# In[15]:


df['Salary'] > 50000


# In[16]:


myfilter = df['Salary'] > 50000


# In[17]:


df[myfilter]


# In[19]:


df[df['Salary'] > 50000]


# In[ ]:





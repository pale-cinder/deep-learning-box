
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


get_ipython().magic('matplotlib inline')


# In[5]:


x = np.arange(0,10)


# In[6]:


x


# In[7]:


y = x**2


# In[12]:


plt.plot(x,y,'r--')
plt.xlim(0,4)
plt.ylim(0,10)
plt.title("TITLE")
plt.xlabel('X LABEL')
plt.ylabel('Y LABEL')


# In[13]:


mat = np.arange(0,100).reshape(10,10)


# In[14]:


mat


# plt.imshow(mat, cmap='RdYlGn')

# In[15]:


plt.imshow(mat, cmap='RdYlGn')


# In[17]:


mat = np.random.randint(0,100,(10,10))


# In[18]:


plt.imshow(mat)
plt.colorbar()


# In[20]:


df = pd.read_csv('salaries.csv')


# In[21]:


df


# In[23]:


df.plot(x='Salary',y='Age',kind='scatter')


# In[ ]:





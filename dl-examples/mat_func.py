
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_list = [1,2,3]


# In[4]:


type(np.array(my_list))


# In[9]:


arr =  np.array(my_list)


# In[10]:


arr


# In[14]:


np.arange(0,10,2)


# In[18]:


np.zeros((3,5))


# In[19]:


np.ones(2)


# In[20]:


np.ones((3,5))


# In[22]:


np.linspace(0,11,10)


# In[25]:


np.random.randint(0,100,(3,3))


# In[26]:


np.random.normal()


# In[28]:


np.random.seed(101)

np.random.randint(0,100,10)


# In[29]:


arr.min()


# In[31]:


arr.mean()


# In[32]:


arr.argmax()


# In[33]:


arr


# In[37]:


mat = np.arange(0,100).reshape(10,10)


# In[38]:


mat


# In[40]:


mat[4,3]


# mat[:,0]

# In[41]:


mat[:,0]


# In[42]:


mat[5,:]


# In[43]:


mat[0:3,0:3]


# In[44]:


mat > 50


# In[45]:


my_filter = mat > 50


# In[46]:


mat[my_filter]


# In[ ]:





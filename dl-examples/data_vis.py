
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as nd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


from sklearn.preprocessing import MinMaxScaler


# In[5]:


from sklearn.model_selection import train_test_split


# In[6]:


np.random.seed(101)


# In[7]:


mat = np.random.randint(1,101,(100,5))


# In[8]:


mat


# In[11]:


get_ipython().magic('matplotlib inline')


# In[15]:


plt.imshow(mat, aspect=0.005)
plt.colorbar()
plt.title("PLOT")


# In[20]:


df = pd.DataFrame(data=mat)


# In[19]:


import pandas as pd


# In[21]:


df


# In[22]:


df.plot(x=0,y=1,kind='scatter')


# In[23]:


scaler = MinMaxScaler()


# In[24]:


result = scaler.fit_transform(df)


# In[25]:


result


# In[26]:


df.columns = ['f1', 'f2', 'f3', 'f4', 'label']


# In[27]:


df


# In[28]:


df.head(10)


# In[29]:


X = df[['f1', 'f2', 'f3', 'f4', 'label']]


# In[30]:


Y = df[['label']]


# In[31]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)


# In[33]:


X_train


# In[ ]:





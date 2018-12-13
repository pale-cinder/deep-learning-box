
# coding: utf-8

# In[14]:


import numpy as np


# In[2]:


from sklearn.preprocessing import MinMaxScaler


# In[3]:


data = np.random.randint(0,100,(10,2))


# In[4]:


data


# In[5]:


scaler_model = MinMaxScaler()


# In[6]:


type(scaler_model)


# In[7]:


scaler_model.fit(data)


# In[8]:


scaler_model.transform(data)


# In[9]:


scaler_model.fit_transform(data)


# In[10]:


mydata = np.random.randint(0,101,(50,4))


# In[11]:


mydata


# In[13]:


data = pd.DataFrame(data=mydata)


# In[15]:


import pandas as pd


# In[20]:


df = pd.DataFrame(data=mydata, columns = ['f1','f2','f3','label'])


# In[21]:


df


# In[22]:


X = df[['f1','f2','f3']]


# In[24]:


Y = df['label']


# In[25]:


from sklearn.model_selection import train_test_split


# In[27]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=101)


# In[28]:


X_train.shape


# In[29]:


X_test.shape


# In[ ]:





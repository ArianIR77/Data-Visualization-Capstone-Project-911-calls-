#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('911.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df['zip'].value_counts().head() # top 5 zip codes


# In[6]:


df['twp'].value_counts().head() # top 5 townships for 911 calls


# In[7]:


df['title'].nunique() #number of unique title codes


# In[8]:


# create a new column 
df['reason']= df['title'].apply(lambda str : str.split(':')[0])


# In[9]:


df['reason']


# In[10]:


df['reason'].value_counts().head()


# In[11]:


sns.set(rc={'figure.figsize':(11,8)})
sns.countplot(x= 'reason', data=df)


# In[12]:


type(df['timeStamp'][0])


# In[13]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[14]:


df['timeStamp']


# In[15]:


df['hour'] = df['timeStamp'].apply(lambda hour : hour.hour)
df['month'] = df['timeStamp'].apply(lambda month : month.month)
df['year'] = df['timeStamp'].apply(lambda yr: yr.year)
df['Day of Week'] = df['timeStamp'].apply(lambda date : date.dayofweek)


# In[16]:


df.head()


# In[17]:


df['Day of Week_str'] =df['timeStamp'].dt.day_name()


# In[18]:


df.head()


# In[19]:


sns.countplot(x='Day of Week_str', data = df , hue='reason')


# In[20]:


sns.countplot(x='month', data = df , hue='reason')


# In[21]:


bymonth = df.groupby('month').count()


# In[23]:


bymonth.head()


# In[24]:


bymonth['zip'].plot()


# In[26]:


bymonth.reset_index()


# In[27]:


sns.lmplot(x='month',y='twp', data=bymonth.reset_index() )


# In[28]:


df['Date'] = df['timeStamp'].apply(lambda x : x.date())


# In[29]:


date = df.groupby('Date').count()


# In[30]:


date['e'].plot()
plt.tight_layout()


# In[32]:


df[df['reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[34]:


df[df['reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[39]:


df[df['reason']=='EMS'].groupby('Date').count()['twp'].plot()


# In[41]:


dayHour = df.groupby(by=['Day of Week','hour']).count()['e'].unstack()
dayHour.head()


# In[42]:


sns.heatmap(dayHour)


# In[44]:


dayMonth = df.groupby(by=['Day of Week','month']).count()['reason'].unstack()


# In[45]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:





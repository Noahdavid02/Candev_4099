#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from matplotlib import rcParams


# In[45]:


data = pd.read_excel("CANDEV_PSC data.xlsx")


# In[46]:


data.head()


# In[47]:


data.info()


# In[48]:


data.describe(include="all").T


# In[49]:


data.shape


# In[51]:


data.ORGANISATION.nunique()


# In[73]:


data.isna().sum()


# In[76]:


data.duplicated().sum()


# In[78]:


data.drop("PROVINCE_FR",axis=1,inplace=True)


# In[82]:


corr = data.corr()


# In[89]:


corr


# In[88]:


sns.heatmap(data=corr)
rcParams['figure.figsize'] = 15,20


# In[52]:


data.groupby("ORGANISATION").sum()


# In[71]:


data.groupby(["INDIGENOUS_PEOPLES"]).agg({"INDIGENOUS_PEOPLES":"count"})


# In[70]:


data.groupby(["PERSONS_WITH_DISABILITIES"]).agg({"PERSONS_WITH_DISABILITIES":"count"})


# In[68]:


data.groupby(["PROVINCE_EN"]).agg({"PROVINCE_EN":"count"})


# In[69]:


data.groupby(["ORGANISATION"]).agg({"PROVINCE_EN":"count"})


# In[72]:


Northern_Canada = ["Newfoundland and Labrador", "Quebec", "Ontario", "Manitoba", "Saskatchewan", "Alberta", "British Columbia"]


# In[92]:


plt.figure(figsize=(8,5))
sns.countplot(x=data['PROVINCE_EN'],  hue=data['PROVINCE_EN'])
plt.show()


# In[95]:


data.groupby(["APPLICATION_DATE"]).agg({"PROVINCE_EN":"count"})


# In[ ]:





# In[ ]:





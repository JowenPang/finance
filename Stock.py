#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[214]:


get_ipython().system('pip install ipython')
get_ipython().system('pip install nbconverter')


# In[ ]:





# In[138]:


pd.set_option('max_columns',None)
pd.set_option('max_rows',None)


# In[205]:


value_files = ['201907/BPAMERP20190731.csv','201908/BPAMERP20190830.csv','201909/BPAMERP20190930.csv',
            '201910/BPAMERP20191031.csv','201912/BPAMERP20191231.csv','202001/BPAMERP20200131.csv',
            '202002/BPAMERP20200228.csv','202003/BPAMERP20200331.csv','202004/BPAMERP20200430.csv',
            '202005/BPAMERP20200529.csv','202006/BPAMERP20200630.csv','202007/BPAMERP20200730.csv',
            '202008/BPAMERP20200828.csv','202009/BPAMERP20200930.csv','202010/BPAMERP20201030.csv']
type_files = ['201907/BPAMERS20190731.csv','201908/BPAMERS20190830.csv','201909/BPAMERS20190930.csv',
            '201910/BPAMERS20191031.csv','201912/BPAMERS20191231.csv','202001/BPAMERS20200131.csv',
            '202002/BPAMERS20200228.csv','202003/BPAMERS20200331.csv','202004/BPAMERS20200430.csv',
            '202005/BPAMERS20200529.csv','202006/BPAMERS20200630.csv','202007/BPAMERS20200730.csv',
            '202008/BPAMERS20200828.csv','202009/BPAMERS20200930.csv','202010/BPAMERS20201030.csv']


df=pd.DataFrame()

for v,t in zip(value_files,type_files):
    df_temp = pd.read_csv('./BPAM Evaluated Prices Rated Range Prices (LT)/'+v)
    df_tempT = pd.read_csv('./BPAM Evaluated Prices Rated Range Prices (LT)/'+t)
    df_temp= df_temp.merge(df_tempT,on='STOCK CODE')
    
    if df.empty:
        df= df_temp[df_temp['STOCK CODE'] =='DT070576']
    else:
        df= df.append(df_temp[df_temp['STOCK CODE'] =='DT070576'])


# In[206]:


df


# In[207]:


df.columns


# In[208]:


df_clean = df[['STOCK CODE','STOCK NAME_x', 'VALUE DATE', 'EVAL MID YIELD',
       'EVAL MID PRICE','MODIFIED DURATION','CONVEXITY','COMPOSITE LIQUIDITY SCORE (T-1)',
       'BOND TYPE', 'RATING','ISSUE DATE', 'MATURITY DATE', 'COUPON FREQUENCY', 
       'NEXT COUPON RATE', 'FACILITY AMOUNT/FACILITY LIMIT(MYR MIL)',
       'FACILITY OUTSTANDING AMOUNT(MYR MIL)', 'BOND ISSUE AMOUNT(MYR MIL)',
       'BOND CURRENT OUTSTANDING AMOUNT(MYR MIL)','ISSUER FACILITY LIMIT(MYR MIL)', 'ISSUER OUTSTANDING AMOUNT(MYR MIL)',
       'SECTOR','CALLABLE/PUTTABLE', 'CONVERTIBLE/EXCHANGABLE']]
df_clean


# In[209]:


df_clean.set_index('VALUE DATE',inplace=True)
df_clean.index = pd.to_datetime(df_clean.index)


# In[210]:


df_clean


# ### Bond Price over time

# In[200]:


df_clean.shape


# In[201]:


#plt.figure(figsize=(16,8))
plt.plot(df_clean['EVAL MID PRICE']);
plt.xlabel('Value Date');
plt.ylabel('Price');


# ### Yield (Interest) over time

# In[202]:


plt.plot(df_clean['EVAL MID YIELD']);
plt.plot(df_clean['NEXT COUPON RATE']);
plt.xlabel('Value Date');
plt.ylabel('Yield');
plt.legend(['yield','coupon rate']);


# ### High liquidity indicates its ability to pay debt obligations, or current liabilities, without having to raise external capital or take out loans.

# In[203]:


plt.plot(df_clean['COMPOSITE LIQUIDITY SCORE (T-1)']);
plt.xlabel('Value Date');
plt.ylabel('COMPOSITE LIQUIDITY SCORE');


# ### Convexity = the degree of the curve, in the relationship between bond prices and bond yields.

# In[204]:


plt.plot(df_clean['CONVEXITY']);
plt.xlabel('Value Date');
plt.ylabel('CONVEXITY');


# In[ ]:





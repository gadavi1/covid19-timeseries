#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[65]:


df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')


# In[66]:


df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')


# In[67]:


df['fips'] = df['fips'].fillna(0)
df['fips'] = df['fips'].astype(int)
df['fips'] = df['fips'].astype(str)
df['fips'] = df['fips'].str.zfill(5)
df['deaths'] = df['deaths'].fillna(0)
df['deaths'] = df['deaths'].astype(int)


# In[68]:


#Assign New York to a unique FIPS
df.loc[df['county'] == 'New York City','fips'] = '99999'

#Assign unknown counties to a generic FIPS code for state
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Alabama'),'fips'] = '01000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Alaska'),'fips'] = '02000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Arizona'),'fips'] = '04000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Arkansas'),'fips'] = '05000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'California'),'fips'] = '06000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Colorado'),'fips'] = '08000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Connecticut'),'fips'] = '09000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Delaware'),'fips'] = '10000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Florida'),'fips'] = '12000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Georgia'),'fips'] = '13000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Hawaii'),'fips'] = '15000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Idaho'),'fips'] = '16000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Illinois'),'fips'] = '17000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Indiana'),'fips'] = '18000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Iowa'),'fips'] = '19000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Kansas'),'fips'] = '20000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Kentucky'),'fips'] = '21000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Louisiana'),'fips'] = '22000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Maine'),'fips'] = '23000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Maryland'),'fips'] = '24000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Massachusetts'),'fips'] = '25000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Michigan'),'fips'] = '26000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Minnesota'),'fips'] = '27000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Mississippi'),'fips'] = '28000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Missouri'),'fips'] = '29000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Montana'),'fips'] = '30000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Nebraska'),'fips'] = '31000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Nevada'),'fips'] = '32000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'New Hampshire'),'fips'] = '33000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'New Jersey'),'fips'] = '34000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'New Mexico'),'fips'] = '35000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'New York'),'fips'] = '36000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'North Carolina'),'fips'] = '37000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'North Dakota'),'fips'] = '38000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Ohio'),'fips'] = '39000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Oklahoma'),'fips'] = '40000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Oregon'),'fips'] = '41000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Pennsylvania'),'fips'] = '42000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Rhode Island'),'fips'] = '44000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'South Carolina'),'fips'] = '45000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'South Dakota'),'fips'] = '46000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Tennessee'),'fips'] = '47000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Texas'),'fips'] = '48000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Utah'),'fips'] = '49000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Vermont'),'fips'] = '50000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Virginia'),'fips'] = '51000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Washington'),'fips'] = '53000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'West Virginia'),'fips'] = '54000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Wisconsin'),'fips'] = '55000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Wyoming'),'fips'] = '56000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'American Samoa'),'fips'] = '60000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Guam'),'fips'] = '66000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Northern Mariana Islands'),'fips'] = '69000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Puerto Rico'),'fips'] = '72000'
df.loc[(df['county'] == 'Unknown') & (df['state'] == 'Virgin Islands'),'fips'] = '78000'

#Assign cities in Missouri based on the county the mostly reside in.
df.loc[(df['county'] == 'Joplin') & (df['state'] == 'Missouri'),'fips'] = '27097'
df.loc[(df['county'] == 'Kansas City') & (df['state'] == 'Missouri'),'fips'] = '27095'


# In[69]:


df.tail()


# In[64]:


for i in range(30):
    df['date_shift' + str(i + 1).zfill(2)] = df['date'] + pd.Timedelta(days = i + 1)


# In[ ]:


#Need three columns
#A key (based on date and fips)
#A variable name
#A variable value
#Target variable will be percent increase


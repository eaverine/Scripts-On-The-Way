#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import shutil
from pathlib import Path
import os


# In[2]:


file = pandas.read_csv('trial.csv') #You can choose your own csv file


# In[3]:


id = file.iloc[0:, 0]
folder = file.iloc[0:, 1]


# In[5]:


real_path = os.getcwd()

for i in range(len(folder)):
    old_id = str(id[i]) 
    old_id_path = real_path + '\\' + old_id
    
    new_id = str(id[i]) + '.wav'
    new_id_path = real_path + '\\' + new_id
    
    new_folder = real_path + '\\' + folder[i]
    
    destination_file = new_folder + '\\' + new_id
    
    
    if os.path.exists(destination_file) == True or os.path.exists(old_id_path) == False:
        continue
    
    if os.path.exists(new_id) == True:
        pass
    else:
        shutil.move(old_id_path, new_id_path)
        
    if os.path.exists(new_folder) == True:
        pass
    else:
        os.makedirs(new_folder)
        
    shutil.move(new_id_path, destination_file)


# In[ ]:





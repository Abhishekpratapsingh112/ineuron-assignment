#!/usr/bin/env python
# coding: utf-8

# 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until
# the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
# [1980, 1981, 1982, 1983, 1984, 1985].

# In[1]:


years_list=[i for i in range(2001,2001+6)]
years_list


# 2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your
# first year.
# 

# In[2]:


years_list[3]


# 3. In the years list, which year were you the oldest?
# 

# In[3]:


max(years_list)


# 4. Make a list called things with these three strings as elements: 'mozzarella', 'cinderella','salmonella'.

# In[4]:


things=['mozzarella', 'cinderella','salmonella']


# 5. Capitalize the element in things that refers to a person and then print the list. Did it change the
# element in the list?
# 

# In[5]:


for i in things:
    print( i.capitalize())
things

#capatilize will not change the list


# 6. Make a surprise list with the elements "Groucho", "Chico", and "Harpo"
# 

# In[31]:


surprise=["Groucho", "Chico", "Harpo"]


# 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
# 

# In[32]:


surprise[-1].lower()


# In[33]:


surprise[-1][::-1]


# In[34]:


surprise[-1][::-1].capitalize()


# 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
# chien, cat is chat, and walrus is morse.
# 

# In[35]:


e2f = {'dog':'chien','cat':'chat','walrus':'morse'}


# 9. Write the French word for walrus in your three-word dictionary e2f.
# 

# In[36]:


e2f['walrus']


# 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
# 

# In[37]:


f2e = dict((key,value) for value,key in e2f.items())
f2e


# 11. Print the English version of the French word chien using f2e.
# 

# In[38]:


f2e['chien']


# 12. Make and print a set of English words from the keys in e2f.
# 

# In[39]:


e2f.keys()


# 13. Make a multilevel dictionary called life. Use these strings for the topmost keys:'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. 
# Make all the other keys refer to empty dictionaries.
# 

# In[40]:


life ={'animals':{'cat':['Henri', 'Grumpy', 'Lucy'], 'octopi':'', 'emus':''},
       'plants' :'',
       'other' :'' }
life


# 14. Print the top-level keys of life.
# 

# In[41]:


life.keys()


# 15. Print the keys for life['animals'].
# 

# In[42]:


life['animals'].keys()


# 16. Print the values for life[animals][cats]

# In[43]:


life['animals']['cat']


# In[ ]:





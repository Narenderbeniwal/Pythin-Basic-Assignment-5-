#!/usr/bin/env python
# coding: utf-8

# In[ ]:




Q. 1. What does an empty dictionary's code look like?
Solution : empty dictionary's code will look like this d = {}Q. 2. What is the value of a dictionary value with the key 'foo' and the value 42
d = {foo:2}
Solution: {'foo': 2}


# In[7]:


d = {"foo":2}
d

Q 3. What is the most significant distinction between a dictionary and a list?
Solution: Elements in a list have the following characteristics:

They maintain their ordering unless explicitly re-ordered (for example, by sorting the list).
They can be of any type, and types can be mixed.
They are accessed via numeric (zero based) indices.
Elements in a Dictionary have the following characteristics:

Every entry has a key and a value
Ordering is not guaranteed
Elements are accessed using key values
Key values can be of any hashtable type (i.e. not a dict) and types can be mixed
Values can be of any type (including other dict’s), and types can be mixed
# In[10]:


## Q 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# Solution: There will be key error 
spam = {'bar': 100}
spam['foo']

Q. 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
Solution: There is no difference. The in operator checks whether a value exists as a key in the dictionary.Q. 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
Solution: 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.Q  7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'
Solution: spam.setdefault('color', 'black')
Q 8.How do you "pretty print" dictionary values using which module and function?
Solution : The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a well-formatted and more readable way!

# In[ ]:





# In[ ]:





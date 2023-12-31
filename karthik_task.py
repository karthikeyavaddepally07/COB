#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from collections import Counter

def count_unique_words(file_path):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text into words (split by spaces and remove punctuation)
    words = re.findall(r'\w+', text.lower())  # Convert to lowercase for case-insensitivity

    # Count the occurrences of each word
    word_count = Counter(words)

    # Print unique words and their counts
    for word, count in word_count.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    file_path = "C:\\Users\\banot\\OneDrive\\Desktop\\tharun.txt"  #assign the file path
    count_unique_words(file_path)


# In[ ]:





# In[ ]:





# In[ ]:





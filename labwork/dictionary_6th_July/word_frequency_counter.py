"""
-----------------------------------------Problem Statement:--------------------------------------- 
Accept a sentence from the user and create a dictionary that stores the frequency of each word. 
Example:
-------------------------------------------------------------------------- 
Input: 
python is easy and python is powerful 
 -----------------------------------------------------------------------------
Output: 
{ 
'python': 2, 
'is': 2, 
'easy': 1, 
'and': 1, 
'powerful': 1 
} 
Additionally: 
• Display the most frequently occurring word.  
• Display all words in alphabetical order.
"""
# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Dictionary to store word frequency
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("\nWord Frequency:")
print(word_freq)

# Display the most frequently occurring word
most_frequent = max(word_freq, key=word_freq.get)
print(f"\nMost frequent word: '{most_frequent}' ({word_freq[most_frequent]} times)")

# Display all words in alphabetical order
sorted_words = sorted(word_freq)
print("\nWords in alphabetical order:")
for word in sorted_words:
    print(word)

"""
Output :
Enter a sentence: python is easy and python is powerful

Word Frequency:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

Most frequent word: 'python' (2 times)

Words in alphabetical order:
and
easy
is
powerful
python
"""

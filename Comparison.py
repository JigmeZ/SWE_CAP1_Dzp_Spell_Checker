import re

# Function to extract Dzongkha words
def Dzongkha(text):
    return set(re.findall(r'[\u0F00-\u0FFF]+', text))

# Read the contents of both files
file1 = open("344.txt", encoding="utf-8").read()
file2 = open("changed_dictionary.txt", encoding="utf-8").read()

# Get the words from both files
words_file1 = Dzongkha(file1)
words_file2 = Dzongkha(file2)

# Find words that are in file1 but not in file2
incorrect_words = words_file1 - words_file2

# Print the incorrect words
for word in incorrect_words:
    print(f"The word '{word}' is incorrect.")

# Reference https://www.opentechguides.com/how-to/article/python/58/python-file-comparison.html

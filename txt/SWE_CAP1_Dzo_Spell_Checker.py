#######################################
# https://github.com/JigmeZ/TXT.git
# Jigme Ngawang Chogyal
# Section: A
# ID : 02240344
#######################################
# REFERENCE: Chat GPT ,YOUTUBE

# https://openai.com/index/chatgpt, https://www.youtube.com/watch?v=_nkQd9SyEpw&t=12s 



#######
#SOLUTION
#######

#INPUT TXT

import re
url = "https://csf101-server-cap1.onrender.com/get/input/344"
file_extract = re.get(url)
with open('344.txt', 'wb') as f:
    statement = f.write(file_extract.content)
print('Downloaded: 344.txt')


# Clear Spelling
def clear_english(input_file, output_file):
    changes = []
    with open(input_file,"r",encoding = "utf-8") as files:
        for line in files:
            dzonkhas = line.split()
            if dzonkhas:
                word_dzo = dzonkhas[0]
                changes.append(word_dzo)
    with open(output_file, "w",encoding = "utf-8") as files:
        for dzonkhas in changes:
            files.write (dzonkhas + "\n")
        print(f"changed word saved to {output_file}")
input_file = "dictionary.txt"
output_file = "changed_dictionary.txt"
clear_english(input_file, output_file)


#main spelling check
import re

def extract_words(text):
    
    words = re.findall(r'[\u0F00-\u0FFF]+', text)
    return set(words)  

with open("344.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)

with open("changed_dictionary.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)

unique_to_file1 = word1.difference(word2)  

for word in unique_to_file1:
    print(f"The word '{word}' from this sentence is incorrect.")

#(some of the code used from chat gpt)


# Extra notes
# CONVERTION of doc into txt with code

import docx2txt as d2t

Docxfile = "dictionary.docx"
txtfile = "dictionary.txt"

doc = d2t.process(Docxfile)

file = open(txtfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print("file converted")
















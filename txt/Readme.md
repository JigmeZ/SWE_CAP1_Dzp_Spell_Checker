https://github.com/JigmeZ/SWE_CAP1_Dzp_Spell_Checker.git
# CODE Explanation
## input text
1.In this code I have extracted the text from the given link and I have saved it as 344.txt.
2.I have given a variable named "url" and gave a the link as an value.
3.And then i used the re.get(url) function to request the input file from url provide.
4.After getting access to the the url the filed will be renamed as 344.txt using the open function in wb mode.

## Check Spelling
1.I have given the function clear_english two parameters and then an empty list caleed changes is initialized to store the modified words.
2.I have used the split function  to read and split 
3.The word is appended to the changes list and then is written to the output file and then saved the file
4.Finally the output is found.

## Main spelling check
1.I have used the extract_words function to extract unique words from a given text using a regular expression.
2.with the help of UTF-8 encoding its read into content1 variable
3.I have used a bit of chat gpt in this codes

## CONVERTION of doc into txt with code
1.In this code, Though it is not rquired i have tried snd it worked...since its the continuation of the code. The docx2txt library is imported as d2t.
2.I have given a file path for both the input and the output to the variables docxfile and txtfile respectively.
3.The function is then used to extract the text from the docfile and then stored in the doc variable.
4.Then i have used the UTF-8 encoding and opened in write mode.






# PROJECT OVERVIEW
The project involves extracting text from a given link, converting a doc file to a text file,and checking the spelling of the text wether it is correct or not.

## USAGE
1. Install the required libraries using pip install doc2txt and requests
import re
url = "https://csf101-server-cap1.onrender.com/get/input/344"
file_extract = re.get(url)
with open('344.txt', 'wb') as f:
    statement = f.write(file_extract.content)
print('Downloaded: 344.txt')

2. Run the code to clear the spelling and charcater from the text
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

3. And then in the end we check for the error and check
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






## Implimentation Details
1. The code is implemented using python programming language and the required libraries are requests and doc2txt
2. The code is divided into three main parts: extracting text from a Link , converting doc file to txt file and checking spelling of the text
3. The code uses regular expression to extract unique words from the text and UTF-8 encoding to read and write files

## Data Structure
The code uses the following data structures:
- List: to store the modified words
- String: to store the text from the link and the doc file words from the text
- File: to store the output files

## Algorithms
The code uses the following algorithms:
- Regular expression: to extract unique words from the text
- UTF-8 encoding: to read and write files
- HTTp GET - requesting to download a specified file
- Document Conversion Algorithms: to convert doc file to txt file
- file processing algorithm: to process the file and check the spelling of the text

## Performance Analysis
The code has a time complexity of O(n) where n is the number of words in the text

## Challenges And Solutions
1.problem : I find it hard to search right term as for python it needs the right term to get the right code
2.problem : I found multiple problrm but with the help of youtube I implemented the concepts, the main challenges I found was when I try to clear all the english characters from the given uniques character set.
3.problem : While taking out the all the english character some character are still left out
4.problem : it was really hard recognizing the unique character (dzongkhag) so i used the concept of chat gpt

## Future Improvements
1. I can improve the code by using more efficient algorithms to extract unique words from the text.
2. the code can be improved by using more efficient data structures to store a modified words.

## Reference 
1. https://youtu.be/EpBX2f0Ebd8?si=IRlbnTe40Drn2jSi , https://youtu.be/jA9mpd4KSLg?si=OlRG7R56lqU9IRj3 , https://youtu.be/L2BDTy4bEcg?si=HWRdoHwhfH-loQcd











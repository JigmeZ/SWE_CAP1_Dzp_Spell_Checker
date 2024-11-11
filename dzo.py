import docx2txt as d2t

Docxfile = "dictionary.docx"
txtfile = "dictionary.txt"

doc = d2t.process(Docxfile)

file = open(txtfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print("file converted")

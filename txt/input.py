import re
url = "https://csf101-server-cap1.onrender.com/get/input/344"
file_extract = re.git(url)
with open('344.txt', 'wb') as f:
    statement = f.write(file_extract.content)
print('Downloaded: 344.txt')
#capitalize every other word
#apt-get insall python-html5lib
import sys
import requests
import random
from bs4 import BeautifulSoup




args = input("Type Sentence :: ")

if len(args) == 0: 
    r=requests.get("https://www.reddit.com/r/randomstories/")
    out = []
    status = r.status_code
    if (status == 200):
        code = "OK"
    elif (status == 404):
        code = "PageNotFound"
    else:
        code = status
    print("Connection :: ["+code+"]")
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    list = soup.find_all('p')
    for i in list:

        text = i.text
        if (len(text) > 100):
            out.append(text)
    num = random.randint(0,len(out)-1)
    print(str(len(out))+str(num))
    print(out[num])
    exit("\nstoryEND")

words = args
cap = 0
out=""
for i in words:
    if (i == " "): 
        out = out + i
        continue
    if (cap):
        out = out + i.upper()
        cap = 0
    else:
        out = out + i.lower()
        cap = 1
print(out)

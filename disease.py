import random
di=[]
line=[line.rstrip('\n') for line in  open('Disease_of_Day.txt')]
count1=1
for i in line:
    s=i.strip()
    if(len(s)>0):
        di.append(s)
        count1+=1
#print(len(di))
x=random.randint(0,304)
val1=di[x]
ans=''
ans+= val1+','
import bs4,webbrowser,requests
from bs4 import BeautifulSoup
flag=0

newlink='http://www.webmd.com/search/2/results?query='+val1+'&page='+str(1)
source_code=requests.get(newlink)
plaintext=source_code.text
soup=BeautifulSoup(plaintext,"lxml")
for link in soup.findAll('div',{"class":"module-content"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                ans+=str(mylink)+','
                flag=1
                break
        if flag==1:
            break
flag=0
newlink='https://search.cdc.gov/search?utf8=%E2%9C%93&affiliate=cdc-main&page='+str(1)+'&query='+val1
source_code=requests.get(newlink)
plaintext=source_code.text
soup=BeautifulSoup(plaintext,"lxml")
for link in soup.findAll('div',{"id":"results"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                ans+=str(mylink)+','
                flag=1
                break
        if flag==1:
            break
flag=0
newlink='https://search.nih.gov/search?affiliate=nih&commit=Search&page='+str(1)+'&query='+val1
source_code=requests.get(newlink)
plaintext=source_code.text
soup=BeautifulSoup(plaintext,"lxml")
for link in soup.findAll('div',{"id":"results"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                ans+=str(mylink)+','
                flag=1
                break
        if flag==1:
            break
flag=0
newlink='http://www.mayoclinic.org/search/search-results?q='+val1+'&Page='+str(1)+'&cItems=10'
source_code=requests.get(newlink)
plaintext=source_code.text
soup=BeautifulSoup(plaintext,"lxml")
for link in soup.findAll('div',{"class":"results"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                ans+=str(mylink)
                flag=1
                break
        if flag==1:
           break
print ans
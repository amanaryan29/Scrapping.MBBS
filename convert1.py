from random import randint
text_file=open('people.txt',"r")
ans=text_file.read()
ans=ans.split(' ')
for i in range(len(ans)):
    if ans[i]=='Disease':
        di=ans[i+1]
    elif ans[i]=='Symptoms':
        sy=ans[i+1]
    elif ans[i]=='Complications':
        com=ans[i+1]
sy=sy.split(',')
com=com.split(',')
di=di.split(',')
lis=[]
lis.append(len(di))
for i in di:
    lis.append(i)
lis.append(len(sy))
for i in sy:
    lis.append(i)
lis.append(len(com))
for i in com:
    lis.append(i)
import bs4,webbrowser,requests
from bs4 import BeautifulSoup
import re
countnumb=0
dicts={}
sym=[]
comp=[]
def findword(url):
    s1=''
    count3=0
    try :
        requests.get(url).raise_for_status()
    except:
        return
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"id":"mainContent_area"}):
            for link1 in link.findAll('p'):
                if link1!=None:
                    s1=s1+' '+link1.text.strip()
                #print s1
            p1=s1.split(' ')
            return p1
               
    return None            
def getlinks(url):
    try :
        requests.get(url).raise_for_status()
    except:
        return
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"class":"module-content"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                global countnumb
                countnumb=countnumb+1
                print(mylink)
                countsym=0
                countcomp=0
                counting=[]
                tex=findword(mylink)
                if tex!=None:
                    for p in sym:
                        if p in tex or p+'.' in tex or p+',' in tex: 
                            countsym+=1
                    for p in comp:
                        if p in tex or p+'.' in tex or p+',' in tex:
                            countcomp+=1
                counting.append(countsym)
                counting.append(countcomp)
                counting.append(countnumb)
                countings=tuple(counting)
                dicts[countings]=mylink
    for link in soup.findAll('div',{"class":"results-container"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                print(mylink)
                countnumb=countnumb+1
                countsym=0
                countcomp=0
                counting=[]
                tex=findword(mylink)
                if tex!=None:
                    for p in sym:
                        if p in tex or p+'.' in tex or p+',' in tex: 
                            countsym+=1
                    for p in comp:
                        if p in tex or p+'.' in tex or p+',' in tex:
                            countcomp+=1
                counting.append(countsym)
                counting.append(countcomp)
                counting.append(countnumb)
                countings=tuple(counting)
                dicts[countings]=mylink
#print(lis)
#lis=[2,'asthma','bronchitis',3,'fever','nausea','coughing',2,'smoking','obesity']
sz=len(lis)
count1=lis[0]
link1=''
for i in range(1,(count1+1)):
    link1=link1+lis[i]+'%20'
count2=lis[count1+1]
countt=count1+2+count2 #End of sym
count3=lis[countt]
#global sym
#global comp
for i in range(count1+2,countt):
    sym.append(lis[i])
for i in range(countt+1,sz):
    comp.append(lis[i])

for l in range(1,2):
    newlink='http://www.webmd.com/search/2/results?query='+link1+'&page='+str(l)
    print (newlink+"\n")
    getlinks(newlink)
    print('\n')
def findword1(url):
    s1=''
    p1=''
    count3=0
    try :
        requests.get(url).raise_for_status()
    except:
        return
       #print ('Hello')
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"class":"mSyndicate"}):
            #print link 
            for link1 in link.findAll('p'):
                if link1!=None:
                    s1=s1+' '+link1.text.strip()
                #print s1
            p1=s1.split(' ')
               
    if p1!='':
        return p1
    else:
        return None           
def getlinks1(url):
    try :
        requests.get(url).raise_for_status()
    except:
        return
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"id":"results"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                global countnumb
                countnumb=countnumb+1
                print(mylink)
                countsym=0
                countcomp=0
                counting=[]
                tex=findword1(mylink)
                if tex!=None:
                    for p in sym:
                        if p in tex or p+'.' in tex or p+',' in tex: 
                            countsym+=1
                    for p in comp:
                        if p in tex or p+'.' in tex or p+',' in tex:
                            countcomp+=1
                counting.append(countsym)
                counting.append(countcomp)
                counting.append(countnumb)
                countings=tuple(counting)
                dicts[countings]=mylink    
    
link1=''
for i in range(1,(count1+1)):
    if i!=count1:
        link1=link1+lis[i]+'%2B'
    else:
        link1+=lis[i]
for l in range(1,2):
    #https://search.cdc.gov/search?affiliate=cdc-main&commit=Search&page=1&query=asthma%2Bbronchitis%2B
    newlink='https://search.cdc.gov/search?utf8=%E2%9C%93&affiliate=cdc-main&page='+str(l)+'&query='+link1
    print newlink+"\n"
    getlinks1(newlink)
    print('\n')
def findword2(url):
    s1=''
    p1=''
    count3=0
    try :
        requests.get(url).raise_for_status()
    except:
        return
       #print ('Hello')
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"class":"row inner_content"}):
            #print link 
            for link1 in link.findAll('p'):
                if link1!=None:
                    s1=s1+' '+link1.text.strip()
                #print s1
            p1=s1.split(' ')
               
    if p1!='':
       
        return p1
    else:
        for link in soup.findAll('div',{"class":"field field-name-body field-type-text-with-summary field-label-hidden"}):
            #print link 
            for link1 in link.findAll('p'):
                if link1!=None:
                    s1=s1+' '+link1.text.strip()
                #print s1
            p1=s1.split(' ')
    if p1!='':
        return p1
    else:
        return None   
def getlinks2(url):
    try :
        requests.get(url).raise_for_status()
    except:
        return
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"id":"results"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                global countnumb
                countnumb=countnumb+1
                print(mylink)
                countsym=0
                countcomp=0
                counting=[]
                tex=findword2(mylink)
                if tex!=None:
                    for p in sym:
                        if p in tex or p+'.' in tex or p+',' in tex: 
                            countsym+=1
                    for p in comp:
                        if p in tex or p+'.' in tex or p+',' in tex:
                            countcomp+=1
                counting.append(countsym)
                counting.append(countcomp)
                counting.append(countnumb)
                countings=tuple(counting)
                dicts[countings]=mylink    
    
link1=''
for i in range(1,(count1+1)):
    if i!=count1:
        link1=link1+lis[i]+'%2B'
    else:
        link1+=lis[i]
for l in range(1,2):
    newlink='https://search.nih.gov/search?affiliate=nih&commit=Search&page='+str(l)+'&query='+link1
    print newlink+"\n"
    getlinks2(newlink)
    print('\n')
def findword3(url):
    #print url
    s1=''
    p1=''
    count3=0
    try :
        requests.get(url).raise_for_status()
    except:
        return
    # print ('Hello')
    source_code=requests.get(url)
    plaintext=source_code.text
#    print plaintext
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"class":"content"}):
            #print link 
            for link1 in link.findAll('p'):
                if link1!=None:
                    s1=s1+' '+link1.text.strip()
                #print s1
            p1=s1.split(' ')
               
    if p1!='':
        return p1
    else:
        return None   
def getlinks3(url):
    try :
        requests.get(url).raise_for_status()
    except:
        return
    #print ('hello')
    source_code=requests.get(url)
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"class":"personlist directory"}):
        # print link
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                global countnumb
                countnumb=countnumb+1
                print(mylink)
                countsym=0
                countcomp=0
                counting=[]
                tex=findword3(mylink)
                if tex!=None:
                    for p in sym:
                        if p in tex or p+'.' in tex or p+',' in tex: 
                            countsym+=1
                    for p in comp:
                        if p in tex or p+'.' in tex or p+',' in tex:
                            countcomp+=1
                counting.append(countsym)
                counting.append(countcomp)
                counting.append(countnumb)
                countings=tuple(counting)
                dicts[countings]=mylink    
    
link1=''
for i in range(1,(count1+1)):
    if i!=count1:
        link1=link1+lis[i]+'%2B'
    else:
        link1+=lis[i]
for l in range(1,2):
    #http://www.healthline.com/search?q1=asthma%2Bbronchitis
    #http://www.mayoclinic.org/search/search-results?q=asthma+bronchitis
    #http://www.mayoclinic.org/search/search-results?q=asthma+bronchitis&Page=2&cItems=10
    newlink='http://www.mayoclinic.org/search/search-results?q='+link1+'&Page='+str(l)+'&cItems=10'
    print newlink+"\n"
    getlinks3(newlink)
    print('\n')
keylist = dicts.keys()
keylist.sort(reverse=True)
dicts1={}
count2=0
for key in keylist:
	if(key[0]==0 and key[1]==0):
		break
	print(str(dicts[key]))
	count2=count2+1
	if count2==5:
		break
if count2!=5:
	for  i in xrange(count2,6):
		val=randint(10,50)
		print(dicts[(0,0,val)])



#Making a list of the details submitted int the form  

from random import randint
text_file=open('people.txt',"r")#people.txt => text file contating the submitted fields(diseases,symptoms,complications)
ans=text_file.read()
ans=ans.split(' ')#the various fields are seperated on spaces
for i in range(len(ans)):
    if ans[i]=='Disease':
        di=ans[i+1]
    elif ans[i]=='Symptoms':
        sy=ans[i+1]
    elif ans[i]=='Complications':
        com=ans[i+1]
sy=sy.split(',') #the datas of a particular field are seperated by ","(eg:various symptoms are seperated using comma) .... So sy contains the list of symptoms
com=com.split(',')#com contains the list of complications
di=di.split(',') #di contains the list of diseases
lis=[] #list of diseases ,symptoms and complications in the form(disease_length,followed by the various diseases,symptoms_length,followed by various symptoms,complications_length,followed by various complications
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#findword() function creates a list of the paragraphs in the provided link where probably we can find the symptoms 
def findword(url):
    s1=''
    count3=0
    try :
        requests.get(url).raise_for_status()
    except:
        return
    source_code=requests.get(url) #source_code is response object
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
    for link in soup.findAll('div',{"id":"mainContent_area"}):
            for link1 in link.findAll('p'):
                if link1!=None:
                    s1=s1+' '+link1.text.strip()#string of all the paragraph's  
                #print s1
            p1=s1.split(' ')#list of all the strings seperated by space 
            return p1
               
    return None

#getlinks function extracts the links and  in the links, finds the frequency of symptoms,complications and with these,
#creates a dictionary with the key=(countsymptoms,countcomplications,link_id)and value as the corresponding_link 
def getlinks(url):
    try :
        requests.get(url).raise_for_status()
    except:
        return
    source_code=requests.get(url) #source_code is response object
    plaintext=source_code.text
    soup=BeautifulSoup(plaintext,"lxml")
   #page is divided into two parts =>module-content and results-container 
    for link in soup.findAll('div',{"class":"module-content"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')#get the corresponding links 
                global countnumb
                countnumb=countnumb+1 #count of the number of links
                #print(mylink)
                countsym=0  #count of number of times any of the symptoms matches in the list
                countcomp=0 #count of number of times any of the complications matches in the list
                counting=[]
                tex=findword(mylink) #contains the list of paragraphs in the given link
                if tex!=None:
                    for p in sym: #sym contains the list of symptoms
                        if p in tex or p+'.' in tex or p+',' in tex: 
                            countsym+=1
                    for p in comp:
                        if p in tex or p+'.' in tex or p+',' in tex:
                            countcomp+=1
                counting.append(countsym)
                counting.append(countcomp)
                counting.append(countnumb)
                countings=tuple(counting) #countings is a list having first symptoms count ,followed by complication count,followed by link count
                dicts[countings]=mylink
                
    for link in soup.findAll('div',{"class":"results-container"}):
        for link2 in link.findAll('a'):
            if link2!=None:
                mylink=link2.get('href')
                #print(mylink)
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
#dicts has key=(symbol_count,complication_count,linknumber) and   value=corresponding link
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
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
                #print(mylink)
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------                
#print(lis)
#lis=[2,'asthma','bronchitis',3,'fever','nausea','coughing',2,'smoking','obesity']
sz=len(lis)
count1=lis[0] #count of the diseases entered 
link1=''
for i in range(1,(count1+1)):#iterating through the disease list
    link1=link1+lis[i]+'%20'
#link1=disease1+%20+disease2+%20
    
count2=lis[count1+1] #count of symptoms entered 
countt=count1+2+count2 #End of sym
count3=lis[countt] #count of complications entered
#global sym
#global comp
for i in range(count1+2,countt): #iterating through the symptom list
    sym.append(lis[i])
for i in range(countt+1,sz): #iterrating through the complication  list
    comp.append(lis[i])

for l in range(1,2):
    newlink='http://www.webmd.com/search/2/results?query='+link1+'&page='+str(l)#forming the link containing the diseases
#    print (newlink+"\n")
    getlinks(newlink)
#    print('\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
link1=''
for i in range(1,(count1+1)):
    if i!=count1:
        link1=link1+lis[i]+'%2B'
    else:
        link1+=lis[i]
#link1=disease1+%2B+disease2
for l in range(1,2):
    #newlink is of form=> https://search.cdc.gov/search?affiliate=cdc-main&commit=Search&page=1&query=asthma%2Bbronchitis%2B
    newlink='https://search.cdc.gov/search?utf8=%E2%9C%93&affiliate=cdc-main&page='+str(l)+'&query='+link1 #forming the link containing the diseases
#    print newlink+"\n"
    getlinks1(newlink)
 #   print('\n')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# def findword2(url):
#     s1=''
#     p1=''
#     count3=0
#     try :
#         requests.get(url).raise_for_status()
#     except:
#         return
#        #print ('Hello')
#     source_code=requests.get(url)
#     plaintext=source_code.text
#     soup=BeautifulSoup(plaintext,"lxml")
#     for link in soup.findAll('div',{"class":"row inner_content"}):
#             #print link 
#             for link1 in link.findAll('p'):
#                 if link1!=None:
#                     s1=s1+' '+link1.text.strip()
#                 #print s1
#             p1=s1.split(' ')
               
#     if p1!='':
       
#         return p1
#     else:
#         for link in soup.findAll('div',{"class":"field field-name-body field-type-text-with-summary field-label-hidden"}):
#             #print link 
#             for link1 in link.findAll('p'):
#                 if link1!=None:
#                     s1=s1+' '+link1.text.strip()
#                 #print s1
#             p1=s1.split(' ')
#     if p1!='':
#         return p1
#     else:
#         return None   
# def getlinks2(url):
#     try :
#         requests.get(url).raise_for_status()
#     except:
#         return
#     source_code=requests.get(url)
#     plaintext=source_code.text
#     soup=BeautifulSoup(plaintext,"lxml")
#     for link in soup.findAll('div',{"id":"results"}):
#         for link2 in link.findAll('a'):
#             if link2!=None:
#                 mylink=link2.get('href')
#                 global countnumb
#                 countnumb=countnumb+1
#                 #print(mylink)
#                 countsym=0
#                 countcomp=0
#                 counting=[]
#                 tex=findword2(mylink)
#                 if tex!=None:
#                     for p in sym:
#                         if p in tex or p+'.' in tex or p+',' in tex: 
#                             countsym+=1
#                     for p in comp:
#                         if p in tex or p+'.' in tex or p+',' in tex:
#                             countcomp+=1
#                 counting.append(countsym)
#                 counting.append(countcomp)
#                 counting.append(countnumb)
#                 countings=tuple(counting)
#                 dicts[countings]=mylink    
    
# link1=''
# for i in range(1,(count1+1)):
#     if i!=count1:
#         link1=link1+lis[i]+'%2B'
#     else:
#         link1+=lis[i]
# for l in range(1,2):
#     newlink='https://search.nih.gov/search?affiliate=nih&commit=Search&page='+str(l)+'&query='+link1
# #    print newlink+"\n"
#     getlinks2(newlink)
#  #   print('\n')
# def findword3(url):
#     #print url
#     s1=''
#     p1=''
#     count3=0
#     try :
#         requests.get(url).raise_for_status()
#     except:
#         return
#     # print ('Hello')
#     source_code=requests.get(url)
#     plaintext=source_code.text
# #    print plaintext
#     soup=BeautifulSoup(plaintext,"lxml")
#     for link in soup.findAll('div',{"class":"content"}):
#             #print link 
#             for link1 in link.findAll('p'):
#                 if link1!=None:
#                     s1=s1+' '+link1.text.strip()
#                 #print s1
#             p1=s1.split(' ')
               
#     if p1!='':
#         return p1
#     else:
#         return None   
# def getlinks3(url):
#     try :
#         requests.get(url).raise_for_status()
#     except:
#         return
#     #print ('hello')
#     source_code=requests.get(url)
#     plaintext=source_code.text
#     soup=BeautifulSoup(plaintext,"lxml")
#     for link in soup.findAll('div',{"class":"personlist directory"}):
#         # print link
#         for link2 in link.findAll('a'):
#             if link2!=None:
#                 mylink=link2.get('href')
#                 global countnumb
#                 countnumb=countnumb+1
#                 #print(mylink)
#                 countsym=0
#                 countcomp=0
#                 counting=[]
#                 tex=findword3(mylink)
#                 if tex!=None:
#                     for p in sym:
#                         if p in tex or p+'.' in tex or p+',' in tex: 
#                             countsym+=1
#                     for p in comp:
#                         if p in tex or p+'.' in tex or p+',' in tex:
#                             countcomp+=1
#                 counting.append(countsym)
#                 counting.append(countcomp)
#                 counting.append(countnumb)
#                 countings=tuple(counting)
#                 dicts[countings]=mylink    
    
# link1=''
# for i in range(1,(count1+1)):
#     if i!=count1:
#         link1=link1+lis[i]+'%2B'
#     else:
#         link1+=lis[i]
# for l in range(1,2):
#     #http://www.healthline.com/search?q1=asthma%2Bbronchitis
#     #http://www.mayoclinic.org/search/search-results?q=asthma+bronchitis
#     #http://www.mayoclinic.org/search/search-results?q=asthma+bronchitis&Page=2&cItems=10
#     newlink='http://www.mayoclinic.org/search/search-results?q='+link1+'&Page='+str(l)+'&cItems=10'
#     #print newlink+"\n"
#     getlinks3(newlink)
#     #print('\n')
keylist = dicts.keys() #list of keys of dictionary
keylist.sort(reverse=True)#sort in descending order
dicts1={}
count2=0
anss=''
for key in keylist:
	if(key[0]==0 and key[1]==0): #if at some point of time there is neither a match for symptoms and complications ,then break 
		break
	anss=anss+str(dicts[key])+','
	count2=count2+1
	if count2==5:
		break
if count2!=5:
	for  i in xrange(count2,6):
		val=randint(0,20)
		anss=anss+str(dicts[(0,0,val)])+','#if there are less than 5 links then randomly select the count id's add the links even if the first two counts are 0 
print(anss)


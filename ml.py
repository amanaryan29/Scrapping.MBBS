import pandas as pd
df2=pd.read_csv('fin.csv')
dataset=df2# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
# Split-out validation dataset
array = dataset.values
#print(dataset.shape)
X = array[:,0:669]
Y = array[:,669]
#print(Y)
# Test options and evaluation metric
#num_folds = 10
#num_instances = len(X)
#seed = 7
scoring = 'accuracy'
model2=DecisionTreeClassifier()
model2.fit(X,Y)
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
sym=[]
for i in sy:
    sym.append(i)
#sy=['Fatigue','Throat pain','Bloating','Loss of Appetite','Severe heartburn']
m=[]
for j in df2.columns:
        if j in sym:
            m.append(1)
        else:
            m.append(0)
m=m[:len(m)-1]
#print(m)

#df5.columns=df2.columns
val1=model2.predict(m)
val1=str(val1[0])
ans=''
ans+=val1+','
import bs4,webbrowser,requests
from bs4 import BeautifulSoup
flag=0
flag0=0
newlink='http://www.webmd.com/search/2/results?query='+val1+'&page='+str(1)
try :
        requests.get(newlink).raise_for_status()
except:
        flag0=1
if flag0==1:
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
flag0=0
newlink='https://search.cdc.gov/search?utf8=%E2%9C%93&affiliate=cdc-main&page='+str(1)+'&query='+val1
try :
        requests.get(newlink).raise_for_status()
except:
        flag0=1
if flag0==1:
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
flag0=0
newlink='https://search.nih.gov/search?affiliate=nih&commit=Search&page='+str(1)+'&query='+val1
try :
        requests.get(newlink).raise_for_status()
except:
        flag0=1
if flag0==0:
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
flag0=0
newlink='http://www.mayoclinic.org/search/search-results?q='+val1+'&Page='+str(1)+'&cItems=10'
try :
        requests.get(newlink).raise_for_status()
except:
        flag0=1
if flag0==0:
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
#print(accuracy_score(ans,Y_validation))

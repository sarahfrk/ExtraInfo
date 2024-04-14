import urllib3.request
import requests
from bs4 import BeautifulSoup
import string
import lxml
import sys
import re
links=[]

h='.htm'
txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=re.findall('['+sys.argv[1]+']',txt)
k=0
info1=open('infos1.txt','w+',encoding='utf-8')
f=open('subst.dic', 'wt',encoding='utf-16-le')
f.write('\ufeff ')
for i in x:
    req = requests.get('http://127.0.0.1:'+sys.argv[2]+'/vidal/vidal-Sommaires-Substances-'+i+h)
    soup = BeautifulSoup(req.content, 'lxml')
    div1 = soup.find('div',{'class':'grey-band'})   
    div2 = div1.find('div', {'id': 'global'})
    div3 = div2.find('div', {'class': 'content_bloc_full'})
    ul =div3.find('ul',{'id':'letter'+i.lower()})
    lis=ul.findAll('li')
    info.write('Total de '+i+' : '+str(len(lis))+'\r')
    k=k+len(lis)
    for li in lis:
        a = li.find('a')
        f.write(a.text+',.N+subst\r')

info.write('Nombre total des substances actives :  '+str(k)+'\r')
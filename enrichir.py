import re
import sys
from string import ascii_uppercase

corpus = open(sys.argv[1], 'r',encoding='UTF-8')
dctenri = open('subt_corpus.dic', 'wt', encoding='utf-16-le')
dctenri.write('\ufeff ')
sv= open('subst.dic', 'r+', encoding='utf-16-le').readlines()
dct = open('subst.dic', 'a+', encoding='utf-16-le')
cpt=0
listCorpus = corpus.readlines()

for line in listCorpus:
    sreg = re.search(r'''
    ^[-*Ø]?\s?  # Debut avec "* " ou "- "
    (\w+)       #La substance recherchée 
    \s:?\s?     #subts :  (GAVISCON : 1 sachet par jour.)
    (\d+|,|\d+.\d)+
    \s?:?   
    (\s(mg\s|MG|UI|ml|mcg|amp|iu|flacon|g|sachet|un\s|1/j|/j)(.+|\n)|(g|/j)\n|(mg)\s.+)
    ''', line, re.VERBOSE | re.I)
    if sreg:
        if  sreg.group(1).lower() != 'digoxine' \
                and sreg.group(1).lower() != 'vichy' \
                and sreg.group(1).lower() != 'mdz' \
                and sreg.group(1).lower() != 'moduretic' \
                and sreg.group(1).lower() != 'vvp' \
                and sreg.group(1).lower() != 'hyperium' \
                and sreg.group(1).lower() != 'kcl' \
                and sreg.group(1).lower() != 'foldine' \
                and sreg.group(1).lower() != 'aerius' \
                and sreg.group(1).lower() != 'hémoglobine' \
                and sreg.group(1).lower() != 'aspégic'  \
                and sreg.group(1).lower() != 'b1' \
                and sreg.group(1).lower() != 'kt' \
                and sreg.group(1).lower() != 'le' \
                and sreg.group(1).lower() != 'crp' \
                and sreg.group(1).lower() != 'eau' \
                and sreg.group(1).lower() != 'puis':
            dctenri.write(sreg.group(1).lower()+',.N+subst\r')
            dct.write(sreg.group(1).lower()+',.N+subst\r')
            cpt+=1
            print(str(cpt)+" : "+sreg.group(1).lower())

dct = open('subst.dic', 'r+', encoding='utf-16-le')
tri = sorted(list(set(dct.readlines())))
dct = open('subst.dic', 'w+', encoding='utf-16-le')
for el in tri:
    dct.write(el)
info3 = open('infos3.txt', 'w+', encoding='utf-8')
info2 = open('infos2.txt', 'w+', encoding='utf-8')
dctenri = open('subt_corpus.dic', 'r', encoding='utf-16-le')
listDctEnri = sorted(list(set(dctenri.readlines())))
cmp=0
for letter in ascii_uppercase:
    nbLettre=0
    for el in  listDctEnri:
        if letter == el[0].upper():
            nbLettre+=1
            info2.write(el)
    cmp=cmp+ nbLettre
    info2.write('----------------------------------------\nTotal de '+str(letter)+' : '+str(nbLettre)+'\n----------------------------------------\n')


info2.write('----------------------------------------\nTotal '+str(cmp)+'\n----------------------------------------\n')

cmp=0
k=0
for i in tri:
    for j in sv:
        if i==j:
            k=k+1
    if k==0:
        info3.write(i)
    k=0

info3 = open('infos3.txt', 'r+', encoding='utf-8')
info3tri = sorted(list(set(info3.readlines())))
info3 = open('infos3.txt', 'w+', encoding='utf-8')
cmp=0
for letter in ascii_uppercase:
    nbLettre=0
    for el in  info3tri:
        if letter == el[0].upper():
            nbLettre+=1
            info3.write(el)
    cmp=cmp+ nbLettre
    info3.write('--------------------------------\nTotal de '+str(letter)+' : '+str(nbLettre)+'\n---------------------------------\n')


info3.write('----------------------------------\nTotal '+str(cmp)+'\n--------------------------------\n')





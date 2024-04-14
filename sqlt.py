
import sqlite3
import codecs 
import re
fichier= codecs.open(r"C:\Users\hp\AppData\Local\Unitex-GramLab\App\corpus-medical_snt\concord.html",'r',"utf-8")
l=fichier.read()

fin = re.findall('href="(([0-9]+) )+[0-9]*">(\w*)',l)

connective =sqlite3.connect('extraction.db')
cur=connective.cursor()
cur.execute("CREATE TABLE EXTRACTION ( ID INTEGER PRIMARY KEY, Posologie TEXT )")
cpt=1
for c in fin:
   cur.execute("INSERT INTO EXTRACTION VALUES ("+str(cpt)+","+" \' "+c[2]+" \' "+")")
   print(str(cpt)+" : "+c[2])
   cpt=cpt+1
   
   
req="select * from EXTRACTION"
result = cur.execute(req)



connective.commit()
cur.close()
connective.close()

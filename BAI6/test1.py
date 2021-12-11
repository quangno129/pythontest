import string
import math
doc_list=['The Learn Python Chanllenge','They bought a car','Casinoville']
keyword=['casino']
doc_temp=doc_list
keytemp=keyword
s= ''
tim=False
#
for indexkey in range(len(keytemp)):
    k=keytemp[indexkey]
    k=k.strip().lower()
    print(k)
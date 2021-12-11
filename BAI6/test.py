import math
doc_list=['   The Learn Python Chanllenge    ']
keyword="the"
doc_temp=doc_list
s= ''
tim=False
for index in range(len(doc_temp)):
    s=doc_temp[index]       
    s1=s.strip().lower()
    s2=s1.split()    
    s3=' '.join(s2)
    #pos = s.find(keyword)
    print('s',s)
    print('s1',s1)
    print('s2',s2)
    print('s3',s3)
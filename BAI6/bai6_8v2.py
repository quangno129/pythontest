doc_list=['The Learn Python Chanllenge casino.','They bought a car and a Casino','Casinoville']
keyword=['Casino','Python','test1','Test2']
doc_temp=doc_list
keytemp=keyword
#xu ly doc list tro thanh dang chữ thường
for index in range(len(doc_temp)):
    doc_temp[index]=doc_temp[index].strip().lower().rstrip('.')
#xu ly keyword tro thanh dang chữ thường
for index_1 in range(len(keytemp)):
    keytemp[index_1]=keytemp[index_1].strip().lower()
    keytemp[index_1]=keytemp[index_1]
#xu ly chinh
flag=False
for element_1 in range(len(keytemp)):
    for element in range(len(doc_temp)):
        if doc_temp[element].find(keytemp[element_1]) != -1:
            flag=True
            doc_tempN=doc_temp[element].split() #tach chuoi trong manng thanh chuoi nho       
            for elementN in range(len(doc_tempN)):
                if doc_tempN[elementN].find(keytemp[element_1]) != -1 and len(doc_tempN[elementN])==len(keytemp[element_1]):
                    print('keyword co trong mang la: '+keytemp[element_1]+' ở vi tri trong mang '+str(element+1))
    if flag==False:
        print('gia tri khong ton tai trong doc_list')           
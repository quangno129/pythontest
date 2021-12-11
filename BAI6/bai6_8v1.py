import math
doc_list=['The Learn Python Chanllenge casino','They bought a car and a Casino','i have Casinoville']
keyword=['Casino','Python','test1','Test2']
doc_temp=doc_list
keytemp=keyword
#xu ly doc list tro thanh dang chữ thường
for index in range(len(doc_temp)):
    doc_temp[index]=doc_temp[index].strip().lower()
# for element_4 in doc_temp:
#     element_4=element_4.strip().lower()
#     print(element_4)
#xu ly keyword tro thanh dang chữ thường
for index_1 in range(len(keytemp)):
    keytemp[index_1]=keytemp[index_1].strip().lower()
    print(keytemp[index_1]+'x')
#xu ly chinh
# flag=False
# for element_1 in keytemp:
#     for element in doc_temp:
#         if element.find(element_1) != -1:
#             flag=True
#             print('keyword co trong mang la: '+element_1+' ở vi tri trong mang '+str(doc_temp.index(element)))
#     if flag==False:
#         print('gia tri khong ton tai trong doc_list')           
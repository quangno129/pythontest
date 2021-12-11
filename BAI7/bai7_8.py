list=[]
y=1
while y==1:
    nhapgiatri=int(input('nhap gia tri:'))
    y=int(input('tiep tuc nhap gia tri? 1:continute 0:stop'))
    list.append(nhapgiatri)
print(list)
#xem trong danh sach co so may man hay khong
findkey=6
if findkey in list:
    print(True)
else:
    print(False)
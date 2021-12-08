set_1=set()
set_2=set()

#nhap phan tu vao set
y=1
while y==1:
    nhapgiatri=int(input('nhap gia tri:'))
    y=int(input('tiep tuc nhap gia tri? 1:continute 0:stop'))
    set_1.add(nhapgiatri)

y=2
while y==2:
    nhapgiatri=int(input('nhap gia tri:'))
    y=int(input('tiep tuc nhap gia tri? 1:continute 0:stop'))
    set_2.add(nhapgiatri)

#set co bao nhieu phan tu
print('len set_1',len(set_1))
print('len set_2',len(set_2))
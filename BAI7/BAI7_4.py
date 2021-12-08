list=[]
y=1
while y==1:
    nhapgiatri=int(input('nhap gia tri:'))
    y=int(input('tiep tuc nhap gia tri? 1:continute 0:stop'))
    list.append(nhapgiatri)
print(list)
print('tong gia tri cua list:',sum(list))
#so lan gia tri xuat hien trong chuoi
x=int(input('nhap gia tri x can tim:'))
i=0
flag=False
for element in list:
    if element == x:
        i+=1
        flag=True
if flag==False:
    print('khong co gia tri x')
print(str(x)+' x xuat hien trong list '+str(i)+' lan')

#tim max trong list
if x is max(list):
    print('x lon hon tat ca cac so trong list')
else:
    print('x khong lon hon tat ca cac so trong list')
print('cac so lon hon x',[i for i in list if x<i])

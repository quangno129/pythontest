tuple=('one','two','three','four','five','six','seven','eight','nine','two')
print('Tuple:',tuple)
index_duong=int(input('nhap vao index duong: '))
index_am=int(input('nhap vao index am: '))
 #chuoi can tim
t=0
flag=False
find=str(input('nhap chuoi can tim: '))
for i in tuple:
     if i == find:
         t+=1
         flag=True
if flag==False:
    print('khong tim thay')
print('Tuble ['+str(index_duong)+']='+tuple[index_duong])
print('Tuble ['+str(index_am)+']='+tuple[index_am])
print(t,i)
    
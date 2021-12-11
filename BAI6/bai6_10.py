import math
#nhap vao chuoi s:
s=str(input('nhap vao chuoi S:'))
#nhap vao chuoi con s_sub:
s_sub=str(input('nhap vao chuoi s_sub:'))
#nhap vao chuoi tim s_find:
s_find=str(input('nhap vao chuoi s_find:'))
#nhap vao chuoi thay the s_replace:
s_replace=str(input('nhap vao chuoi s_replace:'))
# chuoi s loại bỏ khoảng trắng đầu cuối
s1=s.strip()
print('chuoi s sau khi loai bo khoang trang dau va cuoi:'+s1)
#chuoi viet hoa ky tu dau tien
s2=s1.split()
for element in range(len(s2)):
    if element==0:
        s2[element]=s2[element].upper()
    else:
        s2[element]=s2[element]
s3=' '.join(s2)
print('chuoi viet hoa ky tu dau tien:'+s3)
#so lan s_sub suat hien trong s:
i=0
flag=False
for element in s1:
    if element.find(s_sub) != -1:
        flag=True
        i+=1
print('so lan s_sub xuat hien trong s:',i)
if flag==False:
    print('khong co s_sub xuat hien trong s')
#tim kiem va thay the s_find thanh s_replace
s4=s3.split()
flag=False
for index in range(len(s4)):
    if s4[index]==s_find:
        flag=True
        print('tim kiem va thay the:',s3.replace(s_find,s_replace))
if flag==False:
    print('khong tim kiem duoc tu de thay the')


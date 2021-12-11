import string
import math
doc_list=['The Learn Python Chanllenge casino','They bought a car and a Casino','Casinoville']
keyword=str(input('nhap chuoi can tim: '))
doc_temp=doc_list
s= ''
tim=False
for index in range(len(doc_temp)):
      # lay trong tu trong doc_temp ra lan luot
    s=doc_temp[index].strip().lower() #ham chuyen xoa bo khoang trang dau cuoi strip, chuyen do chu hoa thanh chu thuong lower
    s=' '.join(s.split())             #s.spit() dung de tao ra cac phan tu dc list theo tring mac dinh la khoang trang,''.join() dung de doi chu xoa khoang trang
    pos = s.find(keyword)             #sai ham join de chuyen bo cac dau " " thanh khoang trang tao thanh chuoi de tim
    if pos!=-1:
        tim=True
        print('tim thay | '+keyword+' |trong:'+s+' tai vi tri: '+str(index+1)) #str(index+1) so o dang chuoi
if tim==False:
    print('khong tim thay')
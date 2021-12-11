#import thu vien
import time
import calendar
import math
#nhap ngay thang nam
day=int(input('nhap vao ngay: '))
month=int(input('nhap vao thang: '))
year=int(input('nhap vao nam: '))
#xuat ngay thang nam theo dinh dang ngay-thang-nam
print('ngay thang nam vua nhap: '+str(day)+'-'+str(month)+'-'+str(year))
#nam nhap vao co phai la nam nhuan hay khong
if calendar.isleap(year)==True:
    print('nam '+str(year)+' la nam nhuan')
else:  
    print('nam '+str(year)+' khong la nam nhuan')
#thang nhap vao co so ngay
s=calendar.monthrange(year,month)
# print(s)
# s1=s[1]
for element in s:
    if s.index(element)==1:
        print('so ngay trong thang 2 la: ',element)
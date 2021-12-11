import math
a=eval(input('nhap vao so thu a ='))
b=eval(input('nhap vao so thu b ='))
c=eval(input('nhap vao so thu c ='))
delta=math.pow(b,2)-4*a*c
if a == 0:
    print('day khong phai la phuong trinh bac 2')
#tinhketqua
elif delta<0:
    print('phuong trinh vo nghiem')
elif delta==0:
    x1=x2=-b/(2*a)
    print('phuong trinh co nghiem kep= %.2f'%x1)
elif delta>0:
    x1=((-b+math.sqrt(delta))/(2*a))
    x2=((-b-math.sqrt(delta))/(2*a))
    print('phuong trinh co 2 nghiem phan biet x1=%.2f va x2=%.2f'%(x1,x2))
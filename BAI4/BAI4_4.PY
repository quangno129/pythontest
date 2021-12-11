import math
a=eval(input('nhap vao canh tam giac a:'))
b=eval(input('nhap vao canh tam giac b:'))
c=eval(input('nhap vao canh tam giac c:'))
p=(a+b+c)/2
dientich=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('dien tich tam giac: %.2f'%(dientich))
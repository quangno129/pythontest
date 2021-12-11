n=int(input('nhap vào số nguyên n='))
#tổng các số lẻ nhỏ hơn hay bằng n
s=0
for i in range(n+1):
    if i%2==0:
        continue
    s+=i
print('tổng các số lẻ nhỏ hơn hay bằng n=',s)
#tổng các số chẵn nhỏ hơn hay bằng n
s1=0
for i in range(n+1):
    if i%2!=0:
        continue
    s1+=i
print('tổng các số chẵn nhỏ hơn hay bằng n=',s1)
#tích các số từ 1 tới n
s2=1
for i in range(1,n+1):
    s2*=i
    i+=1
print('tích các số từ 1 tới n=',s2)
#tích các số chia hết cho 3 nhỏ hơn hay bằng n
s3=1
for i in range(1,n+1):
    if i%3==0:
        s3*=i
        i+=1
print('tích các số chia hết cho 3 nhỏ hơn hay bằng n=',s3)
#tổng các số nguyên tố nhỏ hơn hay bằng n
tongcacsonguyento=0
for f in range(2,n+1):
    if f == 2:
        tongcacsonguyento+=2
    if f>2:
        lasonguyento=True
        for g in range(2,f):
            if f%g==0:
                lasonguyento=False
                break
        if lasonguyento==True:
            tongcacsonguyento+=f
if n==1:
    print('so nguyen to phai la so khac 1')
print('tổng các số nguyên tố=',tongcacsonguyento)


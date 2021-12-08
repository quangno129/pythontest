list=[1,2,3,4,5,6,7,8,9]
list1=[]
tongcacsonguyento=0
for f in list:
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
            f.append(list1)

print('tổng các số nguyên tố=',tongcacsonguyento)
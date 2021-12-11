list=[]
y=1
#nhap vao list
while y==1:
    nhapgiatri=int(input('nhap gia tri:'))
    y=int(input('tiep tuc nhap gia tri? 1:continute 0:stop'))
    list.append(nhapgiatri)
nums=set(list)
print(nums)
#tinh tong cac so nguyen to
list1=[]
tongcacsonguyento=0
for f in list:
    if f>=2:
        lasonguyento=True
        for g in range(2,f):
            if f%g==0:
                lasonguyento=False
                break
        if lasonguyento==True:
            tongcacsonguyento+=f
            list1.append(f)
nums_1=set(list1)
print('cac so nguyen to bao gom: ',list1)
print('tổng các số nguyên tố=',tongcacsonguyento)
#phan tu am trong list
list_3=[]
for f in list:
    if f<0:
        list_3.append(f)       
print('cac phan tu am',list_3)
avg = sum(list_3)/len(list_3)
print("The average is ",avg)
#phan tu duong trong list
list_4=[]
for f in list:
    if f>0:
        list_4.append(f)       
print('cac phan tu duong',list_4)
avg = sum(list_4)/len(list_4)
print("The average is ",avg)
#gia tri max trong list
print('gia tri max trong list',max(list))
#gia tri min trong list
print('gia tri min trong list',min(list))
#sap xep tang dan
list=list.sort()
print('list sap xe tang dan',list)
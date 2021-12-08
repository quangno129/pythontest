nhapvaosonguyenN=int(input('nhapvaosonguyen N: '))
sum=0
for i in range(1,nhapvaosonguyenN+1):
    nhapvaoNsonguyen=int(input('nhap so nguyen thu %i: '%i))
    sum+=nhapvaoNsonguyen
print('tong cac so nguyen nhap vao= ',sum)

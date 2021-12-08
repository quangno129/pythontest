loaiphong=int(input('nhap vao loai phong: '))
sodem=int(input('nhap vao so dem: '))
dongia=0
thanhtien=0
# xet cac loai phong
if loaiphong==1:
    dongia=1260000
elif loaiphong==2:
    dongia=1550000
elif loaiphong==3 or loaiphong==4:
    dongia=1830000
elif loaiphong==5 or loaiphong==6:
    dongia=2120000
elif loaiphong==7:
    dongia=2540000
elif loaiphong==8:
    dongia=4800000
#xet cac dem su dung
if sodem==1:
    thanhtien=dongia*sodem
elif 2<=sodem<=3:
    thanhtien=sodem*dongia*0.75
else:
    thanhtien=sodem*dongia*0.7
print('thanh tien %d VND'%thanhtien)
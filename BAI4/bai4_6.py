loaixe=eval(input('nhap vao loai xe: '))
km=eval(input('nhap vao so km: '))
thoigiancho=eval(input('nhap vao thoi gian cho: '))
x=(thoigiancho-5)*750
if loaixe == 4:
    if   km <= 0.8 and thoigiancho <= 5:
        tienxe=11000*km
    elif  km <=0.8 and thoigiancho >=5:
        tienxe=11000*km
    elif 0.8 <= km <= 30 and thoigiancho <=5:
        tienxe=15300*km
    elif 0.8 <= km <= 30 and thoigiancho >= 5:
        tienxe=15300*km
    elif km >= 30 and thoigiancho <= 5:
        tienxe=12100*km
    elif km >= 30 and thoigiancho >= 5:
        tienxe=12100*km
tientong=tienxe+x
print('tien cuoc xe: %.3f VND'%tienxe)
print('tien cho: %.3f VND'%x)
print('tong so tien tra: %3f VND'%tientong)

    

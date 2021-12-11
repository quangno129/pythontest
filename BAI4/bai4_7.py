sokwh=float(input('nhap vao so điện sử dụng: '))
if sokwh <= 50:
    tiendien=1.484*sokwh
elif 51 <= sokwh <= 100:
    tiendien=1.533*(sokwh-50)+50*1484
elif 101 <= sokwh <= 200:
    tiendien=1.786*(sokwh-100)+50*1484+50*1533
elif 201 <= sokwh <= 300:
    tiendien= 2.242*(sokwh-200)+50*1484+1533*50+100*1786
elif 301 <= sokwh <= 400:
    tiendien=2.503*(sokwh-300)+50*1484+1533*50+100*1786+100*2242
elif sokwh >= 400:
    tiendien=2.587*(sokwh-400)+50*1484+1533*50+100*1786+100*2242+2503*100
    print('so tien dien phải trả: %.3f VND'%tiendien)
else:
    print('nhập sai giá trị')
print('end')

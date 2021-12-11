x=eval(input('nhap loai phong từ 1 đến 8:'))
y=eval(input('nhap vào số đêm '))
if x == 1:
    if y <= 1:
        thanhtien=1260000*y
    elif 2 <= y <= 3:
        thanhtien=1260000*y-1260000*y*25/100
    elif y >= 4:
        thanhtien=1260000*y-1260000*y*30/100
if x == 2:
    if y <= 1:
        thanhtien=1550000*y
    elif 2 <= y <= 3:
        thanhtien=1550000*y-1550000*y*25/100
    elif y >= 4:
        thanhtien=1550000*y-1550000*y*30/100
if x == 3:
    if y <= 1:
        thanhtien=1830000*y
    elif 2 <= y <= 3:
        thanhtien=1830000*y-1830000*y*25/100
    elif y >= 4:
        thanhtien=1830000*y-1830000*y*30/100 
if x == 4:
    if y <= 1:
        thanhtien=1830000*y
    elif 2 <= y <= 3:
        thanhtien=1830000*y-1830000*y*25/100
    elif y >= 4:
        thanhtien=1830000*y-1830000*y*30/100    
if x == 5:
    if y <= 1:
        thanhtien=2120000*y
    elif 2 <= y <= 3:
        thanhtien=2120000*y-2120000*y*25/100
    elif y >= 4:
        thanhtien=2120000*y-2120000*y*30/100
if x == 6:
    if y <= 1:
        thanhtien=2120000*y
    elif 2 <= y <= 3:
        thanhtien=2120000*y-2120000*y*25/100
    elif y >= 4:
        thanhtien=2120000*y-2120000*y*30/100
if x == 7:
    if y <= 1:
        thanhtien=2540000*y
    elif 2 <= y <= 3:
        thanhtien=2540000*y-2540000*y*25/100
    elif y >= 4:
        thanhtien=2540000*y-2540000*y*30/100
if x == 8:
    if y <= 1:
        thanhtien=4800000*y
    elif 2 <= y <= 3:
        thanhtien=4800000*y-4800000*y*25/100
    elif y >= 4:
        thanhtien=4800000*y-4800000*y*30/100    
print('số tiền: %.2f VND'%thanhtien)
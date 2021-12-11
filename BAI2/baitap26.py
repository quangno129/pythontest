laisuat=eval(input('nhap lai suat: '))
sotiengui=eval(input('nhap so tien gui: '))
sothanggui=eval(input('nhap so thang gui: '))
tienlai=(sotiengui*sothanggui)*(laisuat/100/12)
tongsotien=sotiengui+tienlai
print('so tien lai %.2f VND,tong so tien %.2f VND'%(tienlai,tongsotien))
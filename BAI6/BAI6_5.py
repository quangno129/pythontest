n=str(input('nhap vao chuoi n='))
if n.isdigit()==True:
    if len(n)==6:
        print('day la ma zip VN')
    else:
        print('day khong phai la ma zip VN')
else:
    print('day khong phai la ma zip VN')
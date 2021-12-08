n=int(input('n = '))
if n<2:
    print('n không phải là số nguyên tố')
else:
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if flag==True:
        print(n,'là số nguyên tố')
    else:
        print(n,'không phải là số nguyên tố')
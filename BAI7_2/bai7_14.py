dsDanhBa={'quang':'0924456682','vinh':'0583150263','hao':'0363587897'}
tt =1
while tt ==1:
    chon=int(input('ban muon lam gi? 1: xem danh ba 2: tim kiem 3:them moi     '))
    if chon==1:
        print('danh ba dien thoai:')
        print('ten \t\t so dien thoai')
        for i in dsDanhBa:
            print(i,'\t\t\t',dsDanhBa[i])
    elif chon ==2:
        name=str(input('nhap name can tim'))
        flag=False
        for i in dsDanhBa:
            if name==i:
                print(i,'\t\t\t',dsDanhBa[i])
                flag=True
                break
        if flag==False:
            print('khong tim thay')
    elif chon ==3:
        name=str(input('Ten:\n\n'))
        soDT=int(input('so dien thoai: '))
        dsDanhBa[name]=soDT
        print('danh ba ms them vao: \n')
        for i in dsDanhBa:
            print(i,'\t\t\t',dsDanhBa[i])
    else:
        print('khong biet ban muon lam gi?')
    tt=int(input('ban co muon tiep tuc: (1:TT): '))
        

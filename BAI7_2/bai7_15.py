dic={'cat':'con meo','dog':'con cho','ant':'con kien','bear':'con gau'}
tt =1
while tt ==1:
    chon=int(input('ban muon lam gi? 1: xem tu dien 2: tim kiem 3:them tu 4:xoa tu     '))
    if chon==1:
        print('dictionary')
        print('tu anh \t\t\t nghia viet')
        for i in dic:
            print(i,'\t\t\t',dic[i])
    elif chon == 2:
        search=input('nhap tu dien can tra')
        flag=False
        for i in dic:
            if i ==search:
                print(i,'\t\t\t',dic[i])
                break
        if flag==False:
            print('khong tim thay')
    elif chon ==3:
        tuanh=str(input('tu anh:\n\n\n'))
        nghiaviet=int(input('nghia viet: '))
        dic[tuanh]=nghiaviet
        print('tu dien moi them vao: \n')
        for i in dic:
            print(i,'\t\t\t',dic[i])
    elif chon == 4:
        print('nhap tu can xoa')
        tuanhxoa=str(input('tu anh:  '))
        yn=int(input('ban co that su co muon xoa khong: 1:xoa, 0:khong'))
        if yn==1:
            del dic[tuanhxoa]
            print('tu dien moi xoa: \n')
            for i in dic:
                print(i,'\t\t\t',dic[i])
    else:
        print('khong biet ban muon lam gi?')
    tt=int(input('ban co muon tiep tuc: (1:TT): '))

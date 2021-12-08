sample=[{'name':'Peach','item':['green shell','banana','green shell',],'finish': 3},
        {'name':'Bower','item':['green shell',],'finish': 1},
        {'name':None,'item':['mushroom',],'finish': 2},
        {'name':'Toad','item':['green shell','mushroom',],'finish': 1},
] 
#{} dictionary ben trong mang name:value
#() tuble khong thay doi dc
#[] mang thay doi dc
#xu ly chuong trinh
for element in sample:
    if element["finish"]==1:
        print(str(sample.index(element))+':'+str(len(element['item'])))

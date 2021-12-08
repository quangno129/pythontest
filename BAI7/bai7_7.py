list=[1,2,3,4]
list_1=[]
thresh=2
for i in list:
    if i>thresh:
        i=True
        list_1.append(i)
    else:
        i=False
        list_1.append(i)
print(list_1)

#tao list voi 10 chieu cao(don vi tinh la inch)
list=[74,74,72,72,73,69,69,71,76,71]
#doi inch sang met
list_met=[]
for i in list:
    i=i*0.0254
    list_met.append(i)
print(list_met)
#in ra 3 chieu cao dau tien
print(list_met[0],list_met[1],list_met[2])
#in ra 3 chieu cao cuoi cung
print(list_met[-1],list_met[-2],list_met[-3])
#in ra chieu cao trung binh
avg = sum(list_met)/len(list_met)
print("The average is ",avg)


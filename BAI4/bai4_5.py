nam=float(input('nhap vao nam :'))
if (nam%4 == 0 and nam%100 != 1) or (nam%400 == 0):
    print('năm nhuần')
else:
    print('không phải năm nhuần')
print('end')
list=['a','b','c','d','e','f']
print('list of animals: ',list)
print('number of animals: ',len(list))
#nhap vao thu can tim
findanimals=str(input('nhap vao thu can tim: '))
if any(findanimals in s for s in list):
    print('co animals:',findanimals)
else:
    print('not find enimals')
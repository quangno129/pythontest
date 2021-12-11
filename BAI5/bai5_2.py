n=int(input('n='))
x=int(input('x='))
s=1
for i in range(n):
    s*=(x*x+1)
print('s=',s)
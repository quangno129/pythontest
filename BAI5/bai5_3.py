n=int(input('n='))
x=int(input('x='))
s=1
z=1
for i in range(n):
    s*=(x*x+x+1)
for i in range(n):
    z*=(x*x-x+1)
A=s+z
print(A)
n=int(input())
f=1
for i in range(1,n):
    if n%i==0:
        f=f+i
if f>n:
    print('True')
else:
    print('False')
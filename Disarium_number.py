import math
n=int(input())
temp=n
c=0
while temp!=0:
    temp=temp//10
    c+=1
temp=n
s=0
while temp!=0:
    r=temp%10
    s=s+pow(r,c)
    temp=temp//10
    c-=1
if s==n:
    print('True')
else:
    print('False')
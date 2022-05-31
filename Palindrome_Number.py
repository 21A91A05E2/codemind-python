t=int(input())
for i in range(1,t+1):
    n=int(input())
    s=0
    temp=n
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if temp!=s:
        print('False')
    else:
        print('True')
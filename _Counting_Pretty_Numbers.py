a=int(input())
for i in range(a):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        if i%10==2 or i%10==3 or i%10==5:
            c+=1
    print(c)
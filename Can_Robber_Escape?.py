n=int(input())
odd=0
a=list(map(int,input().strip().split()))
for i in range(len(a)):
    if a[i]%2!=0:
        odd+=1
if odd<=2:
    print('YES')
else:
    print('NO')
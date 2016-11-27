
lst=[]

t=int(input())
for a0 in range(t):
    count = 0
    n,m,c = input().strip().split()
    n,m,c = int(n), int(m), int(c)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i * j == c:
                count += 1
    lst.append(count)

for k in lst:
    print (k)

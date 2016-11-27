n,m=input().strip().split()
n,m=int(n),int(m)
ar=input().split()
a=[int(num) for num in ar]

lst=[]
for a0 in range(m):
    f,p,s=input().strip().split()
    f,p,s=int(f),int(p),str(s)
    l=[]
    l.append(f)
    l.append(p)
    l.append(s)
    lst.append(l)
lst1=[]
for i in range(m):
    if lst[i][0] in a:
        lst1.append(lst[i])
lst1.sort(key=lambda x: x[1] , reverse = True)

lst2=[]
for i in range(m):
    if lst[i] not in lst1:
        lst2.append(lst[i])
lst2.sort(key=lambda x: x[1] , reverse = True)

list0=[]
for j in lst1:
    list0.append(j)
for j in lst2:
    list0.append(j)

for k in list0:
    print (k[2])

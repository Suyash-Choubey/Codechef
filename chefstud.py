t = int(input())
l=[]
for a0 in range(t):
	lst = list(input())
	count=0
	for i in range(len(lst)-1):
		if(lst[i]=='<' and lst[i+1]=='>'):
			count=count+1
	l.append(count)

for k in l:
    print (k)
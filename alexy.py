t=int(input())
def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
def lcm(a,b):
	return (a*b)//gcd(a,b)
def check(x):
	a=[]
	for i in range(len(x)-1):
		for j in range(i+1,len(x)):
			a.append(lcm(x[i],x[j]))
	return min(a)
 
for i in range(t):
	n=int(input())
	x=list(map(int, input().split()))
	print(check(x))
 
T=int(input())
for a in range(T):
	x,y=map(int,input().split())
	maxx=max(x,y)
	num=(maxx-1)**2
	if (num%2==0):
		num=num+y+(maxx-x)
	else:
		num=num+x+(maxx-y)
	print(num)
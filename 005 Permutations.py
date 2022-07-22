def Permutations(num):
	if num==1:
		print(1)
	if 1<num<4:
		print("NO SOLUTION")
	else:
		for a in range(2,num+1,2):
			print(a,end=" ")
		for a in range(1,num+1,2):
			print(a,end=" ")


num=int(input(""))
Permutations(num)
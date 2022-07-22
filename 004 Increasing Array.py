num=int(input(""))
numbers=list(map(int,input("").split(" ")))
moves=0
for a in range(len(numbers)-1):
	if numbers[a]>numbers[a+1]:
		moves+=(numbers[a]-numbers[a+1])
		numbers[a],numbers[a+1]=numbers[a+1],numbers[a]
print(moves)
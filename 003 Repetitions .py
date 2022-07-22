def Repetitions(string):
	max=1
	count=1
	for a in range(len(string)-1):
		if string[a]==string[a+1]:
			count+=1
		else:
			count=1
		if max<count:
			max=count
	print(max)


string=input("")
Repetitions(string)
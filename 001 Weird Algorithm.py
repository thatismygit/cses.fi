def algo(num):
	if num==1:
		# for 1 in the end
		print(1,end="")
	elif num%2==0:
		# for even num
		print(num,end=" ")
		ans=num//2
		algo(ans)
	else:
		# for odd num
		print(num,end=" ")
		ans=(num*3)+1
		algo(ans)
num=int(input(""))
algo(num)
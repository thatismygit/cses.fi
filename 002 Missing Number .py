# input number for upper range
length=int(input(""))

# takes numbers as list
numbers=list(map(int,input("").split(" ")))

# total is a full list till upper range without any missing value
total=list(range(1,length+1))

# just takes the sum of list with and without missing value
sum1=sum(numbers)
sum2=sum(total)

# by subtracting the number we get missing number
print(sum2-sum1)
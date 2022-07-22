string = input("")
single=[]
pair=[]

for char in string:
    if char in single:
        single.remove(char)
        pair.append(char)
    else:
        single.append(char)

ans="".join(pair) + "".join(single) + "".join(pair[::-1])

if ans==ans[::-1]:
    print(ans)
else:
    print("NO SOLUTION")
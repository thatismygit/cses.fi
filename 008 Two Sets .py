def display(set1,set2):
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)


def doit(total):
    set0=[*range(1,num+1)]
    set1=[]
    set2=[]
    print("YES")
    target=total/2
    index=len(set0)-1
    for a in set0:
        element=set0[index]
        if element<=target and target!=0:
            set2.append(element)
            target-=element
        else:
            set1.append(element)
        index-=1
    display(set1,set2)


num=int(input(""))
total=(num*(num+1))/2
if total%2!=0:
    print("NO")
else:
    doit(total)
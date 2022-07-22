T=int(input(""))
for _ in range(T):
        x,y=map(int,input("").split(" "))
        cond1=max(x,y)<=2*(min(x,y))
        cond2=(x+y)%3==0
        if  cond1 and cond2:
                print("YES")
        else:
                print("NO")
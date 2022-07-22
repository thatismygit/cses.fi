for n in range(1,int(input(""))+1):
        knight1=n**2
        knight2=(n**2)-1
        totalways=(knight1*knight2)//2
        totalhits=4*(n-1)*(n-2)
        print(totalways-totalhits)
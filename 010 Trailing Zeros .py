num=int(input(""))
ans=0
catch=5
while num/catch>=1:
    ans+=num//catch
    catch*=5
print(ans)
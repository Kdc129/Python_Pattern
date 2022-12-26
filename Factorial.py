def Fact(n):
    result =1
    while(n>=1):
        result*=n
        n-=1
    return result

for i in range(1,10):
    print(f"Factor of {i} is {Fact(i)}")

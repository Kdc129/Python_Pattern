"""

Input a number ::4
4 3 2 1 
4 3 2 1 
4 3 2 1 
4 3 2 1 

"""

n = int(input("Input a number ::"))

for i in  range(n):
    k=n
    for j in range(n):
        print(k,end =" ")
        k-=1
    print()
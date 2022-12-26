"""

Input a number ::4
D C B A 
D C B A 
D C B A 
D C B A 

"""

n = int(input("Input a number ::"))

for i in  range(n):
    k=65+n-1
    for j in range(n):
        print(chr(k),end =" ")
        k-=1
    print()
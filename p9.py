"""

Input a number ::4
D C B A 
D C B A 
D C B A 
D C B A 

"""

n = int(input("Input a number ::"))

for i in  range(n):
    for j in range(n):
        print(chr(65+n-j-1),end =" ")
    print()
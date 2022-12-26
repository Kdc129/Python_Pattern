"""

Input a number ::4
4 4 4 4 
3 3 3 3 
2 2 2 2 
1 1 1 1 

"""

n = int(input("Input a number ::"))

for i  in range(n):
    print((str(n-i)+" ")*n)
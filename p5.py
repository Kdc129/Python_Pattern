"""
Input a number ::4
1 
2 3 
4 5 6 
7 8 9 10 

"""


n = int(input("Input a number ::"))
k = 1
for i in  range(n):
    for j in range(i+1):
        print(k,end =" ")
        k+=1
    print()

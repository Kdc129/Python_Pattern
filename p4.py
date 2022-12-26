"""
Input a number ::4
1 
2 2 
3 3 3 
4 4 4 4 

"""


n = int(input("Input a number ::"))
j = 1
for i in  range(n):
    print((str(i+1)+" ")*j);
    j+=1
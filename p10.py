"""

Input a number ::4
* 
* * 
* * * 
* * * * 

"""

n = int(input("Input a number ::"))
k =1
for i in  range(n):
        print((str('*')+" ")*k)
        k+=1
   

no = int(input("Input a number ::"))
digit = 0
sum = 0
while no != 0:
    digit =no%10
    sum+=digit
    no=no//10 

print(sum)
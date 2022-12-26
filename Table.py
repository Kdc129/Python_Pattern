print()
S = int(input("Enter a number of starting ::"))
D = int(input("Enter a number of ending ::"))
print()
print("Table Starting from",S,"to",D,"are as follows::")
for i in range(S,D+1,1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print("\t")
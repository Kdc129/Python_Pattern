def sum(*n):
    total = 0
    no=0
    for no in n:
        total+=no
    print(f"SUM of {n} = {total}")

sum()
sum(90)
sum(34,56,7.8)
sum(10,20,30)



global z      #we can define global variable by using global keyword
z = 100
x = 10        #global variable

def Max():
    y = 79   #local variable
    x = 89   #we modify value inside global variable
    if x>y:
        print(f"{x} is greater than {y}")
    else:
        print(f"{y} is greater than {x}")


Max()

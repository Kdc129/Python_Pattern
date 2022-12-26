x = lambda y,z:(y+z)
x1 = lambda y,z:(y-z)

x2 = lambda y,z:(y*z)
x3 = lambda y,z:(y/z)

a = int(input("Input first number :"))
b = int(input("Input second number :"))

print(f"Addition of two number is ::{x(a,b)}")
print(f"Subtraction of two number is ::{x1(a,b)}")
print(f"Multiplication of two number is ::{x2(a,b)}")
print(f"Division of two number is ::{x3(a,b)}")
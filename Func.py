
def Add(a,b):
    return (a+b)

def Mult(a,b):
    return (a*b)

def Sub(a,b):
    return (a-b)
 
def Div(a,b):
    return (a/b)


x = int(input("Input a first number ::"))
y = int(input("Input a second number ::"))

AR = Add(x,y)
print("Addition is ::",AR)
SR = Sub(x,y)
print("Subtraction is ::",SR)
MR = Mult(x,y)
print("Multiplication is ::",MR)
 
if x>=y:
   DR = Div(x,y)
   print("Division is ::",(DR))
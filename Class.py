class demo:
    def __init__(no,r,s):
        no.r = r
        no.s = s
    def Sum(no):
        result=0
        for i in range(no.r,no.s+1):
            result+=i
        return result
    
class base(demo):
    def __init__(no, x, y,r,s):
        super().__init__(r, s)
        no.x = x 
        no.y = y
    def mul(no):
        print("Multiplication of number",no.x,"and",no.y,"is ::",no.x*no.y)
    
obj = base(11,2,3,4)
R = obj.Sum()
obj.mul()
print("Sum of number",obj.r,"to",obj.s,"is ::",R)


           
def smart_divide(func):
    def inner(a,b):
        print("I am going to divide", a,"by",b)
        if b==0:
            print("OOPS!!, can not divide, change the denominator value..")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

p = divide(10,5)
print(p)

q = divide(100,0)
print(q)
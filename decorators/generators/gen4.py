def myPowGen(max=0):
    n = 0
    while n<=max:
        yield 2 ** n
        n+=1

it = myPowGen(5)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  it raises a stop iteration exception...

'''
for p in myPowGen(5):
    print(p)
'''
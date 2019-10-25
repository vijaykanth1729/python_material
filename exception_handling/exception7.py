# User defined exceptions...
'''
exceptions defined by a programmer are called user defined exceptions..
 User defined exceptions always contains raise key word..
'''

class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 10
while True:
    try:
        i_num = int(input("enter a no: "))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break

    except(ValueTooSmallError):
        print("This value is too small, try Again!!!")

    except(ValueTooLargeError):
        print("This value is too large, try again!!!!")

print("Congrazulations!!!, You guessed it correct")


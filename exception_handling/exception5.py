# Default except block, can able to handle any type of exception..

# a program can able to have single try with  multiple except blocks...

# while defining multiple except blocks, always remember to place default except block at the end..
#otherwise we get an error..SyntaxError: default 'except:' must be last



print("begining my program")



try:
    i = int(input("enter a first_no: "))
    j = int(input("enter a second_no: "))

    k = i/j

except(ValueError):
    print("This is a Value Error")


except:
    print("Error Occured!!!")

except(ZeroDivisionError):
    print("This is a Zero Division Error")




#print(k)

print("ending my program..")

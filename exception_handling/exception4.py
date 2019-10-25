# Default except block, can able to handle any type of exception..

# a program can able to have single try with  multiple except blocks...

# while defining multiple except blocks, always remember to place default except block at the end..
#otherwise we get an error..



print("begining my program")



try:
    i = int(input("enter a first_no: "))
    j = int(input("enter a second_no: "))

    k = i/j
    print(k)

except(ValueError):
    print("This is a Value Error")

except(ZeroDivisionError):
    print("This is a Zero Division Error")

except:
    print("Error Occured!!!")


#

print("ending my program..")

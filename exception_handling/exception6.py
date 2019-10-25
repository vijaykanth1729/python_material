# except block should compulsory have try block,

# every try block should always include an except block

# finally block with try and except is an optional..


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

finally:
    print("This will be executed always, irrespective of exceptions..")





print("ending my program..")
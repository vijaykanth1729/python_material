print("begining my program")



try:
    i = int(input("enter a first_no: "))
    j = int(input("enter a second_no: "))

    k = i/j
    print(k)

except(ZeroDivisionError):
    print("Please use denominator other then Zero")


#print(k)

print("ending my program..")

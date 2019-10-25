def my_gen():
    n=1
    print("This is printed first:")
    yield n
    n+=1
    print("This is printed second")
    yield n
    n+=1
    print("This is printed third: ")
    yield n

it = my_gen()
while True:
    try:
        print(next(it))
    except(StopIteration):
        print("Generator execution Completed!!")
        break



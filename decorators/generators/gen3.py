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

# for loop can automatically handling the stopiteration exception..

for p in my_gen():
    print(p)
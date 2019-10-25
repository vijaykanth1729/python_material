# from import way is a very flexible and industy wise usage way of defining modules...
# from import avoids the memory consumption usage...
# it will load only the required information from the moodule...
# if we use from import we can call the required things as like the same file...
# this is the best approach ...

from demo import a, fun

d = 4000
def func_test3():
    print("this is a function from test3 file")

print(d)
func_test3()

print(a)
fun()

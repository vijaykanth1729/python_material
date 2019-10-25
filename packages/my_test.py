import main_package.a
from main_package.b import b, f2
import main_package.sub_package.c as temp
from main_package.sub_package.d import *

# this will print info about 'a' file
print(main_package.a.a)
main_package.a.f1()

# this will print info about 'b' file
print(b)
f2()

# this will print info about 'c' file
print(temp.c)
temp.f3()

# this will print info about 'd' file
print(d)
f4()


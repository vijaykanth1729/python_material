'''
os module is a predefined module, which provides some functions, and by using those functions we can perform
the operating system related activities like executing os commands working with process ..

'''
import os
print("This is current directory: ", os.getcwd())

os.chdir("sample")

print("This is current directory: ", os.getcwd())

os.chdir(os.pardir)


print("This is current directory: ", os.getcwd())
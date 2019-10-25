class Decorator:
    def __init__(self,func):
        self.func = func

    def __call__(self,name):
        if name=="vijay":
            return f"hey vijay"
        else:
            return self.func(name)


@Decorator
def welcome(name):
    return f"Hello welcome, {name}"

print(welcome('ajay'))
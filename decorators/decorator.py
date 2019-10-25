def make_pretty(func):      # decorator function ....
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty      # decorator ...
def ordinary():   # decorated function ...
    print("iam ordinary")

ordinary()
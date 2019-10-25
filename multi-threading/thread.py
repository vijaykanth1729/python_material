import threading


class X(threading.Thread):
    def run(self):
        for p in range(1,101):
            print(p)

class Y(threading.Thread):
    def run(self):
        for p in range(101,201):
            print(p)


x1 = X()
y1 = Y()
#x1.run()   #to excute the method as a thread we need to call start method on it
x1.start()
y1.start()

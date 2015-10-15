# Author: Jayden Navarro
# Date: 10/14/2015

def boundsCheck1(func):
    def wrapper(*args, **kwargs):
        if (args[0] >= 0 and args[0] <= 100):
            func(*args, **kwargs)
        else:
            print("%d out of range." % args[0])
    return wrapper

def boundsCheck2(func):
    def wrapper(*args, **kwargs):
        if (args[0] >= 25 and args[0] <= 75):
            func(*args, **kwargs)
        else:
            print("%d out of range." % args[0])
    return wrapper

@boundsCheck2
@boundsCheck1
def hello1(num):
    print("Hello World! %d" % num)

@boundsCheck1
def hello2(num):
    print("Hello World! %d" % num)

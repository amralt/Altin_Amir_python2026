from functools import wraps

def mock(msg):
    def param(func):
        wraps(func)
        def wrapper(*args, **kwarg):
            return msg
        return wrapper
    return param

@mock("HAHA")
def f(a,b,c):
    return a+b+c

def g(a,b,c):
    return a*b*c

if __name__ == '__main__':
    print(f(1,2,3))
    print(g(1,2,3))
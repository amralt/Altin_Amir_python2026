
def req_fib(n :int) :
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return  req_fib(n-1) + req_fib(n-2)

    

def fib_for(n :int) :
    s1, s2 = 0, 1
    for i in range(n) :
        a = s1
        s1 = s2
        s2 = a + s2
    return s1


print(req_fib(10))
print(fib_for(10))
        

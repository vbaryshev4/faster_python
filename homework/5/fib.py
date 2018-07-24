from functools import lru_cache

def fib(n):
    
    index = 1

    result = 1
    prev = 0
    result += prev
    
    while index != n:
        #print(result)
        result += prev
        prev = result - prev
        index += 1

    return result

print(fib(100))

@lru_cache(maxsize=None)
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(100))
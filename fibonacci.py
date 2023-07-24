def fibonacci(fib):
    count = 0
    fib_list = []
    first = 0
    second = 1
    for i in range(fib):
        temp = first
        first = second
        second = temp + first
        
        
        if i == fib - 1:
            print(temp)


fibonacci(0)

# 0 1 1 2 3 5 8 13 21 34 
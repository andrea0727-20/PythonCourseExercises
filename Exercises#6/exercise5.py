def fibonacci(limit):
    a = 0
    b = 1

    while a <= limit:
        print( a , end = " ")
        temp = a + b
        a = b
        b = temp
    print()

fibonacci(100)
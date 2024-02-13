#Question 2: Fibonacci Sequence
def fabonacci(limit):
     a, b = 0, 1
     while a< limit:
        print(a, end=" ")
        a, b = b ,a + b
fabonacci(100)
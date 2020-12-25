'''
Author: Lucas Wye<lucas.zw.ye@outlook.com>
Date: 2020-12-25 13:23:32
Description: Fibonacci Calculation
'''
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 20):
    print(i, fib(i))
n = 5


def fib(n):
  if n == 0:
    return 0
  if n ==1:
    return 1
  else:
    return fib(n - 1) + fib(n-2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

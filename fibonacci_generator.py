def fibonacci(n):
    """Generate and print the first n numbers of the
    fibonacci sequence."""

    fib2 = 1
    fib1 = 0

    for i in range(0, n):
        print(fib2, end=", ")

        fib2_old = fib2

        fib2 = fib2 + fib1
        fib1 = fib2_old


fibonacci(int(input("How many digits of the fibonacci sequence \
do you want to calculate? ")))

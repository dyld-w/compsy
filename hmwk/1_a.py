def factorial(n):
    """
    this is the docstring
    """

    if n == 1:
        return 1

    return n * (n - 1)


inp = int(input("value "))
ouput = factorial(inp)

print(ouput)

def factorial (n):
    f = 1
    for i in range(1, n+1, +1):
        f = f * i
    return f

num = int (input('Enter a number to determine the factorial:\n'))
print ( 'Factorial of {0} is:\n'.format(num),factorial(num))
'''
factorial of given number
'''
num1 = int(input('Enter a value'))


def factorial(n):
    if n < 0:
        return 'Factorial doesnt exist for negative integers'
    elif n == 0 or n == 1:
        return 1
    else:
        i = 1
        fac = 1
        while i <= n:
            fac *= i
            i += 1
        return fac


if __name__ == '__main__':
    print(factorial(num1))
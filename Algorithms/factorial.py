'''Factorial is the one of the most common algo example which 
is worked on the `4! = 1*2*3*4 = 24, OR n! = (n-2)*(n-1)*n` formula.'''

def factorial_recursive(n):
    if n == 0:
        return 1
    return factorial_recursive(n-1)*n


num = int(input("Enter a number: "))
print(factorial_recursive(num))


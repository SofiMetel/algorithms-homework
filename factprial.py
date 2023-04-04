
def factorial_buzz(number):
    if number%3==0:
        ans = (f"Fizz! the factorial is {factorial(number)}")
    elif number%5==0:
        ans = (f"Buzz! the factorial is {factorial(number)}")
    else:
        ans = factorial(number)
    return ans
    



def factorial(n): 
    return 1 if n == 0 else n * factorial(n-1)

print(factorial_buzz(5))
print(factorial_buzz(8))
print(factorial_buzz(9))
print(factorial_buzz(10))
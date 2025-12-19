# prime number，在这个练习里我们熟悉一下函数的用法，简单的判断和循环来热热手
# 当然我们还用了列表推导式list comprehension，这个很方便
import math

def is_prime(num):
    if num < 2:
        return False
    for a in range (2, math.isqrt(num)+1):
        if num % a == 0:
            return False
    else:
        return True

def tell_if_prime(num):
    if not isinstance(num, int):
        return "Input must be an integer" # 这行其实是多余的，因为我们在主程序中就已经保证了是整数输入，但也不是完全没用因为这有可能被引用，这时候就有用了
    
    if num < 2:
        return f"{num} is not a prime number"
    
    for a in range (2, math.isqrt(num)+1):
        if num % a == 0:
            return f"{num} is not a prime number"
        
    return f"{num} is a prime number"

#n = int(input("Enter a number: "))
# if is_prime(n):
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number
#print(tell_if_prime(n))

# while True:
#     user_input = input("Enter a number (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         break
#     try:
#         n = int(user_input)
#         print(tell_if_prime(n))
#     except ValueError:
#         print("Please enter a valid integer.")

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]
# primes = []
# for number in numbers:
#     if is_prime(number):
#         primes.append(number)
primes = [number for number in numbers if is_prime(number)]
print("Prime numbers in the list:", primes)


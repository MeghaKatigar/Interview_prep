num = int(input("Enter a number to find fibanacci number"))


# def find_fibonacci(n):
#     if n <= 1 :
#         return 1
#     return find_fibonacci(n-1) + find_fibonacci(n-2)


# print(find_fibonacci(num))


#Another way

from functools import lru_cache

@lru_cache
def nth_fibonacci(n):
    if n<= 1:
        return 1
    return nth_fibonacci(n-1) - nth_fibonacci(n-2)

print(nth_fibonacci(num))
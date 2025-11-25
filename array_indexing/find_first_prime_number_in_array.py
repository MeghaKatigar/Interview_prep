from math import sqrt

a = [4, 8, 7, 8, 10, 11]


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False

    return True


# for i in range(len(a)):
#     if is_prime(a[i]):
#         print(a[i])
#         break


for x in a:
    if is_prime(x):
        print(x)
        break

import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        print(2%i)
        if n % i == 0:
            return False
    return True
print(is_prime(2)) 
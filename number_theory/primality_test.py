# primalytest

# O(N)
def is_prime_trivial(number):
    # buggy
    if number == 2:
        return True
    for i in range(3, number):
        if (number % i) == 0:
            return False
    return True

# O(N/2)
def is_prime_less_trivial(number):
    if number == 2: 
        return True
    if (number % 2) == 0:
        return False
    for i in range(3, number, 2):
        if (number % i) == 0:
            return False
    return True

# O(N/4)
def is_prime_even_less_trivial(number):
    if number == 2:
        return True
    if (number % 2) == 0:
        return False
    for i in range(3, int(number/2), 2):
        if (number % i) == 0:
            return False
    return True

# O(sqrt(N))
def is_prime_not_so_trivial(number):
    if number == 2:
        return True
    if (number % 2) == 0:
        return False
    upper_bound = int(number**0.5) + 1 # square root of number
    for i in range (3, upper_bound, 2):
        if (number % i) == 0:
            return False
    return True

if __name__ == '__main__':
    print(' N  N/2 N/4 sqrt(N)')
    for i in range(20, 40):
        if is_prime_trivial(i):
            print(i, ' ', end='')
        if is_prime_less_trivial(i):
            print(i, ' ', end='')
        if is_prime_even_less_trivial(i):
            print(i, ' ', end='')
        if is_prime_not_so_trivial(i):
            print(i, ' ', end='')
            print()
    print()
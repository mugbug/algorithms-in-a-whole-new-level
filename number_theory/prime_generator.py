from primality_test import is_prime_not_so_trivial

# O(N*is_prime(N))
def generate_prime_trivial(n):
    primes = []
    for i in range(2, n+1):
        if is_prime_not_so_trivial(i):
            primes.append(i)
    return primes

# O(N*log(log(N)))
def generate_prime_crivo(n):
    primes = []
    numbers = [i for i in range(n+1)]
    crossed = [False]*(n+1)

    for i in range(2,n+1):
        if not crossed[i]:
            primes.append(numbers[i])

        for j in range(numbers[i], n+1, numbers[i]):
            crossed[j] = True
        
    return primes

if __name__ == '__main__':
    print('O(N*is_prime(N))')
    for prime in generate_prime_trivial(20):
        print(prime, ' ', end = '')
    print('\n')
    print('O(N*log(log(N)))')
    for prime in generate_prime_crivo(20):
        print(prime, ' ', end = '')
    print()
def trivial_pow(x, y):
    result = x # first iteration is here
    for _ in range(y-1):
        result *= x
    return result

# exponentiation by squaring
def optimazed_pow(x, y):
    if y < 0:
        return optimazed_pow(1/x, -y)
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return optimazed_pow(x*x, y/2)
    elif y % 2 != 0:
        return x * optimazed_pow(x*x, (y-1)/2)
        

if __name__ == '__main__':
    print('Trivial power:', trivial_pow(2, 10))
    print('Exponentiation by squaring:', optimazed_pow(2, 10))
